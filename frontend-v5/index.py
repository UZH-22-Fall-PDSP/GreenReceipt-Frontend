from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from app import app
from pages import home, url, design, ingredient, report, information
from components import navbar, footer

# define components
nav = navbar.Navbar()
footer = footer.Footer()

# Define the index page layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    nav, 
    html.Div(id='page-content', children=[]), 
    footer
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/url':
        return url.layout
    if pathname == '/design':
        return design.layout
    if pathname == '/ingredient':
        return ingredient.layout
    if pathname == '/report':
        return report.layout
    else:
        return home.layout


# Run the app on localhost:8050
if __name__ == '__main__':
    app.run_server(host = '0.0.0.0', port = 8050, debug=True)
