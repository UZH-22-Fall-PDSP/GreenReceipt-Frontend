#v6
from app import app
from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from components import co2_sum, co2_bar, co2_comparison
# Define the page layout
layout = dbc.Container([
    dbc.Row([
            html.Center(className='page-title', 
                        children=[html.H2("URL CO2 Calculator"),
                                  html.P("Calculate g of CO2 emissions of your recipe simply by entering food.com recipe url"),

                                  html.Hr()])]),       
    dbc.Row(className='page-contents', 
             children=[
                dbc.Row(className='url-calculator', children=[
                    html.H4("Please enter your recipe from food.com", style={'padding-left':'15%'}), 
                    dbc.Col([dbc.Input(id='url_recipe_input',
                                    placeholder='your Recipe URL from food.com',
                                    type='text', size="md"
                                    )],
                            className='url-input',width=7),
                    dbc.Col([dbc.Button('CALCULATION', id='url_recipe_cal', outline=True, color="secondary",n_clicks=0)],
                            className='url-button',width=1),
                    ]), 
                dbc.Row([ #result 
                         dbc.Row(className='co2-result-text', 
                                 children=[ dbc.Row(id='total-co2',children=[])]),                            
                         html.Div(id='co2_bar_fig', className='co2-bar', children=[])],
                         ),
                dbc.Row(id='co2-comparison',children=[],style={'padding-bottom':'10%'})
            ])
    ])
LOCAL_TEST_URL = 'http://127.0.0.1:5000'
GCP_BACKEND_URL = 'http://34.78.60.82:5000'

@app.callback(
     Output('total-co2','children'),
     Output('co2_bar_fig','children'),
     Output('co2-comparison','children'),
     Input('url_recipe_cal', 'n_clicks'),
     State('url_recipe_input', 'value')
)
def update_result(n_clicks, value):
    totalco2_div = []
    bar_figure_div = []
    co2_comp_div= []

    if n_clicks > 0:
        recipeName = checkValidURL(value)

        backendURL = GCP_BACKEND_URL + '/recipeCO2'
        response = requests.get(url = backendURL,  params={'recipe': recipeName})
        if (response.status_code != 204 and
            response.headers["content-type"].strip().startswith("application/json")):
            try:
                response_json = response.json()
                recipeName, totalco2, ingrdData = parsingRecipeCO2(response_json)

                totalco2_div = co2_sum.Text(recipeName,totalco2)
                bar_figure_div = dcc.Graph(figure=co2_bar.Figure(ingrdData))
                co2_comp_div = co2_comparison.Text(totalco2)

            except ValueError:
                True

    return totalco2_div, bar_figure_div, co2_comp_div


def checkValidURL(url):
     EXPECTED_RECIPE_PAGE = 'food.com/recipe/'
     if url != None:
          url.index(EXPECTED_RECIPE_PAGE) # Exception will be occurred if there is no EXPECTED_RECIPE_PAGE
          url = url.split('?')[0]
          url = url.split('/')[-1]
     else:
          url = ''
     return url

def parsingRecipeCO2(response_json):
     recipeName = response_json['recipeName']
     totalco2 = round(response_json['totalCO2']*1000,2)
     ingrdList = response_json['ingrdCO2List']
     ingrd = []
     co2 = []
     for i in ingrdList:
          ingrd.append(i['ingredient'])
          co2.append(round(i['co2']*1000,2))
     ingrdData = pd.DataFrame(data={'recipe': recipeName,'ingredients':ingrd,'co2':co2})
     ingrdData = ingrdData.sort_values(by=['co2'], ascending = False)
     return recipeName, totalco2, ingrdData
