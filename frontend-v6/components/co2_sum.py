from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from dash_iconify import DashIconify



def Text(recipeName, totalco2):

    div = html.Div([html.Div(className="total-co2-is",children=[html.H4(f"The total CO2 emission of")]),
          html.Div(className="total-co2",
                   children=[
                             html.Div(className='recipe-name',
                                      children=[html.Div(DashIconify(icon="mdi:format-quote-open-outline",width=20)),
                                                html.H4(f"{recipeName}"),
                                                html.Div(DashIconify(icon="mdi:format-quote-close-outline",width=20)),
                                                ]),                        
                             html.Div(html.H4(f"is")),
                             html.Div(html.H2(f"{totalco2}")),
                             #html.Div(html.Img(src='static/assets/footprint_icon.png',style={"height":"50px"}))
        ])


      ])
          

    return div
