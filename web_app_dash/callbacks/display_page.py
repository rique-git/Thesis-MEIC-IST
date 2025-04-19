from dash import html, Input, Output
import dash_bootstrap_components as dbc

from myapp import app

@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname")
)
def display_page(pathname):
    if pathname == "/inicio" or pathname == "/":
        return html.Div([

            # Welcome text + Logo side by side
            html.Div(
                [
                    html.H1("Bem-vindo à plataforma", className="mb-0"),
                    html.Img(src="/assets/logo.png", height="80px", style={"marginLeft": "20px"})
                ],
                style={"display": "flex", "alignItems": "center", "justifyContent": "flex-start", "marginTop": "20px"}
            ),

            # Slim grey separator
            html.Hr(style={"border": "1px solid #D3D3D3", "marginTop": "20px", "marginBottom": "20px"}),

            # Platform Description
            html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut " \
            "labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris " \
            "nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit " \
            "esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt "
            "in culpa qui officia deserunt mollit anim id est laborum.", className="text-left"),

            # Login info
            html.P("Pode fazer o login aqui", className="text-left"),
            html.P("Ainda não tem uma conta? Por favor contacte o administrador", className="text-left"),

            # About the platform
            html.H4("Sobre", className="mt-4"),
            html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut " \
            "labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris " \
            "nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit " \
            "esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt "
            "in culpa qui officia deserunt mollit anim id est laborum.", className="text-left"),

            # Disclaimer
            html.H4("Aviso", className="mt-4"),
            html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut " \
            "labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris " \
            "nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit " \
            "esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt "
            "in culpa qui officia deserunt mollit anim id est laborum.", className="text-left"),

            # IST Logo at the bottom
            html.Div(
                html.Img(src="/assets/ist_logo.png", height="50px"),  # Adjust image source and size
                className="d-flex justify-content-center",
                style={"marginTop": "30px"}
            ),
            
        ])  # your inicio content
    
    elif pathname == "/indice":
        return html.Div([
            html.H2("Índice de Risco", className="mt-4"),
            dbc.Tabs([
                dbc.Tab(label="Geral", tab_id="geral"),
                dbc.Tab(label="Advanced", tab_id="comp"),
                dbc.Tab(label="Multi-Label", tab_id="sever"),
            ], id="tabs", active_tab="geral"),

            html.Div(id="tab-content", className="mt-3"),
        ]) 
    
    elif pathname == "/ajuda":
        return html.H2("Página de Ajuda", className="mt-4")
    
    else:
        return html.H2("Página não encontrada", className="mt-4")