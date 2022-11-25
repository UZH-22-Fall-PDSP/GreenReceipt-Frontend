from dash import html
import dash_bootstrap_components as dbc
from components import card


def Banner():
    layout = dbc.Container(className="manual",
                           children=[dbc.Row([dbc.Col(html.H2("Explore our website"))],style={"padding-bottom":"2%"}),
                                     dbc.Row([dbc.Col(card.url_card,width=2,className='column'),
                                              dbc.Col(card.manual_card,md=2,className='column'),
                                              dbc.Col(card.ing_card,md=2,className='column'),
                                              dbc.Col(card.report_card,width=2,style={"margin-bottom":"20px"})],justify='evenly',align='baseline',style={"padding-bottom":"10%"},)                                                                           
                                    ]
                            )

    return layout
