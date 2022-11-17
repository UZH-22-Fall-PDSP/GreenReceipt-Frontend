from multiprocessing.sharedctypes import Value
import dash
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import dash, html, dcc, Input, Output, State
from dash.dependencies import Input, Output
import requests
import json
# from dash_labs.plugins.pages import register_page

# register_page(__name__)
app = dash.Dash(__name__, assets_folder="assets")

# layout = html.Div([  
app.layout = html.Div([  
                         ## [COMPONENET] URL RECIPE
                         html.Div([

                                   html.H1("🌿 GREEN RECIPE 🌿",style={"text-align": "center","marginTop":100,"marginBottom":20, "font-size":60}),

                                   ## [SUB-COMPONENT] URL RECIPE - INPUT
                                   dcc.Input(id='url_recipe_input',
                                             placeholder='Input your Recipe URL from food.com',
                                             type='text',
                                             style={"border-radius":5, "width":650, "padding" : 10,"font-size":20}),

                                   html.Br(), html.Br(),

                                   ## [SUB-COMPONENT] URL RECIPE - CALCULATION BUTTON
                                   html.Button('CALCULATION', id='url_recipe_cal', n_clicks=0, style={"text-align": "center", "width":200, "height" : 50, "border-radius":10, "font-size":20, "background": "#DBE9D7"})
                                   ], style={"text-align": "center", "border-radius":20}),

                         
                         html.Br(), html.Br(),

                         ## [COMPONENET] CO2 CALCULATION RESULT
                         html.Div([
                                   ## [SUB-COMPONENT] CO2 CALCULATION RESULT - TOTAL OUTPUT
                                   html.H3("Your Recipe's CO2 Emissions", style={"text-align": "center", 'margin':20, "font-size":40}),
                                   ## [SUB-COMPONENT] CO2 CALCULATION RESULT - INGREDIENTS DETAIL OUTPUT
                                   dcc.Graph(id='ingrd_detail_graph'),
                                   html.Br()
                                   ], style={"text-align": "center","font-size":30}),

                         html.Br(), html.Br()
                        ],
     
    # style for the whole page
    style={

    # backgroud picture
    "background-image": "url(assets/background2.png)",
    # backgroud size and position
    "background-position-y":"top", "background-size": "cover",

    # scrollbar
    "scrollbar-gutter": "stable",
    # size of the whole page
    "margin-top":"-10px","margin-left":"-1%","margin-right":"-1%"
    })


LOCAL_TEST_URL = 'http://127.0.0.1:5000/recipeCO2'
GCP_BACKEND_URL = 'XXX.XXX.XXX.XXX'

# @callback(
#      Output('ingrd_detail_graph','figure'),
#      Input('url_recipe_cal', 'n_clicks'),
#      State('url_recipe_input', 'value'))


def update_result(n_clicks, value):

     recipeName = checkValidURL(value)

     backendURL = LOCAL_TEST_URL
     response = requests.get(url = backendURL,  params={'recipe': recipeName})

     totalco2 = ''
     ingrd_details_fig = px.bar()

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


## THIS IS FOR SINGLE PAGE TESTING
if __name__ == '__main__':
      app.run_server( host = '127.0.0.1',port = 8087, debug = True)