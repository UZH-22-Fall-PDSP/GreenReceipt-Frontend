from dash import html
import dash_bootstrap_components as dbc
from components import card


def Banner():
    layout = dbc.Container(className="manual",
                           children=[dbc.Row([dbc.Col(html.H2("Explore our CO2 calculator"))]),
                                     dbc.Row([dbc.Col(card.url_card),
                                              dbc.Col(card.manual_card),
                                              dbc.Col(card.ing_card),
                                              dbc.Col(card.report_card)])                                                                           
                                    ])

    return layout
