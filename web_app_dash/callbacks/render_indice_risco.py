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
                dbc.Col([dbc.Label("Age Range"), dcc.Dropdown(
                    id="input-age",
                    options=[
                        {"label": "40-49", "value": 0},
                        {"label": "50-59", "value": 1},
                        {"label": "60-69", "value": 2},
                        {"label": "70-79", "value": 3},
                        {"label": "80-89", "value": 4},
                        {"label": "90+", "value": 5}
                    ],
                    placeholder="Select age range"
                )], width=4),

                dbc.Col([dbc.Label("Sex"), dcc.Dropdown(
                    id="input-sex",
                    options=[
                        {"label": "Male", "value": 0},
                        {"label": "Female", "value": 1}
                    ],
                    value=0  # default: Male
                )], width=4),

                dbc.Col([dbc.Label("Weight (kg)"), dbc.Input(id="input-wgt", type="number", value=80)], width=4),
            ]),

            dbc.Row([
                dbc.Col([dbc.Label("Height (cm)"), dbc.Input(id="input-hgt", type="number", value=175)], width=4),
                dbc.Col([dbc.Label("BMI"), dbc.Input(id="input-bmi", type="number", value=25.5)], width=4),
                dbc.Col([dbc.Label("Systolic BP (SBP)"), dbc.Input(id="input-sbp", type="number", value=120)], width=4),
            ]),

            dbc.Row([
                dbc.Col([dbc.Label("Diastolic BP (DBP)"), dbc.Input(id="input-dbp", type="number", value=80)], width=4),
                dbc.Col([dbc.Label("HDL Cholesterol"), dbc.Input(id="input-hdl", type="number", value=45)], width=4),
                dbc.Col([dbc.Label("LDL Cholesterol"), dbc.Input(id="input-ldl", type="number", value=130)], width=4),
            ]),

            dbc.Row([
                dbc.Col([dbc.Label("Heart Failure History"), dcc.Dropdown(
                    id="input-hf",
                    options=[{"label": "Yes", "value": 1}, {"label": "No", "value": 0}],
                    value=0
                )], width=4),

                dbc.Col([dbc.Label("Current Smoker"), dcc.Dropdown(
                    id="input-smk_cur",
                    options=[{"label": "Yes", "value": 1}, {"label": "No", "value": 0}],
                    value=0
                )], width=4),

                dbc.Col([dbc.Label("Type 1 Diabetes"), dcc.Dropdown(
                    id="input-t1d",
                    options=[{"label": "Yes", "value": 1}, {"label": "No", "value": 0}],
                    value=0
                )], width=4),
            ]),

            dbc.Button("Predict", id="calcular-btn", color="primary", className="mt-3"),
            html.Div(id="prediction-output", className="mt-3"),

            # ✅ Add the graph here
            dcc.Graph(id="prediction-plot", className="mt-3"),

            dcc.Graph(id="prediction-plot-2", className="mt-3"),

            dcc.Graph(id="prediction-plot-3", className="mt-3"),
        ])


    elif tab == "comp":
        return html.Div("Complications content...")

    elif tab == "sever":
        return html.Div("Severity content...")
