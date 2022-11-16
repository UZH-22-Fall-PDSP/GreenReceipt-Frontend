from multiprocessing.sharedctypes import Value
import dash
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import dash, html, dcc, Input, Output, State, callback
from dash.dependencies import Input, Output
import requests
import json
from dash_labs.plugins.pages import register_page

# app = dash.Dash(__name__, assets_folder="assets")
register_page(__name__)

# app.layout = html.Div([  
layout= html.Div([      
                         ## [COMPONENET] URL RECIPE
                         html.Div([

                                   html.H1("🌿 GREEN RECIPE 🌿",style={"text-align": "center","marginTop":100,"marginBottom":20, "font-size":60}),

                                   ## [SUB-COMPONENT] URL RECIPE - INPUT
                                   ], style={"text-align": "center", "border-radius":20}),

                         
                         html.Br(), html.Br(),


                         html.Br(), html.Br(),

                         ## [COMPONENET] MANUAL INGREDIENTS
                         html.Div([
                                   ## [SUB-COMPONENT] MANUAL INGREDIENTS - INPUT (5x3)
                                   html.Div([
                                        html.H2("Ingredients", style={"font-size":22,'margin-left':'20px','margin-right':'60px','display':'inline-block'}),
                                        html.H2("Quantity", style={"font-size":22,'margin-right':'30px','margin-right':'80px','display':'inline-block'}),
                                        html.H2("Unit", style={"font-size":22,'margin-right':'80px','display':'inline-block'}),
                                        html.Br(),
                                        dcc.Input(
                                             id='ingredient1',
                                             placeholder='Insert ingredient name',
                                             type='text',
                                             value='potato'),
                                        dcc.Input(
                                             id='quantity1',
                                             placeholder='Insert ingredient quantity',
                                             type='number',
                                             value='3'),
                                        dcc.Input(
                                             id='unit1',
                                             placeholder='Insert ingredient unit',
                                             type='text',
                                             value='grams'),

                                        html.Br(),
                                        dcc.Input(
                                             id='ingredient2',
                                             placeholder='Ingredient name',
                                             type='text'),
                                        dcc.Input(
                                             id='quantity2',
                                             placeholder='Quantity',
                                             type='number'),
                                        dcc.Input(
                                             id='unit2',
                                             placeholder='Unit',
                                             type='text'),

                                        html.Br(),
                                        dcc.Input(
                                             id='ingredient3',
                                             placeholder='Ingredient name',
                                             type='text'),
                                        dcc.Input(
                                             id='quantity3',
                                             placeholder='Quantity',
                                             type='number'),
                                        dcc.Input(
                                             id='unit3',
                                             placeholder='Unit',
                                             type='text'),

                                        html.Br(),
                                        dcc.Input(
                                             id='ingredient4',
                                             placeholder='Ingredient name',
                                             type='text'),
                                        dcc.Input(
                                             id='quantity4',
                                             placeholder='Quantity',
                                             type='number'),
                                        dcc.Input(
                                             id='unit4',
                                             placeholder='Unit',
                                             type='text'),
                                             ]),
                                   
                                   html.Br(), html.Br(),
                              
                                   ## [SUB-COMPONENT] MANUAL INGREDIENTS - CALCULATION BUTTON
                                   html.Button('CALCULATION', id='manual_ingrd_cal', n_clicks=0, style={"text-align": "center", "width":200, "height" : 50, "border-radius":10, "font-size":20, "background": "#DBE9D7"})
                                   ], style={"text-align": "center"}),
                                    ## [COMPONENET] CO2 CALCULATION RESULT
                         html.Div([
                                   ## [SUB-COMPONENT] CO2 CALCULATION RESULT - TOTAL OUTPUT
                                   html.H3("Your Recipe's CO2 Emissions", style={"text-align": "center", 'margin':20, "font-size":40}),
                                   ## [SUB-COMPONENT] CO2 CALCULATION RESULT - INGREDIENTS DETAIL OUTPUT
                                   dcc.Graph(id='ingrd_detail_graph'),
                                   html.Br()
                                   ], style={"text-align": "center","font-size":30}),


                         html.Br(), html.Br(),

                    ])
#callback



# if __name__ == '__main__':
#      app.run_server( host = '127.0.0.1',port = 8092, debug = True)