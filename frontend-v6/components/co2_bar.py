from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
import requests
import pandas as pd
import plotly.express as px



def Figure(Data):

    figure = px.bar(Data, x='co2', y='recipe',color='ingredients',
             color_discrete_sequence=px.colors.qualitative.Set3,
             orientation='h',
             height=200,
             text='co2')
    figure.update_yaxes(visible=False, showticklabels=False)
    figure.update_xaxes(visible=False, showticklabels=False)
    figure.update_layout({ 'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(0, 0, 0, 0)'})
    figure.update_layout(legend=dict(orientation="h",
                                    yanchor="bottom",
                                    y=1.02,
                                    xanchor="right",
                                    x=1))
    figure.update_traces(textfont_size=15, textangle=0, textposition="inside", cliponaxis=False)


    return figure
