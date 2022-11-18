import dash
from dash import html, dcc, callback, Input, Output, State
import requests
import plotly.express as px
import pandas as pd

dash.register_page(__name__)

LOCAL_TEST_URL = 'http://127.0.0.1:5000'
GCP_BACKEND_URL = 'XXX.XXX.XXX.XXX'

def getCatIngrdList(category):
    backendURL = LOCAL_TEST_URL + '/ingrdcat'
    response = requests.get(url = backendURL,  params={'cat': category})
    if (response.status_code != 204 and
        response.headers["content-type"].strip().startswith("application/json")):
        try:
            response_json = response.json()
        except ValueError:
            True
    return response_json

vegetables = {'name':'Vegetables','data':getCatIngrdList('Vegetables')}
cat_vege_fig = px.pie(pd.DataFrame(vegetables['data']).sort_values('co2',ascending=False)[:10], names='ingredient', values='co2', hole=.4)

fruits = {'name':'Fruits','data':getCatIngrdList('Fruits')}
cat_fruits_fig = px.pie(pd.DataFrame(fruits['data']).sort_values('co2',ascending=False)[:10], names='ingredient', values='co2', hole=.4)

grains = {'name':'Grains, Beans and Nuts','data':getCatIngrdList('Grains, Beans and Nuts')}
cat_grains_fig = px.pie(pd.DataFrame(grains['data']).sort_values('co2',ascending=False)[:10], names='ingredient', values='co2', hole=.4)

meat = {'name':'Meat and Poultry','data':getCatIngrdList('Meat and Poultry')}
cat_meat_fig = px.pie(pd.DataFrame(meat['data']).sort_values('co2',ascending=False)[:10], names='ingredient', values='co2', hole=.4)

fish = {'name':'Fish and Seafood','data':getCatIngrdList('Fish and Seafood')}
cat_fish_fig = px.pie(pd.DataFrame(fish['data']).sort_values('co2',ascending=False)[:10], names='ingredient', values='co2', hole=.4)

dairy = {'name':'Dairy Foods','data':getCatIngrdList('Dairy Foods')}
cat_dairy_fig = px.pie(pd.DataFrame(dairy['data']).sort_values('co2',ascending=False)[:10], names='ingredient', values='co2', hole=.4)

layout = html.Div([
                html.Div([
                        html.Br(),html.Br(),html.Br(),html.Br(),
                        html.H1("REPORT OF INGREDIENT CO2",style={"text-align": "center","margin-bottom":"100px", "font-size":60,"font": "Black"}),
                        html.Br(),html.Br(),html.Br(),html.Br(),
                        ], style={"text-align": "center", "border-radius":20,
                                    # backgroud picture
                                    "background-image": "url(assets/Background2.jpg)",
                                    # backgroud size and position
                                    "background-position-y":"top", "background-size": "cover",
                                    # margin for the district
                                    "margin-top":"-10px"}
                        ),                
                html.Div([
                        ## [SUB-COMPONENT] Category Ingredient result - Category Graphs
                        dcc.Graph(id='cat1_ingrd_graph', figure = cat_dairy_fig),
                        dcc.Graph(id='cat1_ingrd_graph', figure = cat_fish_fig),
                        dcc.Graph(id='cat1_ingrd_graph', figure = cat_meat_fig),
                        ],style={'display': 'flex', 'flex-direction': 'row'}),
                html.Br(), html.Br(),
                ])


