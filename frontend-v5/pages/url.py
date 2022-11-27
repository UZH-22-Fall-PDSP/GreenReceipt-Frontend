from app import app
from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from components import co2_bar

# Define the page layout
layout = dbc.Container([
    dbc.Row([
            html.Center(className='page-title', 
                        children=[html.H2("URL CO2 Calculator"),
                                  html.P("Calculate CO2 level per gram of your recipe by entering food.com recipe url"),
                                  html.Hr()])]),       
    dbc.Row(className='page-contents', 
             children=[
                dbc.Row(className='url-calculator', children=[
                    html.H4("Please enter your recipe from food.com"), 
                    dbc.Col([dbc.Input(id='url_recipe_input',
                                    placeholder='your Recipe URL from food.com',
                                    type='text', size="md"
                                    )],
                            className='url-input',width=8),
                    dbc.Col([dbc.Button('CALCULATION', id='url_recipe_cal', outline=True, color="secondary",n_clicks=0)],
                            className='url-button',width=1),
                    ], style={'padding':'3%'}), 
                dbc.Row([html.P("# Here is CO2 emission of your recipe."), 
                         dbc.Row(id='co2-result-text', 
                                 children=[dbc.Row(id='recipe-name',children=[]),
                                           dbc.Row(id='total-co2',children=[]),],
                                 style={'padding':'5%'}),                            
                         dbc.Row(id='co2_bar_fig',children=[])],
                         style={'padding':'3%'}
        )])
    ])

# recipeName, totalco2, ingrdData
#title = 'Total CO2 of "' + recipeName + '" is ' + str(totalco2)

LOCAL_TEST_URL = 'http://127.0.0.1:5000'
GCP_BACKEND_URL = 'http://34.78.60.82:5000'

@app.callback(
     Output('recipe-name','children'),
     Output('total-co2','children'),
     Output('co2_bar_fig','children'),
     Input('url_recipe_cal', 'n_clicks'),
     State('url_recipe_input', 'value')
)
def update_result(n_clicks, value):
    recipeName_div= []
    totalco2_div = []
    bar_figure_div = []

    if n_clicks > 0:
        recipeName = checkValidURL(value)

        backendURL = GCP_BACKEND_URL + '/recipeCO2'
        response = requests.get(url = backendURL,  params={'recipe': recipeName})
        if (response.status_code != 204 and
            response.headers["content-type"].strip().startswith("application/json")):
            try:
                response_json = response.json()
                recipeName, totalco2, ingrdList = parsingRecipeCO2(response_json)
                recipeName_div= html.H4(f"Total CO2 emission of {recipeName} is")
                totalco2_div = html.H2(f"{totalco2}")
                bar_figure_div = dcc.Graph(figure=co2_bar.Figure(ingrdList))

            except ValueError:
                True

    return recipeName_div, totalco2_div, bar_figure_div


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
