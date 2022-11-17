import dash
from dash import dash, html, dcc, Input, Output, State

app = dash.Dash(__name__, assets_folder="assets")
#register_page(__name__,path="/")

app.layout = html.Div([
#layout = html.Div([
  
    html.Div([

        html.H1("🌿 GREEN RECIPE 🌿",style={"text-align": "center","marginTop":150, "font-size":60}),

        ## [SUB-COMPONENT] URL RECIPE - INPUT
        dcc.Input(id='url_recipe_input',
         placeholder='Input your Recipe URL from food.com',
         type='text',
         style={"border-radius":5, "width":650, "padding" : 10,"font-size":20}),

        html.Br(), html.Br(),

        ## [SUB-COMPONENT] URL RECIPE - CALCULATION BUTTON
        html.Button('CALCULATION', id='url_recipe_cal', n_clicks=0, style={"text-align": "center", "width":200, "height" : 50, "border-radius":10, "font-size":20, "background": "#DBE9D7"})
        ],

      style={"text-align": "center", "border-radius":20})
             
                 ],

    # style for the whole page
                 
    style={

    # backgroud picture
    "background-image": "url(assets/background2.png)",
    # backgroud size and position
    "background-position-y":"top", "background-size": "cover",

    # scrollbar
    "scrollbar-gutter": "stable",
    # size of the whole page
    "margin-top":"-10px","margin-left":"-1%","margin-right":"-1%"
    })

if __name__ == '__main__':
      app.run(host = '127.0.0.1',port = 8030,debug = True)
 