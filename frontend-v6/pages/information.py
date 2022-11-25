# Import necessary libraries 
import dash
from dash import html
import dash_bootstrap_components as dbc

information_image1 = 'static/assets/information-image1.jpg'
information_image2 = 'static/assets/information-image2.jpg'


layout = dbc.Container([
    dbc.Row([
        #html.Center(html.H1("Information")),
        #html.Center(html.P("Finding more information about Green Recipe")),
        #html.Br(),
        html.Hr(),
        dbc.Col(
            html.Img(src='static/assets/information-image1.jpg', style={"height":"100%","width":"100%"})
        ,style={'padding':'5%'}
        ), 
        dbc.Col([
            html.Br(),
            html.H4("Why you should choose low carbon emssion recipe?"), 
            html.Br(),
            html.P("The current worldwide food production accounts for more than a quarter of total greenhouse gas emissions, which in turn is the leading cause of climate change."),
            html.P("Your food decisions can play a fundamental role in reducing the carbon footprint by for example aligning with a more sustainable food diet and choosing more environmentally friendly food ingredients."),
        ],style={'padding':'5%'},align="center",),  
    ],
    style={'padding':'0%'}),
    dbc.Row(html.Hr()),
    dbc.Row([
        dbc.Col([
            html.H4("Why you should choose Green Recipe?"), 
            html.Br(),
            html.P("Green Recipes has a very large database of ingredients, to measure the CO2 emissions from your favourite recipes or foods. "),
            html.P("By using Green recipe to find substitute ingredients, you will generate fewer emissins. You can search the ingredient you like on Green Recipe, then you can get the carbon footprint of alternative ingredients.")
        ],style={'padding':'5%'}, align="center",), 
        dbc.Col([
            html.Img(src='static/assets/information-image2.jpg', style={"height":"100%","width":"100%"})
        ],style={'padding':'5%'}),
        html.Hr()
    ],
    style={'padding':'0%'}),
])