from app import app
import pandas as pd
import dash
from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
from components import similar_bar, similar_guage
import requests

### Add the page components here 

# Define the final page layout
layout = dbc.Container([
    dbc.Row(className='page-title', 
            children=[
                html.H2("Find alternative ingredient"),
                html.P("you can find more green ingredient which can reduce CO2 emission"),
                html.Hr()]),
    dbc.Row(className='page-contents',
            children=[
            dbc.Row([html.H4("Enter the ingredient you want to replace"), 
                     dbc.Col([dbc.Input(id='ingredient_input', placeholder='ingredient', type='text', size="md")],width=5),
                     dbc.Col([dbc.Button("Search", id='sim_cal', color="secondary",n_clicks=0)],width=2)],style={'padding':'3%'}),
            dbc.Row([ 
                     dbc.Col([html.P("Here is all alternative green ingredients"),
                             dbc.Row(id='sim_bar_fig',children=[])],style={'padding':'3%'}),
                     dbc.Col([html.P("You can reduce CO2 emission"),
                             dbc.Row([dbc.Col(id='guage_fig1',children=[], ),
                                      dbc.Col(id='guage_fig2',children=[])]),
                             dbc.Row([dbc.Col(id='guage_fig3',children=[]),
                                      dbc.Col(id='guage_fig4',children=[])])],style={'padding':'3%'}
            )
        ])
    ], style={'margin-right': '5%', 'margin-left': '5%'})
   ])

LOCAL_TEST_URL = 'http://127.0.0.1:5000'
GCP_BACKEND_URL = 'http://34.140.236.234:5000'

@app.callback(
     Output('sim_bar_fig','children'),
     Output('guage_fig1','children'),
     Output('guage_fig2','children'),
     Output('guage_fig3','children'),
     Output('guage_fig4','children'),
     Input('sim_cal', 'n_clicks'),
     State('ingredient_input', 'value')
)
def update_result(n_clicks, value):
    sim_bar_fig = []
    guage_fig1 = []
    guage_fig2 = []
    guage_fig3 = []
    guage_fig4 = []

    if n_clicks > 0: 

        backendURL = GCP_BACKEND_URL + '/simingrdset'

        if (value != None) and (value != ''):
            response = requests.get(url = backendURL,  params={'ingrd': value})
            print(response)
            if (response.status_code != 204 and
                response.headers["content-type"].strip().startswith("application/json")):
                try:
                    response_json = response.json()
                    ingrdList = parsingSimIngrdList(response_json)
                    org_input = (ingrdList['ingredient'][0], ingrdList['co2'][0])
                    print(org_input)
                    Data = pd.DataFrame(data=ingrdList)
                    Data = Data.drop([0]).sort_values(by=['co2'],ascending=False)
                    print(Data)
                    sim_bar_fig = dcc.Graph(figure=similar_bar.Figure(org_input,Data))
                    guage1, guage2, guage3, guage4 = similar_guage.Figure(org_input,Data)

                    guage_fig1 = dcc.Graph(figure=guage1)
                    guage_fig2 = dcc.Graph(figure=guage2)
                    guage_fig3 = dcc.Graph(figure=guage3)
                    guage_fig4 = dcc.Graph(figure=guage4)

                except ValueError:
                    True


        # org_input = ('olive oil', 4)
        # d = {'ingredient' : ['oils','olive','canola oil','sesame oil'],
        #      'co2':  [5.2, 3.9, 2.1, 1.05]}
        # Data = pd.DataFrame(data=d)

        # sim_bar_fig = dcc.Graph(figure=similar_bar.Figure(org_input,Data))
        # guage1, guage2, guage3, guage4 = similar_guage.Figure(org_input,Data)


        # guage_fig1 = dcc.Graph(figure=guage1)
        # guage_fig2 = dcc.Graph(figure=guage2)
        # guage_fig3 = dcc.Graph(figure=guage3)
        # guage_fig4 = dcc.Graph(figure=guage4)


    return sim_bar_fig, guage_fig1, guage_fig2, guage_fig3, guage_fig4



def parsingSimIngrdList(response_json):
     ingrd = []
     co2 = []
     for i in response_json:
          ingrd.append(i['ingredient'])
          co2.append(round(i['co2']*1000,2))
     ingrdData = {'ingredient':ingrd,'co2':co2}
     return ingrdData