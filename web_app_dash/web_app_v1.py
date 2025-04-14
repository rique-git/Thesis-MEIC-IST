import dash
import numpy as np
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import joblib

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.FLATLY],
    suppress_callback_exceptions=True 
)

model = joblib.load('kaggle_model.pkl')
# Navbar with links to switch between pages
navbar = dbc.Navbar(
    dbc.Container([
        # Left: Logo or App Name
        html.A(
            dbc.Row([
                dbc.Col(html.Img(src="/assets/logo.png", height="30px")),  # You can put your logo in /assets
            ], align="center", className="g-0"),
            href="#",
            style={"textDecoration": "none"}
        ),

        # Center: Navigation items
        dbc.Nav([
            dbc.NavItem(dbc.NavLink("Início", href="/inicio")),
            dbc.NavItem(dbc.NavLink("Índice de Risco", href="/indice")),
            dbc.NavItem(dbc.NavLink("Ajuda", href="/ajuda")),
        ], className="mx-auto", navbar=True),

        # Right: Language or login (optional)
        dbc.Nav([
            dbc.NavItem(dbc.NavLink("EN", href="#")),
            dbc.NavItem(dbc.NavLink("Entrar", href="#")),
        ], navbar=True),
    ]),
    color="#276f48",
    dark=True,
    sticky="top",
)


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    
    html.Div([
        navbar,
        dbc.Container(  # ← This keeps your content centered
            html.Div(id="page-content", className="flex-grow-1 mt-4")
        ),
    ], className="d-flex flex-column min-vh-100"),
    
    html.Footer(
        dbc.Container(
            html.Small([
                "Copyright © 2025 | LOGO-AF",
                html.Br(),
                "Updated: YYYY-MM-DD"
            ], className="text-muted")
        ),
        className="text-center py-3 bg-light"
    )
])


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
    



# Callback for rendering content based on selected tab in the "Índice de Risco" page
@app.callback(
    Output("tab-content", "children"),
    Input("tabs", "active_tab")
)
def render_tab(tab):
    if tab == "geral":
        return html.Div([
                    dbc.Row([
                        dbc.Col([dbc.Label("Idade"), dbc.Input(id="input-age", type="number", placeholder="Ex: 70")], width=4),

                        dbc.Col([dbc.Label("Sexo"), dcc.Dropdown(id="input-sex", options=[{"label": "Masculino", "value": 1},
                                                                                          {"label": "Feminino", "value": 0},
                                                                                         ], value = 1)], width=4),

                        dbc.Col([dbc.Label("Tipo de Dor no Peito"), dcc.Dropdown(id="input-cp", options=[{"label": "Tipo 1", "value": 0},
                                                                                                         {"label": "Tipo 2", "value": 1},
                                                                                                         {"label": "Tipo 3", "value": 2},
                                                                                                         {"label": "Tipo 4", "value": 3},
                                                                                                        ], value = 1)], width=4),
                    ]),

                    dbc.Row([
                        dbc.Col([dbc.Label("Pressão Arterial"), dbc.Input(id="input-bp", type="number", value = 120)], width=4),
                        dbc.Col([dbc.Label("Colesterol"), dbc.Input(id="input-chol", type="number", value = 250)], width=4),
                        dbc.Col([dbc.Label("FBS > 120"), dcc.Dropdown(id="input-fbs", options=[{"label": "Sim", "value": 1},
                                                                                               {"label": "Não", "value": 0},
                                                                                              ], value = 0)], width=4),
                    ]),

                    dbc.Row([
                        dbc.Col([dbc.Label("Resultados ECG"), dcc.Dropdown(id="input-ecg", options=[{"label": "Normal", "value": 0},
                                                                                                    {"label": "Anormalidade", "value": 1},
                                                                                                   ], value = 0)], width=4),

                        dbc.Col([dbc.Label("Frequência Cardíaca Máx"), dbc.Input(id="input-hr", type="number", value = 150)], width=4),

                        dbc.Col([dbc.Label("Angina de Exercício"), dcc.Dropdown(id="input-angina", options=[{"label": "Sim", "value": 1},
                                                                                                            {"label": "Não", "value": 0},
                                                                                                           ], value = 1)], width=4),
                    ]),

                    dbc.Row([
                        dbc.Col([dbc.Label("ST Depression"), dbc.Input(id="input-oldpeak", type="number", value = 2)], width=4),

                        dbc.Col([dbc.Label("Slope ST"), dcc.Dropdown(id="input-slope", options=[{"label": "Ascendente", "value": 1},
                                                                                                {"label": "Horizontal", "value": 2},
                                                                                                {"label": "Descendente", "value": 3},
                                                                                               ], value = 2)], width=4),

                        dbc.Col([dbc.Label("Nº Vasos Fluoro"), dbc.Input(id="input-vessels", type="number", value=1)], width=4),
                    ]),

                    dbc.Row([
                        dbc.Col([dbc.Label("Talium"), dcc.Dropdown(id="input-thallium", options=[{"label": "Normal", "value": 3},
                                                                                                 {"label": "Defeito Reversível", "value": 6},
                                                                                                 {"label": "Defeito Irreversível", "value": 7},
                                                                                                ], value = 3)], width=4),
                    ]),

                    dbc.Button("Calcular", id="calcular-btn", color="primary", className="mt-3"),
                    html.Div(id="prediction-output", className="mt-3"),

            ])

    elif tab == "comp":
        return html.Div("Conteúdo das complicações...")

    elif tab == "sever":
        return html.Div("Conteúdo de severidade...")

@app.callback(
    Output("prediction-output", "children"),
    Input("calcular-btn", "n_clicks"),
    State("input-age", "value"),
    State("input-sex", "value"),
    State("input-cp", "value"),
    State("input-bp", "value"),
    State("input-chol", "value"),
    State("input-fbs", "value"),
    State("input-ecg", "value"),
    State("input-hr", "value"),
    State("input-angina", "value"),
    State("input-oldpeak", "value"),
    State("input-slope", "value"),
    State("input-vessels", "value"),
    State("input-thallium", "value"),
    prevent_initial_call=True
)
def predict(n_clicks, age, sex, cp, bp, chol, fbs, ecg, hr, angina, oldpeak, slope, vessels, thallium):
    
    inputs = [age, sex, cp, bp, chol, fbs, ecg, hr, angina, oldpeak, slope, vessels, thallium]
    if any(value is None for value in inputs):
        return dbc.Alert("Por favor preencha todos os campos.", color="warning")
    
    # Prepare the features for prediction
    features = np.array([inputs])
    
    # Make the prediction using the model
    prediction = model.predict(features)[0]
    
    # Return the prediction result
    if prediction == 1:
        return dbc.Alert("Resultado: Doença cardíaca detectada", color="danger")
    else:
        return dbc.Alert("Resultado: Sem doença cardíaca", color="success")



if __name__ == '__main__':
    app.run(debug=True, port=8054)
