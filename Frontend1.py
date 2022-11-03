# %%
pip install requests 

# %%
pip install numpy

# %%
pip install pandas

# %%
import dash
from dash import dash, html, dcc
from dash.dependencies import Input, Output
import requests

app = dash.Dash()


app.layout = html.Div([
    html.H1("Enter your recipe here:"),
    dcc.Input(
        id='recipelink',
        placeholder='Insert website value',
        type='text',
    ),
    html.Br(),
    html.Br(),
    html.H2("Enter the ingredients of your recipe here:"),
    dcc.Input(
        id='ingredientname',
        placeholder='Insert ingredient name',
        type='text',
        value='potato',
    ),
    dcc.Input(
        id='quantity',
        placeholder='Insert ingredient quantity',
        type='int',
        value='2',
    ),
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
     app.run_server(debug=False, port=8057)

# %%



