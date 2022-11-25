from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output



## On average, one tree take in 68.5 gram CO2. (25000/365)
## On average, one eletric cat will emit 200 gram CO2 per mile. 

def Text(totalco2):
    treeco2day=25000/365
    co2day = totalco2/treeco2day
    carco2mile = 200
    co2mile = totalco2/carco2mile

    treeresult = "Your recipe will generate the equivalent of the CO2 taken in by a tree for "+ str(co2day) + " days"
    carresult = "Your recipe will generate the equivalent of the CO2 produced by an eletric car driving " + str(co2mile)+ " mile."
    

    div = dbc.Row(
                  children=[dbc.Col([
                    html.Center(children=[
                         html.Img(src='static/assets/result-tree.png',style={"height":"25%","width":"25%","text-align":"center"}),
                         html.Br(),html.Br(),
                         html.Div(html.P(treeresult),style={"width":"90%"}),
                        ])
                        ,],style={"text-align":"center"},align="center",width=3),
                    dbc.Col([
                    html.Center(children=[
                         html.Img(src='static/assets/result-car.png',style={"height":"25%","width":"25%","text-align":"center"}),
                         html.Br(),html.Br(),
                         html.Div(html.P(carresult),style={"width":"90%"}),
                        ])
                        ,],style={"text-align":"center"},align="center",width=3)   
                ],justify="center",)


    return div