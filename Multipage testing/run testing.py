import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
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

app = dash.Dash(__name__,use_pages= True)

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
        # dcc.Location(id='url'),

        # html.Div(id='page-content'),
        # content of each page
        dash.page_container
    ]
)

# @app.callback([Output("page-content", "children"),
#               Input('url', 'pathname')
#               ])

# def display_content(pathname):

#     if pathname == '/':
#         return home.layout

#     elif pathname == '/a':
#         return archive.layout()
        
#     else:
#         return home.layout
if __name__ == '__main__':
    app.run(host = '127.0.0.1',port = 8085,debug = True)


def generate_piechart(n_clicks, value):

     imgredientName = checkValidURL(value)

     backendURL = LOCAL_TEST_URL
     response = requests.get(url = backendURL,  params={'recipe': recipeName})

     ingrdco2 = ''


     if (response.status_code != 204 and
          response.headers["content-type"].strip().startswith("application/json")):
          try:
               response_json = response.json()
               recipeName, totalco2, ingrdList = parsingRecipeCO2(response_json)
               title = 'Total CO2 of "' + recipeName + '" is ' + str(totalco2) + ' / 1 serve'
               BDdata= pd.DataFrame(ingrdList).sort_values(by=['co2'], ascending=False)
               ingrd_details_fig = px.bar(BDdata, x='ingredient', y='co2',text_auto=True,
                                             title=title)
               ingrd_details_fig.update_layout(title_x=0.5)

          except ValueError:
               True

     return ingrd_details_fig