from dash import html
import dash_bootstrap_components as dbc
from dash_iconify import DashIconify


about_div = html.Div(className="footer_content", 
                    children = [dbc.Row(html.H4("About")),
                                dbc.Row(html.P("Prototyping Data Science Products @UZH"))],
    )

contact_div = html.Div(className="footer_content", 
                      children = [dbc.Row(html.H4("Contact")),
                      dbc.Row([html.P("kaden@uzh.ch"),
                               html.P("songyi.han@uzh.ch"),
                               html.P("yian.gong@uzh.ch"),
                               html.P("mengqi@uzh.ch")
                                ])],
    )

FAQ_div = html.Div(className="footer_content", 
                   children = [dbc.Row(html.H4("FAQ")),
                      dbc.Row(html.P("link"))],
    )

newsletter_div = html.Div(className="footer_content", 
                      children = [dbc.Row(html.H4("News letter")),
                                  dbc.Row([dbc.Col([dbc.Input(placeholder='follow us',size="sm")],width=7),
                                           dbc.Col([dbc.Button('subscribe', outline=True, color="secondary",size="sm")],width=1)])

                    ])

social_media = dbc.Row(className="social-media", 
                       children=[
                                html.Div(DashIconify(icon="ion:logo-github",width=30),style={'width':'40px'}),
                                html.Div(DashIconify(icon="ri:instagram-fill",width=30),style={'width':'40px'}),
                                html.Div(DashIconify(icon="codicon:twitter",width=30),style={'width':'40px'}),
    ])

def Footer():
    layout = dbc.Row(className="footer",
                      children=[dbc.Row([ dbc.Col(about_div),
                                          dbc.Col(contact_div),
                                          dbc.Col(FAQ_div),
                                          dbc.Col(newsletter_div),
                                          ],style={'padding-bottom':'1px'}),
                                dbc.Row(social_media, style = {'margin-bottom': '4px'}),
                                dbc.Row([html.P("This web page is made with ❤️ of group 2")],style={'padding-bottom':'3px'})])

    return layout


