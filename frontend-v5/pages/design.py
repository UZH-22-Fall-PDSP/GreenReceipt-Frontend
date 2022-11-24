
from app import app
from dash import html, dcc, callback, Input, Output, State, dash_table
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go

import pandas as pd
import requests
from collections import OrderedDict


from components import manual_input, co2_bar

d = {'recipe' : "manual",
     'ingredients' : ['bacon','avocado','salt','wheat bread','lemmon juice','mayonnaise'],
     'co2':  [5.2, 3, 2, 7,1.5,2.2] }

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
                                {'id': 'q', 'name': 'Quantity', "type": "numeric"},
                                {'id': 'u', 'name': 'Unit', 'presentation': 'dropdown'},
                            ],
                            editable=True,
                            dropdown={
                                'u': {'options': [{'label': i, 'value': i} for i in ['g','kg']], 'clearable' : False}
                            },
                        )

################################################################

# Define the page layout
layout = dbc.Container([
    dbc.Row([
        html.Center(className='page-title', 
                    children=[html.H2("Manual CO2 Calculator"),
                              html.P("Calculate CO2 level per gram of your recipe by entering ingredient and quantity manually"),
                              html.Hr()]),
        
    dbc.Row(className='page-contents', 
            children = [
            dbc.Row([
                dbc.Row(html.H4("Please fill in the table and press the calculate button !")), 
                dbc.Col(manual_input, style={'padding-top':'3%', 'padding-bottom':'3%'},width=6),
                html.Div(dbc.Button('CALCULATION', id='manual_recipe_cal', color="secondary",size="rg",n_clicks=0)),        
                ],style={'padding':'5%'}), 
            dbc.Row([
                html.P("# Here is CO2 emission of your recipe."), 
                dbc.Row(className='co2-result-text', 
                        children=[dbc.Row(id='manual-total-co2',children=[]),], style={'padding':'5%'}),                            
                dbc.Row(id='manual-co2-bar-fig',children=[])],
                style={'padding':'3%'}
        )])
    ])
])

LOCAL_TEST_URL = 'http://127.0.0.1:5000'
GCP_BACKEND_URL = 'http://34.140.236.234:5000'


@callback(
    Output('manual-total-co2','children'),
    Output('manual-co2-bar-fig','children'),
    Input('manual_recipe_cal', 'n_clicks'),
    State('manual-recipe-table', 'data'))
def update_manualrecipe_result(n_clicks, rows):
    totalco2_div = []
    bar_figure_div = []

    ##
    #ingrdSet = parsingManualTable(rows)
    ###
    #totalco2, ingrdList = parsingManualCO2(response_json)
    if n_clicks > 0:
        backendURL = GCP_BACKEND_URL + '/calculatorCO2'

        ingrdSet = parsingManualTable(rows)
        if '' not in ingrdSet['ingrd']:
            response = requests.post(url = backendURL,  json = ingrdSet)
            if (response.status_code != 204 and
                response.headers["content-type"].strip().startswith("application/json")):
                try:
                    response_json = response.json()
                    totalco2, ingrdList = parsingManualCO2(response_json)
                    totalco2_div = html.H2(f"{totalco2}")
                    bar_figure_div = dcc.Graph(figure=co2_bar.Figure(ingrdList))
                except ValueError:
                    True


    # if n_clicks > 0: 
    #     recipeName= "manual"
    #     totalco2 = 15.0
    #     ingData = pd.DataFrame(data=d)

    #     recipeName_div= html.H4(f"Total co2 emission of {recipeName} is")
    #     totalco2_div = html.H2(f"{totalco2}")
    #     bar_figure_div = dcc.Graph(figure=co2_bar.Figure(ingData))



    return totalco2_div, bar_figure_div


def parsingManualTable(rows):
    ingrd = []
    ingrd_q = []
    ingrd_u = []
    for r in rows:
        ingrd.append(r['ingrd'])
        ingrd_q.append(r['q'])
        ingrd_u.append(r['u'])
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