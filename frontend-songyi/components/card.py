import dash_bootstrap_components as dbc
from dash import html
from dash_iconify import DashIconify

url_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("URL Calculator", className="card-title"),
            DashIconify(icon="material-symbols:co2",width=60),
            html.P("This card has some text content, but not much else"),
            dbc.Button("Calculate CO2", color="secondary", style={'margin': '5%'}),
        ]
    )
)


manual_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Manual calculor", className="card-title"),
            DashIconify(icon="clarity:form-line",width=60),
            html.P("This card has some text content, but not much else"),
            dbc.Button("Calculate CO2", color="secondary",style={'margin': '5%'}),
        ]
    )
)

ing_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Find Green ingredient", className="card-title"),
            DashIconify(icon="mdi:green-circle-outline",width=60),
            html.P("This card has some text content, but not much else"),
            dbc.Button("Find ingredient", color="secondary",style={'margin': '5%'}),
        ]
    )
)

report_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Report", className="card-title"),
            DashIconify(icon="mdi:report-areaspline",width=60),
            html.P("This card has some text content, but not much else"),
            dbc.Button("Go to report", color="secondary",style={'margin': '5%'}),
        ]
    )
)