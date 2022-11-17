import dash
from dash import html, dcc
#import dash_bootstrap_components as dbc
# dbc = ash_bootstrap_components

#styling the navigation bar 
Navigation_Style = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "right":0,
    "bottom": 680,
    "width": "5 rem",
    "height":"5 rem",
    "padding":"1rem 0rem",
    "background-color": "#eafaf3",
}


navigation = html.Div(
    [
        # html.H2("Navigation", className="display-3"),
        # html.P(
        #     "Green Recipe", className="lead"
        # ),
        dbc.Nav(
            [   
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Recipe Calculator", href="/page-1", active="exact"),
                dbc.NavLink("Design Recipe", href="/page-1", active="exact"),
                dbc.NavLink("Ingredient Calculator", href="Ingredient Calculato", active="exact")
                # dbc.NavLink("Page 2", href="/page-2", active="exact"),
            ],
            vertical=True,
            pills=True,
        )
    ],
    style=Navigation_Style,
)

app = dash.Dash(__name__, use_pages=True)

# app.layout = html.Div([
#     dcc.Location(id="url"),
#     navigation,
#     dash.page_container
# ])

app.layout = html.Div(
    [
        # main app framework
        # html.Div("Green Recipe", style={'fontSize':50, 'textAlign':'center'}),
        html.Div([
            dcc.Link(page['name']+"  |  ", href=page['path'])
            for page in dash.page_registry.values()
        ]),
        html.Hr(),

        # content of each page
        dash.page_container
    ]
)

if __name__ == '__main__':
    app.run(host = '127.0.0.1',port = 8085,debug = True)


