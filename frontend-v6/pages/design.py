#v6
from app import app
from dash import html, dcc, callback, Input, Output, State, dash_table
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go

import pandas as pd
import requests
from collections import OrderedDict


from components import co2_sum, co2_bar, co2_comparison


df = pd.DataFrame(OrderedDict([
    ('ingrd', ["","","","",""]),
    ('q', [0.0,0.0,0.0,0.0,0.0]),
    ('u', ['g', 'g', 'g', 'g' , 'g'])
]))

################################################################
manual_input = dash_table.DataTable(id='manual-recipe-table',
                            data=df.to_dict('records'),
                            columns=[
                                {'id': 'ingrd', 'name': 'Ingredient'},
                                {'id': 'q', 'name': 'Quantity (g, default = 1g)', "type": "numeric"},
                                # {'id': 'u', 'name': 'Unit', 'presentation': 'dropdown'},
                            ],
                            editable=True,
                            # dropdown={
                            #     'u': {'options': [{'label': i, 'value': i} for i in ['g','kg']], 'clearable' : False}
                            # },
                        )

################################################################

# Define the page layout
layout = dbc.Container([
    dbc.Row([
        html.Center(className='page-title', 
                    children=[html.H2("Manual CO2 Calculator"),
                              html.P("Calculate g of CO2 emissions / kg of your meal"),
                              html.P("by entering ingredient and quantity manually"),
                              html.Hr()]),
        
    dbc.Row(className='page-contents', 
            children = [
            html.Div(className='manual-form',children=[
                html.Div(html.H4("Please fill in the table and press the calculate button !")), 
                html.Div(manual_input, style={'padding-top':'1%', 'padding-bottom':'2%'}),
                html.Div(dbc.Button('CALCULATION', id='manual_recipe_cal', color="secondary",size="rg",n_clicks=0)),        
                ]), 
            dbc.Row([ #result 
                         dbc.Row(className='co2-result-text', 
                                 children=[ dbc.Row(id='manual-total-co2',children=[])]),                            
                         dbc.Col(id='manual-co2-bar-fig', className='co2-bar', children=[])],
                         ),
                dbc.Row(id='manual-co2-comparison',children=[],style={'padding-bottom':'10%'})
        ])
    ])
])

LOCAL_TEST_URL = 'http://127.0.0.1:5000'
GCP_BACKEND_URL = 'http://34.78.60.82:5000'


@callback(
    Output('manual-total-co2','children'),
    Output('manual-co2-bar-fig','children'),
    Output('manual-co2-comparison','children'),
    Input('manual_recipe_cal', 'n_clicks'),
    State('manual-recipe-table', 'data'))
def update_manualrecipe_result(n_clicks, rows):
    totalco2_div = []
    bar_figure_div = []
    co2_comp_div= []

    if n_clicks > 0:
        backendURL = GCP_BACKEND_URL + '/calculatorCO2'

        ingrdSet = parsingManualTable(rows)
        if '' not in ingrdSet['ingrd']:
            response = requests.post(url = backendURL,  json = ingrdSet)
            if (response.status_code != 204 and
                response.headers["content-type"].strip().startswith("application/json")):
                try:
                    response_json = response.json()
                    totalco2, ingrdData = parsingManualCO2(response_json)
                    recipeName = "your manual recipe"
                    totalco2_div = co2_sum.Text(recipeName,totalco2)
                    bar_figure_div = dcc.Graph(figure=co2_bar.Figure(ingrdData))
                    co2_comp_div = co2_comparison.Text(totalco2)
                except ValueError:
                    True
    return totalco2_div, bar_figure_div, co2_comp_div


def parsingManualTable(rows):
    ingrd = []
    ingrd_q = []
    ingrd_u = []
    for r in rows:
        if r['ingrd'] != '':
            ingrd.append(r['ingrd'])
            if r['q'] != 0:
                ingrd_q.append(r['q'])
            else:
                ingrd_q.append(1)
            ingrd_u.append('g')
    ingrdSet = {'ingrd':ingrd,'ingrd_q':ingrd_q,'ingrd_u':ingrd_u}
    return ingrdSet

def parsingManualCO2(response_json):
     totalco2 = round(response_json['totalCO2']*1000,2)
     ingrdList = response_json['ingrdCO2List']
     ingrd = []
     co2 = []
     for i in ingrdList:
          ingrd.append(i['ingredient'])
          co2.append(round(i['co2']*1000,2))
     ingrdData = pd.DataFrame(data={'recipe': 'manual','ingredients':ingrd,'co2':co2})
     ingrdData = ingrdData.sort_values(by=['co2'], ascending = False)
     return totalco2, ingrdData