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
import plotly.graph_objects as go

LOCAL_TEST_URL = 'http://127.0.0.1:5000/recipeCO2'
GCP_BACKEND_URL = 'XXX.XXX.XXX.XXX'


df = [{'ingredient': 'baking powder', 'co2': 1.504}, {'ingredient': 'bbq sauce', 'co2': 0.983}, {'ingredient': 'gelatin', 'co2': 0.652}, 
{'ingredient': 'mayonnaise', 'co2': 1.914}, {'ingredient': 'mustard', 'co2': 1.108}, {'ingredient': 'nutmeg', 'co2': 0.367},
{'ingredient': 'soy sauce', 'co2': 1.344}, {'ingredient': 'tabasco sauce', 'co2': 4.274}, {'ingredient': 'vanilla extract', 'co2': 13.827},
{'ingredient': 'yeast extract', 'co2': 2.194}, {'ingredient': 'yeast', 'co2': 0.754}, {'ingredient': 'half-fat margarine', 'co2': 1.15}, 
{'ingredient': 'vegan spreadable fat', 'co2': 1.67}, {'ingredient': 'full-fat margarine', 'co2': 1.78}, {'ingredient': 'mixed salad', 'co2': 0.28},
{'ingredient': 'crispbread', 'co2': 0.53}, {'ingredient': 'lasagna noodles', 'co2': 0.46}, {'ingredient': 'bread baguette', 'co2': 0.61}, 
{'ingredient': 'wheat bread', 'co2': 0.61}, {'ingredient': 'cream cheese', 'co2': 5.65}, {'ingredient': 'philadelphia cream cheese', 'co2': 5.65},
{'ingredient': 'ricotta', 'co2': 5.65}, {'ingredient': 'low-fat curd cheese', 'co2': 2.52}, {'ingredient': 'mozzarella', 'co2': 4.34}, 
{'ingredient': 'curd cheese', 'co2': 3.4}, {'ingredient': 'whipping cream', 'co2': 4.31}, {'ingredient': 'icing sugar', 'co2': 0.49}, 
{'ingredient': 'coconut milk', 'co2': 0.54}, {'ingredient': 'peanut butter', 'co2': 2.0}, {'ingredient': 'pastry', 'co2': 1.6}, 
{'ingredient': 'puff pastry', 'co2': 1.6}, {'ingredient': 'coffee powder', 'co2': 5.6}, {'ingredient': 'cocoa powder', 'co2': 5.0}, 
{'ingredient': 'cheese emmentaler', 'co2': 6.0}, {'ingredient': 'parmesan', 'co2': 6.3}, {'ingredient': 'dark chocolate', 'co2': 4.1}, 
{'ingredient': 'milk chocolade', 'co2': 4.1}, {'ingredient': 'white chocolate', 'co2': 4.1}, {'ingredient': 'ham', 'co2': 3.23}, 
{'ingredient': 'cheddar cheese', 'co2': 15.1549862}, {'ingredient': 'butter', 'co2': 8.49}, {'ingredient': 'buttermilk', 'co2': 3.73}, 
{'ingredient': 'cheese', 'co2': 14.9}, {'ingredient': 'coffee', 'co2': 7.75}, {'ingredient': 'cottonseed oil', 'co2': 1.82}, 
{'ingredient': 'full cream milk', 'co2': 1.98}, {'ingredient': 'milk', 'co2': 1.98}, {'ingredient': 'cream', 'co2': 2.99}, 
{'ingredient': 'sour cream', 'co2': 2.99}, {'ingredient': 'sanddab', 'co2': 0.55}, {'ingredient': 'whiting', 'co2': 0.55}, 
{'ingredient': 'bream', 'co2': 2.93}, {'ingredient': 'mackerel', 'co2': 2.93}, {'ingredient': 'pompano', 'co2': 2.93}, 
{'ingredient': 'horseradish', 'co2': 7.88}, {'ingredient': 'white radish', 'co2': 7.88}, {'ingredient': 'skimmed milk', 'co2': 1.25}, 
{'ingredient': 'granulated sugar', 'co2': 0.568}, {'ingredient': 'sugar', 'co2': 0.568}, {'ingredient': 'vanilla', 'co2': 13.4}, 
{'ingredient': 'whey', 'co2': 0.161}, {'ingredient': 'yogurt', 'co2': 2.2}]


register_page(__name__)
# app = dash.Dash(__name__, assets_folder="assets")

# app.layout = html.Div([
layout = html.Div([
         
          ## [COMPONENET] Title
               html.Div([

                    html.Br(),html.Br(),html.Br(),html.Br(),
                    html.H1("REPORT OF INGREDIENT CO2",style={"text-align": "center","margin-bottom":"100px", "font-size":60,"font-family":"sans-serif","color":"White"}),
                    html.Br(),html.Br(),html.Br(),
                    ],
                    
                    style={"text-align": "center",
                    # backgroud picture
                     "background-image": "url(assets/Background4.jpg)","opacity": "0.9",
                    # backgroud size and position
                    "background-position-y":"center", "background-size": "cover",
                    # margin for the district
                    "margin-top":"-10px"
                    }
                    
               ),
         
         ##[COMPONENET] Fixed insight graph
          html.Div([
               dcc.Graph('id=ingrd_cat_fig1',style={'display': 'inline-block'}) 
               ],
               #style for the graph
               style={
                    "text-align": "center","font-size":30,"width":"90%","margin":"0 auto"

               }
          ),

          ## [COMPONENET] Simple comment
          html.Div([
               html.Br(),html.Br(),
               html.H5("Description of something", style={"text-align": "center", "font-size":30,}),
               html.H5("whole dataset table", style={"text-align": "center", "font-size":30}),
               html.Br(),html.Br(),
               ],
               style={"background-color":"lightgrey","width":"70%",
               "margin":"0 auto","border-radius":10}
                                  ),
                         
          html.Br(), html.Br(), html.Br(), html.Br()
          
     ],
         

     #style for the whole page
     style={

      # scrollbar
      "scrollbar-gutter": "stable",
      # size of the whole page
      "margin-top":"-10px","margin-left":"-1%","margin-right":"-1%"
     }
  
 )
 


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
# if __name__ == '__main__':
#      app.run(host = '127.0.0.1',port = 8093,debug = True)