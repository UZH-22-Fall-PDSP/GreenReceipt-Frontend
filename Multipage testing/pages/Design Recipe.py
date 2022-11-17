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

## THIS IS FOR SINGLE PAGE TESTING
# app = dash.Dash(__name__, assets_folder="assets")

register_page(__name__)


## THIS IS FOR SINGLE PAGE TESTING
# app.layout = html.Div([  

layout= html.Div([      
                         ## [COMPONENET] URL RECIPE
                         html.Div([

                                   html.H1("🌿 GREEN RECIPE 🌿",style={"text-align": "center","marginTop":100,"marginBottom":20, "font-size":60}),

                                   ## [SUB-COMPONENT] URL RECIPE - INPUT
                                   ], style={"text-align": "center", "border-radius":20}),
                         
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

## For backend 
# @callback(Output('Output_Ingrd','children'),
#               Input('manual_ingrd_cal','n_clicks'),
#               State('ingredient1','value'),
#               State('ingredient2','value'),
#               State('ingredient3','value'),
#               State('ingredient4','value')
#              )

# @callback(Output('Output_quantity','children'),
#               Input('manual_ingrd_cal','n_clicks'),
#               State('ingrdient1','value'),
#               State('ingrdient2','value'),
#               State('ingrdient3','value'),
#               State('ingrdient4','value')
#              )

# @callback(Output('Output_unit','children'),
#               Input('manual_ingrd_cal','n_clicks'),
#               State('ingrdient1','value'),
#               State('ingrdient2','value'),
#               State('ingrdient3','value'),
#               State('ingrdient4','value')
#              )

# def update_output(clicks, ingredient1,ingredient2, ingredient3, ingredient4,):
#      if clicks is not None:
#             Ingrd = ingredient1 + ingredient2 + ingredient3 + ingredient4 
#             Ingrd_q = quantity1 + quantity2 + quantity3 + quantity4
#             Ingrd_u = unit1 + unit2 + unit3 + unit4 
#             print(Ingrd, Ingrd_q, Ingrd_u)


# LOCAL_TEST_URL = 'http://127.0.0.1:5000/recipeCO2'
# GCP_BACKEND_URL = 'XXX.XXX.XXX.XXX'

#Callback the CO2 emssion

def update_result(n_clicks, value):

     imgredientName = checkValidURL(value)

     backendURL = LOCAL_TEST_URL
     response = requests.get(url = backendURL,  params={'recipe': recipeName})

     ingrdco2 = ''


     if (response.status_code != 204 and
          response.headers["content-type"].strip().startswith("application/json")):
          try:
               response_json = response.json()
               recipeName, totalco2, ingrdList = parsingRecipeCO2(response_json)
               title = 'Total CO2 of "' + recipeName + '" is ' + str(totalco2) + ' / 1 serve'
               BDdata= pd.DataFrame(ingrdList).sort_values(by=['co2'], ascending=False)
               ingrd_details_fig = px.bar(BDdata, x='ingredient', y='co2',text_auto=True,
                                             title=title)
               ingrd_details_fig.update_layout(title_x=0.5)

          except ValueError:
               True

     return ingrd_details_fig


## IT IS FOR SINGLE PAGE TESTING
# if __name__ == '__main__':
#      app.run_server( host = '127.0.0.1',port = 8092, debug = True)