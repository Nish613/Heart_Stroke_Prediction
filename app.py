import streamlit as st
import pandas as pd
import joblib

#Unpickling
model = joblib.load('knn_heart.pkl')
scaler = joblib.load('scaler.pkl')
columns = joblib.load('columns.pkl')

st.title("Heart Stroke Prediction")
st.markdown("Project made by Nishtha")
st.markdown("Enter correct details : ")

age = st.number_input("Age", 18, 100, 40)
sex = st.selectbox("Sex", ['M', 'F'])
chest_pain = st.selectbox("Chest Pain Type", ['ATA', 'NAP', 'ASY', 'TA'])
resting_bp = st.number_input("Resting BP(mm Hg)", 80, 200, 120)
cholesterol = st.number_input("Cholesterol (mg/dL)", 100, 600, 200)
fasting_bs = st.selectbox("Fasting Blood sugar > 120mg/dL", [0, 1])
resting_ecg = st.selectbox("Resting ECG", ['Normal', 'ST', 'LVH'])
max_hr = st.number_input("Max heartrate", 60, 220, 150)
exercise_angina = st.selectbox("Exercise induced Angina", ['Y', 'N'])
oldpeak = st.number_input("Oldpeak(ST depression)", 0.0, 6.0, 1.0)
st_slope = st.selectbox("ST Slope", ['Up', 'Flat', 'Down'])

if st.button("Predict"):
    raw_input = {
        'Age': age,
        'Sex': sex,
        'ChestPainType': chest_pain,
        'RestingBP': resting_bp,
        'Cholesterol': cholesterol,
        'FastingBS': fasting_bs,
        'RestingECG': resting_ecg,
        'MaxHR': max_hr,
        'ExerciseAngina': exercise_angina,
        'Oldpeak': oldpeak,
        'ST_Slope': st_slope
    }

    input_df = pd.DataFrame([raw_input])

    input_encoded = pd.get_dummies(input_df)

    input_encoded = input_encoded.reindex(columns=columns, fill_value=0)

    input_scaled = scaler.transform(input_encoded)

    prediction = model.predict(input_scaled)

    if prediction[0] == 1:
        st.error("High chance of heart disease")
    else:
        st.success("Low chance of heart disease")