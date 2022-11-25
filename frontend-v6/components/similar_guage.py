from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
import requests
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def Figure(org_input, Data):
    
    max_co2 = max(list(Data['co2']))
    results = []

    for i in range(4):

        if Data['co2'].iloc[i] > org_input[1]: 
            bar_color = 'tomato'
        else : 
            bar_color = 'yellowgreen'

        fig = go.Figure(go.Indicator(
            value = Data['co2'].iloc[i],
            delta = {'reference': org_input[1],
                    'increasing': {'color': "red"},
                     'decreasing': {'color': "green"}
                     },
            gauge = {'bar': {'color': bar_color},
                     'axis': {'range': [None, max_co2] },
                     'threshold': { 'value': org_input[1],
                                    'line': {'color': "red", 'width': 4},
                                    'thickness': 0.75,}},
            mode = "gauge+number+delta",
            title = {'text': Data['ingredient'].iloc[i], 'font': {'size': 18}},
            ))

        fig.update_layout(autosize=False, width=200,height=180,
                        margin=dict(l=0,r=0,b=0,t=30,pad=2))
        results.append(fig)

    fig1, fig2, fig3, fig4 = results[0], results[1], results[2], results[3]
    
    return fig1, fig2, fig3, fig4


