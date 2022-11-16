import dash
from dash import html, dcc
# from dash import dash_bootstrap_components
# dbc = ash_bootstrap_components

# styling the sidebar
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "5rem",
    "padding": "2rem 1rem",
    "background-color": "#eafaf3",
}


# sidebar = html.Div(
#     [
#         html.H2("Sidebar", className="display-4"),
#         html.Hr(),
#         html.P(
#             "Green Recipe", className="lead"
#         ),
#         dbc.Nav(
#             [
#                 dbc.NavLink("Home", href="/", active="exact"),
#                 dbc.NavLink("Ingredient Calculator", href="/page-1", active="exact"),
#                 # dbc.NavLink("Page 2", href="/page-2", active="exact"),
#             ],
#             vertical=False,
#             pills=True,
#         ),
#     ],
#     style=SIDEBAR_STYLE,
# )

app = dash.Dash(__name__, use_pages=True)

# app.layout = html.Div([
#     dcc.Location(id="url"),
#     sidebar
# ])

app.layout = html.Div(
    [
        # main app framework
        html.Div("Green Recipe", style={'fontSize':50, 'textAlign':'center'}),
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



