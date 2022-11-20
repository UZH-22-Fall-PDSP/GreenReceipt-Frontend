# Import necessary libraries 

import dash_bootstrap_components as dbc
import dash
from dash import html, dcc, callback, Input, Output, State, dash_table
import requests
import plotly.express as px
import pandas as pd
from collections import OrderedDict

# TODO: Tasks pending completion -@hyeongkyunkim at 11/19/2022, 11:08:53 PM
# - Resize components
# - Dropdown option in manual-recipe-table doesn't work
# - Result graph placeholder

df = pd.DataFrame(OrderedDict([
    ('ingrd', ["","","","",""]),
    ('q', [0.0,0.0,0.0,0.0,0.0]),
    ('u', ['kg', 'kg', 'kg', 'kg' , 'kg'])
]))



# Define the page layout
layout = dbc.Container([
    dbc.Row([
        html.Center(className='page-title', 
                    children=[html.H2("Manual CO2 Calculator"),
                              html.P("Calculate CO2 level of your recipe by entering ingredient and quantity manually"),]),
        html.Hr(),
        html.Div(className='page-contents', children = [
            dbc.Row([
                html.H4("This is for user input"),
                dash_table.DataTable(
                            id='manual-recipe-table',
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
                            style_cell={'textAlign': 'center'},
                            ),

                            dbc.Button('CALCULATE', id='manual_ingrd_calculate', outline=True, color="secondary" )
                ],
                style={'padding':'5%'}), 
            dbc.Row([
                html.H4("This is result."), 
                dcc.Graph(id='manual_ingrd_detail_graph')],
                style={'padding':'5%'}

        )])
    ])
])


# html.Br()



LOCAL_TEST_URL = 'http://127.0.0.1:5000'
GCP_BACKEND_URL = 'XXX.XXX.XXX.XXX'

@callback(
     Output('manual_ingrd_detail_graph','figure'),
     Input('manual_ingrd_calculate', 'n_clicks'),
     State('manual-recipe-table', 'data'))
def update_manualrecipe_result(n_clicks, rows):

    backendURL = LOCAL_TEST_URL + '/calculatorCO2'
    ingrd_details_fig = px.bar()
    ingrd_details_fig.update_yaxes(color='white')
    ingrd_details_fig.update_xaxes(color='white')
    ingrd_details_fig.update_layout(title_x=0.5, plot_bgcolor='white',title_font_color="white",
                                   font_color="white")

    ingrdSet = parsingManualTable(rows)
    if '' not in ingrdSet['ingrd']:
        response = requests.post(url = backendURL,  json = ingrdSet)
        if (response.status_code != 204 and
            response.headers["content-type"].strip().startswith("application/json")):
            try:
                response_json = response.json()
                totalco2, ingrdList = parsingManualCO2(response_json)
                title = 'Total CO2 is ' + str(totalco2)
                BDdata= pd.DataFrame(ingrdList).sort_values(by=['co2'], ascending=False)
                ingrd_details_fig = px.bar(BDdata, x='ingredient', y='co2',text_auto=True,
                                                title=title)
                ingrd_details_fig.update_layout(title_x=0.5, plot_bgcolor='white')
                ingrd_details_fig.update_xaxes(color='black')
                ingrd_details_fig.update_xaxes(color='balck')



            except ValueError:
                True

    return ingrd_details_fig

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
     totalco2 = response_json['totalCO2']
     ingrdList = response_json['ingrdCO2List']
     ingrd = []
     co2 = []
     for i in ingrdList:
          ingrd.append(i['ingredient'])
          co2.append(i['co2'])
     ingrdData = {'ingredient':ingrd,'co2':co2}
     return totalco2, ingrdData




