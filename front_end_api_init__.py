from multiprocessing.sharedctypes import Value
import dash
import pandas as pd
import plotly.express as px
from dash import dash, html, dcc, Input, Output, State
from dash.dependencies import Input, Output
import requests


#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#app = Dash(__name__, external_stylesheets=external_stylesheets)



app = dash.Dash(__name__, assets_folder="assets")

# dash.register_page("home",  path='/', layout=html.Div('Home Page'))
# dash.register_page("calculate", layout=html.Div('Calculate'))
# dash.register_page("result", layout=html.Div('Result'))


LINK_INPUT_PLACEHOLDE = 'Links from food.com'
app.layout = html.Div([
    html.H1("Enter your recipe",style={"text-align": "center","marginTop":250,"font-size":60}),
    
    html.Div([
          dcc.Input(
          id='recipelink',
          placeholder=LINK_INPUT_PLACEHOLDE,
          type='text',
          style={"border-radius":5, "width":750,"padding" : 16,"font-size":12}),
     
          html.Button('import', id='import-button', style={"text-align": "center", "width":60})],
        
          style={"text-align": "center"}),

   
    html.Br(),
    html.Br(),

    html.Div([
        
        html.Div([
          dcc.Markdown("Ingredient   Quantity     Unit      Status", style={"font-size":25}),
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
          dcc.Input(
               id='status1',
               placeholder='Insert ingredient status',
               type='text',
               value='frozen'),

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
          dcc.Input(
               id='status2',
               placeholder='Status',
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
          dcc.Input(
               id='status3',
               placeholder='Status',
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
          dcc.Input(
               id='status4',
               placeholder='Status',
               type='text'),
               ]),

        html.Br(),
        html.Br(),
        html.Button('calculate', id='calculate-button', n_clicks=0, style={"text-align": "center", "width":350, "height" : 70, "border-radius":20, "font-size":35, "background": "#DBE9D7"})], 
         
         style={"text-align": "center"}),

    

    

    html.Br(),
    html.Br(),
    html.H3("CO2 emssion of your recipe:", style={"text-align": "center"}),
    html.Br(),
    html.Br(),
    html.Div(id='result')
    ])


@app.callback(
    Output('result', 'children'),
    Input('import-button', 'n_clicks'),
    State('recipelink', 'value')
)
def update_result(n_clicks, value):
     LOCAL_TEST_URL = 'http://127.0.0.1:5000/recipeCO2'
     GCP_BACKEND_URL = 'XXX.XXX.XXX.XXX'

     recipeName = checkValidURL(value)

     backendURL = LOCAL_TEST_URL
     response = requests.get(url = backendURL,  params={'recipe': recipeName})
     output = ''
     if (response.status_code != 204 and
          response.headers["content-type"].strip().startswith("application/json")):
          try:
               response_json = response.json()
               output = "The recipe link you entered is not from Food.com"
               if True:
                         output = " {recipe} {totalco2} / serves".format(recipe = response_json['recipeName'], totalco2=response_json['totalCO2'])
          except ValueError:
               True
     return output

def checkValidURL(url):
     EXPECTED_RECIPE_PAGE = 'food.com/recipe/'
     if url != None:
          url.index(EXPECTED_RECIPE_PAGE) # Exception will be occurred if there is no EXPECTED_RECIPE_PAGE
          url = url.split('?')[0]
          url = url.split('/')[-1]
     else:
          url = ''
     return url

if __name__ == '__main__':
     app.run_server( host = '127.0.0.1',port = 8087, debug = True)


