from app import app
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
from components import banner
from pages import information

banner = banner.Banner()


# Define the page layout
layout = dbc.Container([
    dbc.Row(className="home-description",children=[
        dbc.Col([
            html.Div(
                     children=[
                                html.H4("A more sustainable food style with"), 
                                html.H1("Green Recipe"), 
                                html.P("Our CO2 calculator lets you quickly and easily figure out how sustainable your typical meals are and makes recommendations on how to improve "), 
                                html.Div(className="home-button",
                                         children=[dbc.Button("Learn more", id='learn-more', outline=True, color="secondary", n_clicks=0)])    
                ],style = {'margin': '10%'})            
        ]), 
        dbc.Col([
            html.Div(style={'width':'100%'})
        ],style = {'margin': '0%', 'padding': '0%'})
    ]),
    dbc.Row(id='page-information',children=[]),
    dbc.Row(banner)
],fluid=True)

@app.callback(Output('page-information', 'children'),
              Input('learn-more', 'n_clicks'))
def display_information(n):
    if n%2 == 0:
        return []
    else:
        return information.layout

