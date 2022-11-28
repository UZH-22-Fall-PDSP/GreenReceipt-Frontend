#v6
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
     dbc.Row([
            html.Center(className='page-title', 
                        children=[
                            html.H2("Find alternative ingredient"),
                            html.P("you can find more green ingredient which can reduce CO2 emission"),
                            html.Hr()])
            ]),
    dbc.Row(className='page-contents',
            children=[
            dbc.Row(className='ingredient_input', 
                    children=[html.H4("Enter the ingredient you want to replace"), 
                              html.Div([dbc.Col([dbc.Input(id='ingredient_input', placeholder='ingredient', type='text', size="md")],width=5),
                                        dbc.Col([dbc.Button("Search", id='sim_cal', color="secondary",n_clicks=0)],width=2)])
                              ]),
            dbc.Row([ #result
                     dbc.Row(id='orig-text', className='sim-result-text',children=[]) ,
                     dbc.Col([dbc.Row(id="sim_text", children=[],style={'padding-bottom':'3%'}),
                             dbc.Row(id='sim_bar_fig',children=[])],style={'padding':'5%'}),
                     dbc.Col([dbc.Row(id="guage_text", children=[],style={'padding-bottom':'3%'}),
                             dbc.Row([dbc.Col(id='guage_fig1',children=[], ),
                                      dbc.Col(id='guage_fig2',children=[])]),
                             dbc.Row([dbc.Col(id='guage_fig3',children=[]),
                                      dbc.Col(id='guage_fig4',children=[])])],style={'padding':'5%'}
            )
        ])
    ], style={'margin-right': '5%', 'margin-left': '5%', 'margin-bottom':'10%'})
   ])

LOCAL_TEST_URL = 'http://127.0.0.1:5000'
GCP_BACKEND_URL = 'http://34.78.60.82:5000'

@app.callback(
     Output('orig-text','children'),
     Output('sim_text','children'),
     Output('sim_bar_fig','children'),
     Output('guage_text','children'),
     Output('guage_fig1','children'),
     Output('guage_fig2','children'),
     Output('guage_fig3','children'),
     Output('guage_fig4','children'),
     Input('sim_cal', 'n_clicks'),
     State('ingredient_input', 'value')
)
def update_result(n_clicks, value):
    orig_text = []
    sim_text = []
    sim_bar_fig = []
    guage_text = []
    guage_fig1 = []
    guage_fig2 = []
    guage_fig3 = []
    guage_fig4 = []

    if n_clicks > 0: 

        backendURL = GCP_BACKEND_URL + '/simingrdset'

        if (value != None) and (value != ''):
            response = requests.get(url = backendURL,  params={'ingrd': value})
            if (response.status_code != 204 and
                response.headers["content-type"].strip().startswith("application/json")):
                try:
                    response_json = response.json()
                    ingrdList = parsingSimIngrdList(response_json)
                    org_input = (ingrdList['ingredient'][0], ingrdList['co2'][0])
                    orig_text = html.Center([html.H2(f"We found {org_input[0]} for you!"),
                                            html.H2(f"It emits {org_input[1]} g of CO2 / kg of product"),html.Br(),html.Br()])
                    Data = pd.DataFrame(data=ingrdList)
                    sim_text = html.H4(f"Here is top 5 similar ingredients of {value}")
                    sim_bar_fig = dcc.Graph(figure=similar_bar.Figure(org_input,Data))
                    #Data = Data.drop([0]).sort_values(by=['co2'],ascending=False)
                    Data = Data.drop([0])
                    guage1, guage2, guage3, guage4 = similar_guage.Figure(org_input,Data)

                    guage_text = html.Div([html.H4(f"Here is relative CO2 emission to {org_input[0]}!"),html.H4("Why don't you choose greener one? :)")])
                    guage_fig1 = dcc.Graph(figure=guage1)
                    guage_fig2 = dcc.Graph(figure=guage2)
                    guage_fig3 = dcc.Graph(figure=guage3)
                    guage_fig4 = dcc.Graph(figure=guage4)

                except ValueError:
                    True

    return orig_text, sim_text, sim_bar_fig, guage_text, guage_fig1, guage_fig2, guage_fig3, guage_fig4



def parsingSimIngrdList(response_json):
     ingrd = []
     co2 = []
     for i in response_json:
          ingrd.append(i['ingredient'])
          co2.append(round(i['co2']*1000,2))
     ingrdData = {'ingredient':ingrd,'co2':co2}
     return ingrdData