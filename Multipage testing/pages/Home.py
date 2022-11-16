import dash
from dash import dash, html, dcc, Input, Output, State
from dash_labs.plugins.pages import register_page

app = dash.Dash(__name__, assets_folder="assets")
# register_page(__name__,path="/")

app.layout = html.Div([
# layout = html.Div([
    html.Br(),
    html.H1("Green Recipe"),
    html.H2("Try your recipre CO2 Calculator"),
    html.Br(),
    html.H3("Quickly and easily get sustainable scores of your recipe!",style={'font':'30px'}),
    html.H3("Your effort can help improve the world environment!",style={'font':'30px'}),
    html.Br(),
    html.Br(),
    html.Button('START', id='Home_startbutton', 
                 n_clicks=0, style={"text-align": "center", 
                 "width":250, "height" : 70, "border-radius":20, 
                 "font-size":35, "background": "#DBE9D7",'marginLeft': 550})],
    style={"background-image": "url(assets/Background.png)","background-size": "cover",
    "-webkit-background-size": "cover","-o-background-size": "cover","background-position":" center 0",
    "width":"100%","height":"100%"})

if __name__ == '__main__':
    app.run(host = '127.0.0.1',port = 8040,debug = True)
