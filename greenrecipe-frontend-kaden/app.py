import dash
from dash import html, dcc
#import dash_bootstrap_components as dbc
from dash_labs.plugins.pages import register_page

app = Dash(__name__, use_pages=True, suppress_callback_exceptions=True)

app.layout = html.Div([
    html.Div(
        [
            html.Div([
            dcc.Link(page['name']+"  |  ", href=page['path'])
            for page in dash.page_registry.values()
            ]),
            html.Hr(),
        ]
    ),
	dash.page_container
])

if __name__ == '__main__':
	app.run_server(debug=True)