import streamlit as st
import pandas as pd

# ---------------- NAVIGATION ----------------
def navigation():
    st.sidebar.title("Navigate")

    if st.sidebar.button("Home"):
        st.session_state.page = "home"

    if st.sidebar.button("Prediction"):
        st.session_state.page = "prediction"

    if st.sidebar.button("Career"):
        st.session_state.page = "career"

    if st.sidebar.button("Schedule"):
        st.session_state.page = "schedule"

    if st.sidebar.button("Timetable"):
        st.session_state.page = "timetable"
    
    if st.sidebar.button("AI File Assistant"):
        st.session_state.page = "pdf_ai"



# ---------------- FEATURE COLUMNS ----------------
feature_cols = [
    'Student_Age','Sex','High_School_Type','Scholarship',
    'Additional_Work','Sports_activity','Transportation',
    'Weekly_Study_Hours','Attendance','Reading','Notes',
    'Listening_in_Class','Project_work'
]

# ---------------- EXPLAIN STUDENT ----------------
def explain_student(student):

    reasons = []

    if student["Attendance"] <= 1:
        reasons.append("Low attendance reduces learning consistency")

    if student["Weekly_Study_Hours"] < 2:
        reasons.append("Insufficient study time")

    if student["Reading"] == 0:
        reasons.append("Weak reading habit affects understanding")

    if student["Listening_in_Class"] == 0:
        reasons.append("Low classroom engagement")

    if student["Project_work"] == 0:
        reasons.append("Lack of practical/project experience")

    if len(reasons) == 0:
        reasons.append("Good academic habits observed")

    return reasons