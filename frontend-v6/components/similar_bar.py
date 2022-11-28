from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
import requests
import pandas as pd
import plotly.express as px


def Figure(orig_input, Data):
    figure = px.bar(Data, x="co2", y="ingredient", color='ingredient', orientation='h',
             hover_data=["ingredient", "co2"],
             color_discrete_sequence=px.colors.qualitative.Pastel1,
             height=400,
             labels=dict(co2="g of CO2 / kg of product"))
    figure.update_xaxes(
    scaleratio = 0.5,
  )
    figure.update_layout({ 'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(0, 0, 0, 0)'})
    figure.update_yaxes(visible=False, showticklabels=False)
    figure.add_vline(x=orig_input[1], line_width=2, line_dash="dash", line_color="gray")
    return figure
