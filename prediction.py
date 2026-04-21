import streamlit as st
import pickle
import pandas as pd
from utils import explain_student, feature_cols, navigation

def show_prediction():

    navigation()

    st.title("Academic Prediction")

    name = st.session_state.get("name", "Student")

    with open("model.pkl", "rb") as f:
        rf = pickle.load(f)

    st.subheader("Fill in your details")

    def bold_radio(label, options, key):
        st.markdown(f"<p style='color:white; font-weight:bold; margin-bottom:4px;'>{label}</p>", unsafe_allow_html=True)
        return st.radio("", options, key=key, label_visibility="collapsed")

    # --- INPUTS ---
    age = st.selectbox("Age", ["18", "19-22", "23-27"])
    age = {"18":1, "19-22":2, "23-27":3}[age]

    sex = st.selectbox("Sex", ["Male", "Female"])
    sex = 0 if sex == "Male" else 1

    school = st.selectbox("High School Type", ["State", "Private", "Other"])
    school = {"State":0, "Private":1, "Other":2}[school]

    scholarship = st.slider("Scholarship (%)", 0, 100, 50) / 100

    additional_work = 1 if bold_radio("Do you have additional work?", ["No", "Yes"], "additional_work") == "Yes" else 0
    sports = 1 if bold_radio("Do you engage in sports?", ["No", "Yes"], "sports") == "Yes" else 0

    transport = st.selectbox("Transportation", ["Bus", "Private"])
    transport = 0 if transport == "Bus" else 1

    study_hours = st.number_input("Weekly Study Hours", 0, 24, 5)

    attendance = st.selectbox("Attendance", ["Never", "Sometimes", "Always"])
    attendance = {"Never":1, "Sometimes":2, "Always":3}[attendance]

    reading = 1 if bold_radio("Do you read regularly?", ["No", "Yes"], "reading") == "Yes" else 0
    notes = 1 if bold_radio("Do you take notes?", ["No", "Yes"], "notes") == "Yes" else 0
    listening = 1 if bold_radio("Do you listen in class?", ["No", "Yes"], "listening") == "Yes" else 0
    project = 1 if bold_radio("Do you complete projects?", ["No", "Yes"], "project") == "Yes" else 0

    # --- PREDICTION ---
    if st.button("Predict"):

        data = [[
            age, sex, school, scholarship,
            additional_work, sports, transport,
            study_hours, attendance, reading,
            notes, listening, project
        ]]

        pred = rf.predict(data)[0]
        prob = rf.predict_proba(data)[0][1]

        result = "Pass" if pred == 1 else "Fail"

        st.success(f"Dear {name}, you are likely to {result}")
        st.write(f"Confidence: {round(prob*100,2)}%")

        sample = pd.Series(data[0], index=feature_cols)
        reasons = explain_student(sample)

        st.subheader("Key Insights")
        st.write(reasons)