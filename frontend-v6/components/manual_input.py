import dash
from dash import html, dcc, callback, Input, Output, State, dash_table
import requests
import plotly.express as px
import pandas as pd
from collections import OrderedDict

'''

@app.callback(
    Output('adding-rows-table', 'data'),
    Input('editing-rows-button', 'n_clicks'),
    State('adding-rows-table', 'data'),
    State('adding-rows-table', 'columns'))
def add_row(n_clicks, rows, columns):
    if n_clicks > 0:
        rows.append({c['id']: '' for c in columns})
    return rows
'''