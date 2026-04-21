import streamlit as st
import google.generativeai as genai
import os
from utils import navigation
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-2.5-flash-lite")

def show_schedule():

    navigation()

    st.markdown("""
        <h1 style='text-align:center; color:#00C9A7;'>
        Smart Study Planner
        </h1>
    """, unsafe_allow_html=True)

    name = st.session_state.get("name", "Student")

    # ---------- INSTRUCTION BOX ----------
    st.info("""
    **How to add your tasks:**
    - Enter one task at a time and click **"Add Task"** to build your list.
    - For academic subjects, just type the name (e.g. *Mathematics*, *Biology*).
    - If you include a religious activity like prayer, add your religion in brackets so the AI can schedule it correctly.
      **Example:** `Fajr Prayer (Islam)`, `Morning Devotion (Christianity)`
    - Click **"Remove Last Task"** to undo your last entry, or **"Clear All Tasks"** to start over.
    """)

    # ---------- PLAN TYPE ----------
    st.markdown("<p style='color:white; font-weight:bold; font-size:16px; margin-top:10px;'>What do you want to create?</p>", unsafe_allow_html=True)

    plan_type = st.radio(
        "",
        ["Daily Plan", "Weekly Plan"],
        key="plan_type",
        label_visibility="collapsed",
        horizontal=True
    )

    st.markdown(f"""
        <div style='background-color:#1E1E2F; border-left: 4px solid #00C9A7;
        padding: 10px 15px; border-radius: 8px; margin: 8px 0 16px 0;'>
            <span style='color:#00C9A7; font-weight:bold;'>Selected:</span>
            <span style='color:white;'> {plan_type}</span>
        </div>
    """, unsafe_allow_html=True)

    # ---------- HOURS ----------
    st.markdown("<p style='color:white; font-weight:bold; font-size:15px;'>Available study hours per day</p>", unsafe_allow_html=True)
    hours = st.slider("", 1, 12, 4, label_visibility="collapsed")

    # ---------- TASK STORAGE ----------
    if "planner_tasks" not in st.session_state:
        st.session_state.planner_tasks = []

    # ---------- TASK INPUT ----------
    st.markdown("<p style='color:white; font-weight:bold; font-size:16px; margin-top:10px;'>Add Tasks / Subjects</p>", unsafe_allow_html=True)

    st.markdown("""
        <style>
        div[data-testid="stTextInput"] input {
            background-color: #1E1E2F !important;
            color: white !important;
            border: 1px solid #444 !important;
            border-radius: 8px !important;
            padding: 10px !important;
            font-size: 15px !important;
        }
        div[data-testid="stTextInput"] input:focus {
            border: 1px solid #00C9A7 !important;
            box-shadow: 0 0 6px #00C9A7 !important;
        }
        div[data-testid="stTextInput"] input::placeholder {
            color: #aaaaaa !important;
        }
        </style>
    """, unsafe_allow_html=True)

    task = st.text_input("", placeholder="e.g. Mathematics, Fajr Prayer (Islam)", label_visibility="collapsed")

    col1, col2, col3 = st.columns(3)

    if col1.button("Add Task"):
        if task.strip():
            st.session_state.planner_tasks.append(task.strip())
            st.success(f'"{task.strip()}" added!')
        else:
            st.warning("Please enter a task first.")

    if col2.button("Remove Last"):
        if st.session_state.planner_tasks:
            removed = st.session_state.planner_tasks.pop()
            st.info(f'"{removed}" removed.')
        else:
            st.warning("No tasks to remove.")

    if col3.button("Clear All"):
        st.session_state.planner_tasks = []
        st.info("All tasks cleared.")

    # ---------- TASK LIST ----------
    st.markdown("<p style='color:white; font-weight:bold; font-size:15px; margin-top:12px;'>Your Task List</p>", unsafe_allow_html=True)

    if st.session_state.planner_tasks:
        for i, t in enumerate(st.session_state.planner_tasks, 1):
            st.markdown(f"<p style='color:#00C9A7; margin:2px 0;'><b>{i}.</b> {t}</p>", unsafe_allow_html=True)
    else:
        st.caption("No tasks added yet. Use the input above to get started.")

    st.divider()

    # ---------- GENERATE ----------
    if st.button("Generate Plan"):

        if len(st.session_state.planner_tasks) == 0:
            st.warning("Please add at least one task.")
            return

        with st.spinner("AI is creating your plan..."):

            if plan_type == "Daily Plan":
                prompt = f"""
                Student: {name}
                Tasks: {st.session_state.planner_tasks}
                Available hours: {hours}

                Create a clear and practical DAILY study schedule.
                Include time blocks and short breaks.
                Keep it realistic and easy to follow.
                If any task includes a religion in brackets (e.g. Fajr Prayer (Islam), Morning Devotion (Christianity)),
                schedule it at the most appropriate and culturally accurate time of day for that religion.
                """
            else:
                prompt = f"""
                Student: {name}
                Tasks: {st.session_state.planner_tasks}
                Daily study hours: {hours}

                Create a WEEKLY timetable (Monday–Sunday).
                Distribute tasks evenly across the week.
                Include rest and balance.
                If any task includes a religion in brackets (e.g. Fajr Prayer (Islam), Morning Devotion (Christianity)),
                schedule it at the correct and culturally appropriate time every day.
                """

            response = model.generate_content(prompt)

        st.success(f"Dear {name}, your {plan_type.lower()} is ready!")
        st.markdown(response.text)