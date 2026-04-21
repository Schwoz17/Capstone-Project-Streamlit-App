import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
from utils import navigation

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-2.5-flash-lite")

def show_career():

    navigation()

    st.title("Career Advisor")

    name = st.session_state.get("name", "Student")

    # ---------- BOLD RADIO HELPER ----------
    def bold_radio(label, options, key):
        st.markdown(f"<p style='color:white; font-weight:bold; margin-bottom:4px;'>{label}</p>", unsafe_allow_html=True)
        return st.radio("", options, key=key, label_visibility="collapsed")

    if "questions" not in st.session_state:
        prompt = "Generate 20 Yes/No questions designed to help a student reflect on and narrow down their ideal career path. The questions should cover key areas including: personal strengths and skills, work environment preferences, values and motivations, lifestyle expectations (income, work-life balance, travel), interest in working with people vs. data vs. things, tolerance for risk and entrepreneurship, and passion for specific fields (e.g., arts, science, business, social impact). Each question should be clear, concise, and directly actionable — meaning the student's Yes or No answer meaningfully points them toward or away from certain career types. Do not name the headings just combine the questions together and the heading should be Here are 20 Yes/No questions designed to help a student reflect on and narrow down their ideal career path: without Yes/No under the heading."
        res = model.generate_content(prompt)
        st.session_state.questions = res.text.split("\n")

    answers = []

    for i, q in enumerate(st.session_state.questions):
        q = q.strip()

        if not q or q.startswith("Here are"):
            if q.startswith("Here are"):
                st.markdown(f"<p style='color:white; font-size:16px; font-weight:600; margin-bottom:10px;'>{q}</p>", unsafe_allow_html=True)
            continue

        ans = bold_radio(q, ["No", "Yes"], key=i)
        answers.append(ans)

    if st.button("Analyze"):
        with st.spinner("AI is analyzing your answers..."):
            prompt = f"""
            Student: {name}
            Question answers (in order): {answers}

            Based on the student's Yes/No answers above, suggest career options from MULTIPLE different fields.
            Do NOT give just one career. Instead, provide at least 5 career options spread across different industries such as:
            - Technology & Engineering
            - Business & Finance
            - Arts, Design & Media
            - Science & Healthcare
            - Education & Social Impact
            - Law & Government
            - Trades & Entrepreneurship

            For each career option:
            1. State the career title and field
            2. Explain in 2-3 sentences why it suits this student based on their answers
            3. Give 3 practical tips on how to succeed in that career
            4. Mention the estimated income range and job outlook

            At the end, highlight the TOP recommended career for this student and explain why it stands out above the rest.

            Format each career clearly with headers and spacing so it is easy to read.
            """

            res = model.generate_content(prompt)
            st.write(res.text)