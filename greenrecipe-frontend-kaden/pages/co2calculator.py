import dash
from dash import html, dcc, callback, Input, Output, State, dash_table
import requests
import plotly.express as px
import pandas as pd
from collections import OrderedDict


dash.register_page(__name__)

df = pd.DataFrame(OrderedDict([
    ('ingrd', ["","","","",""]),
    ('q', [0.0,0.0,0.0,0.0,0.0]),
    ('u', ['g', 'g', 'g', 'g' , 'g'])
]))

layout = html.Div([
                ## [COMPONENET]
                html.Div([
                        html.Br(),html.Br(),html.Br(),html.Br(),
                        html.H1("DESIGN YOUR OWN RECIPE",style={"text-align": "center","margin-bottom":"100px", "font-size":60,"font": "White"}),

                        ## [SUB-COMPONENT] Ingredient - INPUT
                        dcc.Input(id='ingrd_input',
                                    placeholder='Find similar ingredients with co2 level',
                                    type='text',
                                    style={"border-radius":5, "width":650, "padding" : 10,"font-size":20}),

                        ## [SUB-COMPONENT] Searching Similar Ingredients - SEARCH BUTTON
                        html.Button('SEARCH', id='ingrd_sim_search', n_clicks=0, style={"text-align": "center", "width":200, "height" : 50, "border-radius":10, "font-size":20, "background": "white"}),
                        html.Br(),html.Br(),html.Br(),html.Br(),        

                        ## [SUB-COMPONENT] Similar Ingredients Result - Pie Chart
                        dcc.Graph(id='ingrd_sim_graph')                     
                        ], style={"text-align": "center",
                                    # backgroud picture
                                    "background-image": "url(assets/background3.png)",
                                    # backgroud size and position
                                    "background-position-y":"top", "background-size": "cover",
                                    # margin for the district
                                    "margin-top":"-10px"}
                        ),
                
                html.Br(), html.Br(),

                ## [COMPONENET]
                html.Div([
                        html.Div(children=[
                        ## [SUB-COMPONENT] Manual Recipe Input - TABLE
                        dash_table.DataTable(
                            id='manual-recipe-table',
                            data=df.to_dict('records'),
                            columns=[
                                {'id': 'ingrd', 'name': 'Ingredient'},
                                {'id': 'q', 'name': 'Quantity', "type": "numeric"},
                                {'id': 'u', 'name': 'Unit', 'presentation': 'dropdown'},
                            ],
                            editable=True,
                            dropdown={
                                'u': {'options': [{'label': i, 'value': i} for i in ['g','kg']], 'clearable' : False}
                            },
                        )], style ={"margin":"0 15%"}),                        
                        
                        html.Div(children=[
                        ## [SUB-COMPONENT] Manual Recipe CO2 Output - INGREDIENTS DETAIL Bar graph
                        dcc.Graph(id='manual_ingrd_detail_graph',style={} ),
                        
                        ## [SUB-COMPONENT] Updating the manual recipe co2 - UPDATE BUTTON
                        html.Button('UPDATE', id='manual_ingrd_update', n_clicks=0, style={"text-align": "center", "width":200, "height" : 50, "border-radius":10, "font-size":20, "background": "white"})                        
                        ]),]
                        ,style={'display': 'flex', 'flex-direction': 'row',"text-align": "center","font-size":30,"width":"80%","margin":"0 auto"}
                        ),
                        html.Br(),html.Br(),html.Br(),html.Br()
                ], 
    # style for the whole page
    style={

    # scrollbar
    "scrollbar-gutter": "stable",
    # size of the whole page
    "margin-top":"-10px","margin-left":"-1%","margin-right":"-1%"})


LOCAL_TEST_URL = 'http://127.0.0.1:5000'
GCP_BACKEND_URL = 'XXX.XXX.XXX.XXX'

@callback(
     Output('manual_ingrd_detail_graph','figure'),
     Input('manual_ingrd_update', 'n_clicks'),
     State('manual-recipe-table', 'data'))
def update_manualrecipe_result(n_clicks, rows):

    backendURL = LOCAL_TEST_URL + '/calculatorCO2'
    ingrd_details_fig = px.bar()

    ingrdSet = parsingManualTable(rows)
    if '' not in ingrdSet['ingrd']:
        response = requests.post(url = backendURL,  json = ingrdSet)
        if (response.status_code != 204 and
            response.headers["content-type"].strip().startswith("application/json")):
            try:
                response_json = response.json()
                totalco2, ingrdList = parsingManualCO2(response_json)
                title = 'Total CO2 is ' + str(totalco2)
                BDdata= pd.DataFrame(ingrdList).sort_values(by=['co2'], ascending=False)
                ingrd_details_fig = px.bar(BDdata, x='ingredient', y='co2',text_auto=True,
                                                title=title)
                ingrd_details_fig.update_layout(title_x=0.5)

            except ValueError:
                True

    return ingrd_details_fig

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

def parsingManualTable(rows):
    ingrd = []
    ingrd_q = []
    ingrd_u = []
    for r in rows:
        ingrd.append(r['ingrd'])
        ingrd_q.append(r['q'])
        ingrd_u.append(r['u'])
    ingrdSet = {'ingrd':ingrd,'ingrd_q':ingrd_q,'ingrd_u':ingrd_u}
    return ingrdSet

def parsingManualCO2(response_json):
     totalco2 = response_json['totalCO2']
     ingrdList = response_json['ingrdCO2List']
     ingrd = []
     co2 = []
     for i in ingrdList:
          ingrd.append(i['ingredient'])
          co2.append(i['co2'])
     ingrdData = {'ingredient':ingrd,'co2':co2}
     return totalco2, ingrdData

def parsingSimIngrdList(response_json):
     ingrd = []
     co2 = []
     for i in response_json:
          ingrd.append(i['ingredient'])
          co2.append(i['co2'])
     ingrdData = {'ingredient':ingrd,'co2':co2}
     return ingrdData