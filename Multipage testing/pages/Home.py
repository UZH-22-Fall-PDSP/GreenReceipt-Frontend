import dash
from dash import dash, html, dcc, Input, Output, State
from dash_labs.plugins.pages import register_page


register_page(__name__,path="/")

layout = html.Div([
    html.H1("Green Recipe",style={"marginTop":150,'background-image':'url(home_img)'}),
    html.H2("Try your recipre CO2 Calculator"),
    html.Br(),
    html.H3("Quickly and easily get sustainable scores of your recipe!",style={'font':'30px'}),
    html.H3("Your effort can help improve the world environment!",style={'font':'30px'}),
    html.Br(),
    html.Br(),
    html.Button('START', id='Home_startbutton', 
                 n_clicks=0, style={"text-align": "center", 
                 "width":250, "height" : 70, "border-radius":20, 
                 "font-size":35, "background": "#DBE9D7",'marginLeft': 550})])

