import streamlit as st
import plotly.express as px
import numpy as np
import pickle
import time
import pandas as pd

st.title('Water Potability Predictor')
cols = st.columns(2)

ph = cols[0].slider("pH of the water", 0.0, 14.0, 7.0)
Hardness = cols[1].slider("Hardness of the water (mg/L)", 0, 500, 100)


Solids = cols[0].slider("Total dissolved solids in the water (ppm)", 0, 50000, 10000)
Chloramines = cols[1].slider("Amount of chloramines in the water (ppm)", 0.0, 11.0, 4.0)


Sulfate = cols[0].slider("Amount of sulfate in the water (mg/L)", 0, 500, 250)
Conductivity = cols[1].slider("Conductivity of the water (μS/cm)", 0, 2000, 800)


Organic_carbon = cols[0].slider("Amount of organic carbon in the water (ppm)", 0.0, 30.0, 10.0)
Trihalomethanes = cols[1].slider("Amount of trihalomethanes in the water (μg/L)", 0.0, 200.0, 80.0)
Turbidity = cols[1].slider("Turbidity of the water (NTU)", 0.0, 10.0, 2.0)

metrics_conv_dict = {
    'ph':1,
    'Hardness':1,
    'Solids':1,
    'Chloramines':1,
    'Sulfate':1,
    'Conductivity':0.55,
    'Organic_carbon':1,
    'Trihalomethanes':0.001,
    'Turbidity':3
    }

data = {
    'ph':ph,
    'Hardness':Hardness,
    'Solids':Solids,
    'Chloramines':Chloramines,
    'Sulfate':Sulfate,
    'Conductivity':Conductivity,
    'Organic_carbon':Organic_carbon,
    'Trihalomethanes':Trihalomethanes,
    'Turbidity':Turbidity
}

def apply_conversion(data, conv_dict):
    for i in data.columns:
        data[i] = data[i] * conv_dict[i]
    return data

model = pickle.load(open('rf_model.pkl', 'rb'))

if st.button("Apply Conversion"):
    df = pd.DataFrame(data.values(), index=data.keys()).T
    converted_data = apply_conversion(df, metrics_conv_dict)
    # st.dataframe(converted_data)

    with st.spinner('Predicting...'):
        time.sleep(4)
        prediction = model.predict(converted_data)
        st.success('Prediction Complete!')

    if prediction == 0:
        st.title(f'Water is not potable')
    else:
        st.title(f'Water is potable')

