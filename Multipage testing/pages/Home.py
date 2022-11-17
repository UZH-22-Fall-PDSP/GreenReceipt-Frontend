import dash
from dash import dash, html, dcc, Input, Output, State
from dash_labs.plugins.pages import register_page

# # app = dash.Dash(__name__, assets_folder="assets")
register_page(__name__,path="/")

# app.layout = html.Div([
layout = html.Div([
    html.Br(),
    html.H1("🌿 GREEN RECIPE 🌿",style={"text-align": "center","marginTop":"15%","marginBottom":20, "font-size":60}),
    html.H2("Try your recipre CO2 Calculator",style={"text-align": "center"}),
    html.Br(),
    html.H3("Quickly and easily get sustainable scores of your recipe!",style={'font':'30px',"text-align": "center"}),
    html.H3("Your effort can help improve the world environment!",style={'font':'30px',"text-align": "center"}),
    html.Button('START', id='Home_startbutton', 
                 n_clicks=0, style={"text-align": "center", 
                 "width":250, "height" : 70, "border-radius":20, 
                 "font-size":35, "background": "#DBE9D7","position": "relative","left":"42%"}),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.H3("",style={"":""}),
                 ],
    style={"background-image": "url(assets/Background.png)","-webkit-background-size":"100%","background-repeat":" no-repeat","height":"1100px",
    "background-attachment":"fixed","scrollbar-gutter": "stable",
    "margin-block":"-10px -10px","margin-left":"-1%","margin-right":"-1%"
    })

# if __name__ == '__main__':
#     app.run(host = '127.0.0.1',port = 8040,debug = True)
 