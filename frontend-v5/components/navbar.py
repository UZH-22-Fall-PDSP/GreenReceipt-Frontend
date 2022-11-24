# Import necessary libraries
from dash import html
import dash_bootstrap_components as dbc


# Define the navbar structure
def Navbar():

    layout = html.Div([
        dbc.NavbarSimple(className="navbar",
            children=[
                dbc.NavItem(dbc.NavLink("URL", href="/url")),
                dbc.NavItem(dbc.NavLink("Design", href="/design")),
                dbc.NavItem(dbc.NavLink("Ingredient", href="/ingredient")),
                dbc.NavItem(dbc.NavLink("Report", href="/report")),
            ] ,
            brand="🍴🌿 Green Recipe ",
            brand_href="/",
            color="light",
            fluid=True
            
        ), 
    ])

    return layout
