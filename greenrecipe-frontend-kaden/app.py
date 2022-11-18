from dash import Dash, html, dcc
import dash

app = Dash(__name__, use_pages=True, suppress_callback_exceptions=True)

app.layout = html.Div([
    html.Div(
        [
            html.Br(),
            html.Div([
            dcc.Link(" "+page['name']+"  |  ", href=page['path'])
            for page in dash.page_registry.values()
            ],style = {"font": "White","font-size":20,"text-align":"center"}),
            html.Br(),
            html.Br()
        ],style ={"background-color":"Black","margin-block":"-10px 0px","margin-left":"-1%","margin-right":"-1%"}
    ),
	dash.page_container
],style = {"scrollbar-gutter": "stable" })

if __name__ == '__main__':
	app.run_server(debug=True)