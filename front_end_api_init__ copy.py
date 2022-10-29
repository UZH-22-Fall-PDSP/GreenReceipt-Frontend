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



app.layout = html.Div([
    html.H1("Enter your recipe",style={"text-align": "center","marginTop":250,"font-size":60}),

    html.Div([
          dcc.Input(
          id='recipelink',
          placeholder='Links from food.com',
          type='url',
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
        html.Button('calculate', id='calculate-button', style={"text-align": "center", "width":350, "height" : 70, "border-radius":20, "font-size":35, "background": "#DBE9D7"})], 
         
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
    [Input('input-num1', 'value'),
     Input('input-num2', 'value')]
)

def update_result(num1, num2):
    sum_arguments = {'x': num1, 'y': num2}
    url ='http://35.233.118.56:5000/get_sum'
    response = requests.get(url = url,  params=sum_arguments)
    print(response.url)
    print(response.json())
    return "The sum is: {}".format(response.json())

if __name__ == '__main__':
     app.run_server( host = '127.0.0.1',port = 8087, debug = True)


