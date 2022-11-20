# Import necessary libraries 
import dash_bootstrap_components as dbc

import dash
from dash import html, dcc, callback, Input, Output, State
import requests
import plotly.express as px
import pandas as pd

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

def createCatIngrdDataFrame(cat_ingrd):
    df_final = pd.DataFrame(columns = ['dummy','category','ingredient','co2'])
    
    for i,c in enumerate(cat_ingrd):
        data = getCatIngrdList(c)
        c_data = []
        df_cat = pd.DataFrame(columns = ['category','ingredient','co2'])
        for ingrd in data:
            _ = {}
            _['category'] = c
            _['ingredient'] = ingrd['ingredient']
            _['co2'] = ingrd['co2']
            df_cat = df_cat.append(_,ignore_index=True)
        df_final = df_final.append(df_cat.sort_values('co2',ascending=False)[:10],ignore_index=True)
  
    return df_final

cat_ingrd = ['Vegetables','Fruits','Grains, Beans and Nuts','Meat and Poultry','Fish and Seafood','Dairy Foods']
color = ['#3cb371','#ffa500','#cd853f','#800000','#4169e1','#ffe4b5']
color_map = {cat:color for cat,color in zip(cat_ingrd,color)}

df_final = createCatIngrdDataFrame(cat_ingrd)

cat_total_fig = px.sunburst(df_final,
                            path=['category', 'ingredient'], values='co2', 
                            color='category',
                            color_discrete_map=color_map,
                            height = 800)

layout = dbc.Container([
    dbc.Row([
        html.Center(html.H1("Report")),
        html.Br(),
        html.Hr(),
        dbc.Col([
                html.H4("Which ingredient is greener?"), 
                dcc.Graph(id='cat_total_ingrd_graph', figure = cat_total_fig),
        ]), 
    ],style={'padding':'5%'})
])