from multiprocessing.sharedctypes import Value
import dash
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import dash, html, dcc, Input, Output, State, callback
from dash.dependencies import Input, Output
import requests
import json
#from dash_labs.plugins.pages import register_page
import plotly.graph_objects as go

LOCAL_TEST_URL = 'http://127.0.0.1:5000/recipeCO2'
GCP_BACKEND_URL = 'XXX.XXX.XXX.XXX'


#register_page(__name__)
app = dash.Dash(__name__, assets_folder="assets")

app.layout = html.Div([
#layout = html.Div([
         html.H1("🌿 GREEN RECIPE 🌿",style={"text-align": "center","marginTop":100,"marginBottom":20, "font-size":60}),
         html.H2('CO2 Emssion of ingredients',style={"text-align": "center"}),
         dcc.Graph('id=ingrd_cat_fig1',style={'display': 'inline-block'}) 
        ])


def update_result(n_clicks, value):

     backendURL = LOCAL_TEST_URL
     response = requests.get(url = backendURL,  params={'cat':catergory}) #adjust later 
     ingrd=[]
     co2=[]
     if (response.status_code != 204 and
          response.headers["content-type"].strip().startswith("application/json")):
          try:
               response_json = response.json()
               co2, ingrd = parsingCategoryCO2(response_json)
            #    title = 'Total CO2 of "' + recipeName + '" is ' + str(totalco2) + ' / 1 serve'
               ingrd_cat_fig1 = go.Figure(data=[go.Pie(labels=ingrd,values=co2, hole= 0.3)])
               ingrd_cat_fig1.update_layout(title_x=0.5)

          except ValueError:
               True

     return  ingrd_cat_fig1


def parsingCategoryCO2(response_json):
     co2List = response_json['co2']
     ingrdList = response_json['ingrdient']
     ingrd = []
     co2 = []
     for i in ingrdList:
          ingrd.append(i['ingredient'])
          co2.append(i['co2'])
     ingrdData = {'ingredient':ingrd,'co2':co2}
     return co2, ingrd


## THIS IS FOR SINGLE PAGE TESTING  
if __name__ == '__main__':
     app.run(host = '127.0.0.1',port = 8093,debug = True)