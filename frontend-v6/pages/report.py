# Import necessary libraries 
import dash
from dash import html
import dash_bootstrap_components as dbc
import requests
import plotly.express as px
import pandas as pd
from dash import html, dcc
import plotly 
import plotly.express as px
import plotly.figure_factory as ff
import numpy as np
import pandas as pd
import plotly.graph_objects as go

LOCAL_TEST_URL = 'http://127.0.0.1:5000'
GCP_BACKEND_URL = 'http://34.78.60.82:5000'

def getCatIngrdList(category):
    backendURL = GCP_BACKEND_URL + '/ingrdcat'
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
            _['category'] = [c]
            _['ingredient'] = [ingrd['ingredient']]
            _['co2'] = [ingrd['co2']]
            df_cat = pd.concat([df_cat,pd.DataFrame(_)])
        df_final = pd.concat([df_final,df_cat.sort_values('co2',ascending=False)[:10]])
    return df_final

cat_ingrd = ['Vegetables','Fruits','Grains, Beans and Nuts','Meat and Poultry','Fish and Seafood','Dairy Foods']
color = ['A5ADF3','E2A69E','A1DAC7','C3A9F3','ECC9AE','A4DEF2']
color_map = {cat:color for cat,color in zip(cat_ingrd,color)}

df_final = createCatIngrdDataFrame(cat_ingrd)

cat_total_fig = px.sunburst(df_final,
                            path=['category', 'ingredient'], values='co2', 
                            color='category',
                            color_discrete_map=color_map)


cat_each_dist = go.Figure()

for cate in cat_ingrd:
    cat_each_dist.add_trace(go.Violin(x=df_final['category'][df_final['category'] == cate],
                            y=df_final['co2'][df_final['category'] == cate],
                            name=cate,
                            box_visible=True,
                            meanline_visible=True))


layout = dbc.Container([
    dbc.Row([
        html.Center(html.H1("Report")),
        html.Br(),
        html.Hr(),
        dbc.Col([
            html.H4("Which ingredient category is the most greener? "), 
            html.P("Check the report of ingredient CO2 charts by each category."),
            dcc.Graph(id='cat_total_ingrd_graph', figure = cat_total_fig),
        ],style={'padding':'0%'}), 
        dbc.Col([
            html.H4("How are ingredients CO2 level distributed?"), 
            html.P("Check the report of ingredient CO2 distribution by each category."),
            dcc.Graph(id='cat_each_dist_graph', figure = cat_each_dist),
        ],style={'padding':'0%'}),
    ],style={'padding':'5%'})
])