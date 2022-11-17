import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
# dbc = ash_bootstrap_components


app = dash.Dash(__name__, use_pages=True)

nav_content = [
    dbc.NavItem([dbc.NavLink("Home", href="/", active=True), 
                dbc.NavLink("RecipeCO2Calculator", href="/RecipeCO2Calculator")]),
#     dbc.NavLink("Ingredient Searching page", href="/IngredientCalculator"),
#     dbc.NavLink("Design Recipe", href="/DesignRecipe"),
#     dbc.NavLink("Report", href="/IngredientsReport"),
#     dbc.NavLink("Button", id="button-link", n_clicks=0)
]

# nav_content = [
#     dbc.NavItem(dbc.NavLink("Home", href="/", active=True)),
#     #dbc.NavItem(dbc.NavLink("Recipe CO2 Calculator", href="/RecipeCO2Calculator")),
#     dbc.NavItem(dbc.NavLink("Ingredient Searching page", href="/Ingredient_searching")),
#     dbc.NavItem(dbc.NavLink("Design Recipe", href="/DesignRecipe")),
#     dbc.NavItem(dbc.NavLink("Report", href="/IngredientReport"))
# ]

nav1 = dbc.Nav(nav_content, pills = True, fill = True, justified=True, vertical = False, style = ({'margin-right':'30px'}))
navs = html.Div([nav1, html.Hr()])


## Page Layout 
app.layout = html.Div(
    [
        # main app framework
        navs,
        # content of each page
        dash.page_container
    ]
)

# @app.callback([Output("page-content", "children"),
#                Input('url', 'pathname')])



if __name__ == '__main__':
    app.run(host = '127.0.0.1',port = 8050,debug = True)



# def display_content(pathname):

#     if pathname == '/':
#         return home.layout

#     elif pathname == '/a':
#         return archive.layout()
        
#     else:
#         return home.layout
     
# navigation = html.Div(
#     [
#         # html.H2("Navigation", className="display-3"),
#         # html.P(
#         #     "Green Recipe", className="lead"
#         # ),
#         dbc.Nav(
#             [   
#                 dbc.NavLink("Home", href="/", active="exact"),
#                 dbc.NavLink("Recipe Calculator", href="/page-1", active="exact"),
#                 dbc.NavLink("Design Recipe", href="/page-1", active="exact"),
#                 dbc.NavLink("Ingredient Calculator", href="Ingredient Calculato", active="exact")
#                 # dbc.NavLink("Page 2", href="/page-2", active="exact"),
#             ],
#             vertical=True,
#             pills=True,
#         )
#     ],
#     style=Navigation_Style,
# )


# app.layout = html.Div(
#     [
#         # main app framework
#         # html.Div("Green Recipe", style={'fontSize':50, 'textAlign':'center'}),
#         html.Div([
#             dcc.Link(page['name']+"  |  ", href=page['path'])
#             for page in dash.page_registry.values()
#         ]),
#         html.Hr(),
#         # dcc.Location(id='url'),

#         # html.Div(id='page-content'),
#         # content of each page
#         dash.page_container
#     ]
# )