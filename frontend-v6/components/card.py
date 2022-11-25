import dash_bootstrap_components as dbc
from dash import html, dcc
from dash_iconify import DashIconify

url_card = dbc.Card(
    dbc.CardBody(
        [
            dbc.Row(html.H5("Recipe Calculator", className="card-title"),style={'padding':'3%'}),
            DashIconify(icon="material-symbols:co2",style={"color": "#9ce236","width":"100","height":"100"},width=60),
            dbc.Row(html.P("Enter your recipe url from food.com for the detailed CO2 emission ")),
        ],
    )
)


manual_card = dbc.Card(
    dbc.CardBody(
        [
            dbc.Row(html.H5("Manual Calculator", className="card-title"),style={'padding':'3%'}),
            DashIconify(icon="clarity:form-line",style={"color": "#9ce236","width":"70","height":"70",'margin':'15px'},
                                width=60),
            html.Br(),
            html.P("Didn't find the recipe? Enter the ingredients manually to calculate co2 level of your own recipe."),

        ] 
    )
)

ing_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Find Green Ingredient", className="card-title"),
            DashIconify(icon="mdi:green-circle-outline",style={"color": "#9ce236","width":"70","height":"85",'margin':'10px'},width=60),
            html.P("Enter your favorite ingredient, then you will find similar and greener ingredients !"),
        ]
    )
)

report_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Ingredients Categorical Report", className="card-title"),
            DashIconify(icon="mdi:report-areaspline",style={"color": "#9ce236","width":"70","height":"80",'margin':'12px'},width=60),
            html.P("Want to learn more about CO2 level of ingredients by category? Check out our report"),
        ]
    )
)