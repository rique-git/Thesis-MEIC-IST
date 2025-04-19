from dash import html, Input, Output, dcc
import dash_bootstrap_components as dbc

from myapp import app

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