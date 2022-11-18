import dash
from dash import html, dcc, callback, Input, Output, State
import requests
import plotly.express as px
import pandas as pd

dash.register_page(__name__, path='/')

layout = html.Div([
                ## [COMPONENET]
                html.Div([
                        html.Br(),html.Br(),html.Br(),html.Br(),
                        html.H1("GREEN RECIPE",style={"text-align": "center","margin-bottom":"100px", "font-size":60,"font": "Black"}),

                        ## [SUB-COMPONENT] URL RECIPE - INPUT
                        dcc.Input(id='url_recipe_input',
                                    placeholder='Input your Recipe URL from food.com',
                                    type='text',
                                    style={"border-radius":5, "width":650, "padding" : 10,"font-size":20}),
                        html.Br(), html.Br(),html.Br(), html.Br(),

                        ## [SUB-COMPONENT] URL RECIPE - CALCULATION BUTTON
                        html.Button('CALCULATION', id='url_recipe_cal', n_clicks=0, style={"text-align": "center", "width":200, "height" : 50, "border-radius":10, "font-size":20, "background": "white"}),
                        html.Br(),html.Br(),html.Br(),html.Br(),
                        ], style={"text-align": "center", "border-radius":20,
                                    # backgroud picture
                                    "background-image": "url(assets/Background2.jpg)",
                                    # backgroud size and position
                                    "background-position-y":"top", "background-size": "cover",
                                    # margin for the district
                                    "margin-top":"-10px"}
                        ),
                
                html.Br(), html.Br(),

                ## [COMPONENET]
                html.Div([
                        html.H3("Your Recipe's CO2 Emissions", style={"text-align": "center", 'margin':20, "font-size":40}),
                        ## [SUB-COMPONENT] CO2 CALCULATION RESULT - INGREDIENTS DETAIL Bar graph
                        dcc.Graph(id='recipe_ingrd_detail_graph'),
                        html.Br()
                        ], style={"text-align": "center","font-size":30}),

                html.Br(), html.Br()
                ])


LOCAL_TEST_URL = 'http://127.0.0.1:5000'
GCP_BACKEND_URL = 'XXX.XXX.XXX.XXX'

@callback(
     Output('recipe_ingrd_detail_graph','figure'),
     Input('url_recipe_cal', 'n_clicks'),
     State('url_recipe_input', 'value'))
def update_recipeCO2_result(n_clicks, value):

     recipeName = checkValidURL(value)

     backendURL = LOCAL_TEST_URL + '/recipeCO2'
     response = requests.get(url = backendURL,  params={'recipe': recipeName})

     totalco2 = ''
     ingrd_details_fig = px.bar()

     if (response.status_code != 204 and
          response.headers["content-type"].strip().startswith("application/json")):
          try:
               response_json = response.json()
               recipeName, totalco2, ingrdList = parsingRecipeCO2(response_json)
               title = 'Total CO2 of "' + recipeName + '" is ' + str(totalco2)
               BDdata= pd.DataFrame(ingrdList).sort_values(by=['co2'], ascending=False)
               ingrd_details_fig = px.bar(BDdata, x='ingredient', y='co2',text_auto=True,
                                             title=title)
               ingrd_details_fig.update_layout(title_x=0.5)

          except ValueError:
               True

     return ingrd_details_fig

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
     totalco2 = response_json['totalCO2']
     ingrdList = response_json['ingrdCO2List']
     ingrd = []
     co2 = []
     for i in ingrdList:
          ingrd.append(i['ingredient'])
          co2.append(i['co2'])
     ingrdData = {'ingredient':ingrd,'co2':co2}
     return recipeName, totalco2, ingrdData
