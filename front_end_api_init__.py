from multiprocessing.sharedctypes import Value
import dash
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import dash, html, dcc, Input, Output, State
from dash.dependencies import Input, Output
import requests
import json

#picture link from github 
tree = 'https://github.com/UZH-22-Fall-PDSP/GreenRecipe-Frontend/blob/main/assets/tree.png?raw=true'
#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#app = Dash(__name__, external_stylesheets=external_stylesheets)



app = dash.Dash(__name__, assets_folder="assets")

# dash.register_page("home",  path='/', layout=html.Div('Home Page'))
# dash.register_page("calculate", layout=html.Div('Calculate'))
# dash.register_page("result", layout=html.Div('Result'))

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

                         html.Br(), html.Br(),

                         html.Img(src=tree)
                    ])



LOCAL_TEST_URL = 'http://127.0.0.1:5000/recipeCO2'
GCP_BACKEND_URL = 'XXX.XXX.XXX.XXX'

@app.callback(
     Output('ingrd_detail_graph','figure'),
     Input('url_recipe_cal', 'n_clicks'),
     State('url_recipe_input', 'value')
)
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


if __name__ == '__main__':
     app.run_server( host = '127.0.0.1',port = 8087, debug = True)


