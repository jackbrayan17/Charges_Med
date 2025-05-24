import numpy as np
import streamlit as st
import pickle
import time

with open('reg.pkl','rb') as file:
    model = pickle.load(file)

st.set_page_config(page_title="Predicteur de charge medicales", page_icon="", layout="centered")
st.title("💰Prediction des charges medicales")
st.markdown("Remplis les informations ci-dessous")

with st.spinner("Chargement du modele "):
    time.sleep(1)

col1, col2, = st.columns(2)
with col1:
    age = st.slider("Age",18,100,25)
with col2: 
    sex = st.selectbox('Sexe',['Male','Female'])

col3,col4 = st.columns(2)
with col3: 
    bmi = st.number_input("Indice Masse Corporelle",10.0,50.0,25.0)
with col4:
    children = st.slider("Nombre d'enfants", 0, 5, 1)

col5,col6 = st.columns(2)
with col5: 
    smoker = st.selectbox("Fumeur : ", ['Oui', 'Non'])
with col6:
    region = st.selectbox("Region : ", ['southwest', 'southeast', 'northwest', 'northeast'])

# Encodage
sex_encoded = 1 if sex == 'Male' else 0
smoker_encoded = 1 if smoker == 'Yes' else 0
reg_dict = {
    'southwest':0.2430,
    'southeast':0.2722,
    'northwest':0.2423,
    'northeast':0.2722
}

region_encoded = reg_dict[region]

input_data = [[age, sex_encoded, bmi, children, smoker_encoded, region_encoded]]

if st.button("💰Predire les charges"):
    with st.spinner("Calcul en cours ..."):
        prediction = model.predict(input_data)[0]
        time.sleep(1)
    st.success("Prediction terminee")
    st.markdown(f"💰 Charges medicales estimees : **{prediction:,.2f}**")
    st.balloons()