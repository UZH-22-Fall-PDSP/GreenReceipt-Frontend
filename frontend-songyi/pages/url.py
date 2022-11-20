# Import necessary libraries 
from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
import requests
import plotly.express as px
import pandas as pd

# TODO: Tasks pending completion -@hyeongkyunkim at 11/19/2022, 11:05:48 PM
# - Resize components
# - Result graph placeholder


# FOR SINGLE PAGE TESTING

# Define the page layout
layout = dbc.Container([
    dbc.Row([
        html.Center(className='page-title', 
                    children=[html.H2("URL CO2 Calculator"),
                              html.P("Calculate CO2 level of your recipe by entering food.com recipe url"),]),
        html.Hr(),
        html.Div(className='page-contents', children = [
            dbc.Row([
                html.H4("This is for user input"), 
                dcc.Input(id='url_recipe_input',
                                    placeholder='Input your Recipe URL from food.com',
                                    type='text',
                                    ),
                dbc.Button('CALCULATION', id='url_recipe_cal', outline=True, color="secondary" ),
                        html.Br(),html.Br(),html.Br(),html.Br()],
                style={'padding':'5%'}), 
            dbc.Row([
                html.H4("This is result."), 
                dcc.Graph(id='recipe_ingrd_detail_graph')],
                style={'padding':'5%'}

        )])
    ])
])


# html.Br()



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
               ingrd_details_fig = px.bar(BDdata, x='ingredient', y='co2',
                                        text_auto=True,
                                        title=title,
                                        width = 1000)
            #    ingrd_details_fig.update_layout(title_x=0.5,margin=dict(t=50, r=100, b=50, l=100))

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

def parsingRecipeCO2(response_json):# if __name__ == '__main__':
#    app.run(host = '127.0.0.1',port = 8089,debug = True)
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
      app.run(host = '127.0.0.1',port = 8089,debug = True)
