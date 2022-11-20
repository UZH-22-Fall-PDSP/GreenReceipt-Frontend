# Import necessary libraries 
from dash import html
import dash_bootstrap_components as dbc
from components import banner

banner = banner.Banner()

# TODO: Tasks pending completion -@hyeongkyunkim at 11/19/2022, 11:04:38 PM
# - Link buttons to corresponding pages

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
                                         children=[dbc.Button("Learn more", outline=True, color="secondary")])    
                ],style = {'margin': '10%'})            
        ]), 
        dbc.Col([
            html.Div(style={'width':'100%'})
        ],style = {'margin': '0%', 'padding': '0%'})
    ]),
    dbc.Row(banner)


],fluid=True)