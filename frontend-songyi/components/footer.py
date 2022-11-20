from dash import html
import dash_bootstrap_components as dbc
from dash_iconify import DashIconify


about_div = html.Div(className="footer_content", 
                    children = [dbc.Row(html.H4("About")),
                                dbc.Row(html.P("Prototyping Data Science Products @UZH"))],
    )

contact_div = html.Div(className="footer_content", 
                      children = [dbc.Row(html.H4("Contact")),
                      dbc.Row(html.P("abc@gmail.com"))],
    )

FAQ_div = html.Div(className="footer_content", 
                   children = [dbc.Row(html.H4("FAQ")),
                      dbc.Row(html.P("link"))],
    )

newsletter_div = html.Div(className="footer_content", 
                      children = [dbc.Row(html.H4("News letter")),
                                  dbc.Row(html.P("link"))],
    )

social_media = html.Div(
        [DashIconify(icon="ion:logo-github",width=30),
         DashIconify(icon="ri:instagram-fill",width=30),
         DashIconify(icon="codicon:twitter",width=30),
         ]

    )

def Footer():
    layout = dbc.Row(className="footer",
                      children=[dbc.Row([ dbc.Col(about_div),
                                          dbc.Col(contact_div),
                                          dbc.Col(FAQ_div),
                                          dbc.Col(newsletter_div),
                                          ]),
                                dbc.Row(social_media, style = {'margin': '1%'}),
                                dbc.Row([html.P("This web page is made by ❤️ from group 2")])])

    return layout


