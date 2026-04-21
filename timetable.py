import streamlit as st
import google.generativeai as genai
import os
from utils import navigation
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-2.5-flash-lite")

def show_timetable():

    navigation()

    st.title("AI Reading Timetable Generator")

    name = st.session_state.get("name", "Student")

    hours = st.slider("Available reading hours per day", 1, 12, 5)
    subjects = st.text_input("Subjects / Topics (comma separated)")
    days = st.slider("Number of days for the timetable", 1, 14, 7)
    goal = st.text_input("Reading goal (e.g. prepare for exams, finish textbook, revise notes)")

    if st.button("Generate Timetable"):
        with st.spinner("AI is creating your reading timetable..."):

            prompt = f"""
            Student: {name}
            Available reading hours per day: {hours}
            Subjects or topics: {subjects}
            Number of days: {days}
            Reading goal: {goal}

            Create a detailed daily reading timetable for the student.
            - Distribute the subjects evenly across the days.
            - Break each day into reading sessions with specific time slots.
            - Include short breaks between sessions.
            - Keep it realistic, structured, and easy to follow.
            """

            res = model.generate_content(prompt)

            st.subheader(f"{name}'s Reading Timetable")
            st.write(res.text)