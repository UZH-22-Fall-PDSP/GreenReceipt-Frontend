import dash
import pandas as pd
import plotly.express as px
from dash import dash, html, dcc, Input, Output, State
from dash.dependencies import Input, Output
import requests


#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#app = Dash(__name__, external_stylesheets=external_stylesheets)



app = dash.Dash()


app.layout = html.Div([
    html.H1("Enter your recipe here:"),

    html.Div(dcc.Input(
        id='recipelink',
        placeholder='Links from food.com',
        type='url')),

    html.Button('import', id='import-button'),
    html.Div(id='container-button-basic',
             children='Enter a value and press submit'),

    html.Br(),
    html.Br(),

    html.H2("Enter the ingredients of your recipe here:"),

    html.Div( html.H5(["Infredient    ","Quantity    ","Unit    ","Status    "])),

    html.Div([
        dcc.Input(
            id='ingredient',
            placeholder='Insert ingredient name',
            type='text',
            value='potato'),
        dcc.Input(
            id='quantity',
            placeholder='Insert ingredient quantity',
            type='int',
            value='3'),
        dcc.Input(
            id='unit',
            placeholder='Insert ingredient unit',
            type='text',
            value='grams'),
        dcc.Input(
            id='status',
            placeholder='Insert ingredient status',
            type='text',
            value='frozen'),]),

    html.Button('calculate', id='calculate-button'),

    html.Br(),
    html.Br(),
    html.H3("CO2 emssion of your recipe:"),
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
     app.run_server(host - '127.0.0.1', debug=True, port=8077)


#if __name__ == '__main__':
 #    app.run_server(host = '0.0.0.0', port = 8050, debug = True)
