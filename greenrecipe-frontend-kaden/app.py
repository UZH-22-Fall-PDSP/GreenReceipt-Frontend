from dash import Dash, html, dcc
import dash

app = Dash(__name__, use_pages=True, suppress_callback_exceptions=True)

app.layout = html.Div([
    html.Div(
        [
            html.Br(),
            html.Div([
            dcc.Link(page['name']+"  |  ", href=page['path'])
            for page in dash.page_registry.values()
            ],style = {"font": "Brown","font-size":20}),
            html.Br()
        ]
    ),
	dash.page_container
],style = {"scrollbar-gutter": "stable"})

if __name__ == '__main__':
	app.run_server(debug=True)