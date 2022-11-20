# Import necessary libraries 
import dash
from dash import html, dcc, callback, Input, Output, State, dash_table
import dash_bootstrap_components as dbc
import requests
import plotly.express as px
import pandas as pd

# TODO: Tasks pending completion -@hyeongkyunkim at 11/19/2022, 11:10:06 PM
# - Resize components
# - Choose the result visualization type: table? bar graph?

### Add the page components here 
table_header = [
    html.Thead(html.Tr([html.Th("ingredient"), html.Th("CO2 level")]))
]

row1 = html.Tr([html.Td("tofu"), html.Td("0.7")])
row2 = html.Tr([html.Td("chicken"), html.Td("1.2")])
row3 = html.Tr([html.Td("beef"), html.Td("1.4")])
row4 = html.Tr([html.Td("pork"), html.Td("1.9")])

table_body = [html.Tbody([row1, row2, row3, row4])]

page2_table = dbc.Table(table_header + table_body, bordered=True)

# Define the final page layout
layout = dbc.Container([
    dbc.Row([
        html.Center(html.H2("Find alternative ingredient")),
        html.Br(),
        html.Hr(),
        dbc.Col([
                dcc.Input(id='ingrd_input',
                        placeholder='Input your ingredient',
                        type='text',
                        ),
                dbc.Button("Search", id="ingrd_sim_search", color="secondary")
        ]), 
        dbc.Col([
            html.P("Here is alternative green ingredients"), 
            dcc.Graph(id='ingrd_sim_graph')                     

        ])
    ],style={'padding':'10%'})
])



LOCAL_TEST_URL = 'http://127.0.0.1:5000'
GCP_BACKEND_URL = 'XXX.XXX.XXX.XXX'

@callback(
     Output('ingrd_sim_graph','figure'),
     Input('ingrd_sim_search', 'n_clicks'),
     State('ingrd_input', 'value'))
def update_simingrdset_result(n_clicks, value):

    backendURL = LOCAL_TEST_URL + '/simingrdset'

    ingrd_details_fig = px.pie()
    if (value != None) and (value != ''):
        response = requests.get(url = backendURL,  params={'ingrd': value})

        if (response.status_code != 204 and
            response.headers["content-type"].strip().startswith("application/json")):
            try:
                response_json = response.json()
                ingrdList = parsingSimIngrdList(response_json)
                BDdata= pd.DataFrame(ingrdList).sort_values(by=['co2'], ascending=False)
                ingrd_details_fig = px.pie(BDdata, names='ingredient', values='co2', hole=.4)

            except ValueError:
                True

    return ingrd_details_fig

def parsingSimIngrdList(response_json):
     ingrd = []
     co2 = []
     for i in response_json:
          ingrd.append(i['ingredient'])
          co2.append(i['co2'])
     ingrdData = {'ingredient':ingrd,'co2':co2}
     return ingrdData