import numpy as np
from dash import Input, Output, State
import dash_bootstrap_components as dbc
from myapp import app
import joblib

model = joblib.load('utils/kaggle_model.pkl')

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