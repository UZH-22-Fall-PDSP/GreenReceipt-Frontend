from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output



## On average, one tree take in 68.5 gram CO2. (25000/365)
## On average, one eletric cat will emit 200 gram CO2 per mile. 

def Text(totalco2):
    treeco2day=60 # CO2 absorbability : 60g of CO2 / day by a mature tree
    tree_co2day = round(totalco2/treeco2day,2)
    carco2day = 525 # CO2 emissions : 525g of CO2 / hour by a typical passenger vehicle
    car_co2mile = round(totalco2/carco2day,2)

    treeresult = f"It takes about {tree_co2day} days to be absorbed by a mature tree."
    carresult = f"It is equivalent to the CO2 emissions by a car in {car_co2mile} hour(s)."
    

    div = dbc.Row(
                  children=[dbc.Col([
                    html.Center(children=[
                         html.Img(src='static/assets/result-tree.png',style={"height":"25%","width":"25%","text-align":"center"}),
                         html.Br(),html.Br(),
                         html.Div([html.P(treeresult),
                                  html.P("( CO2 absorbability : 60g of CO2 / day by a mature tree )")],style={"width":"90%"}),
                        ])
                        ,],style={"text-align":"center"},align="center",width=3),
                    dbc.Col([
                    html.Center(children=[
                         html.Img(src='static/assets/result-car.png',style={"height":"25%","width":"25%","text-align":"center"}),
                         html.Br(),html.Br(),
                         html.Div([html.P(carresult),
                                  html.P("( CO2 emissions : 525g of CO2 / hour by a typical passenger vehicle )")],style={"width":"90%"}),
                        ])
                        ,],style={"text-align":"center"},align="center",width=3)   
                ],justify="center",)


    return div