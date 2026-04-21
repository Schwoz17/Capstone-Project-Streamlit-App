import streamlit as st

st.set_page_config(layout="wide")

st.markdown("""
<style>

/* App background */
.stApp {
    background-color: #0E1117;
    color: white;
}

/* Force all text to be visible */
html, body, [class*="css"] {
    color: white !important;
}

/* Labels */
label, .stMarkdown, .stText, .stRadio, .stSelectbox {
    color: white !important;
}

/* Input text - white and visible */
input, textarea {
    color: white !important;
    background-color: #1E1E2F !important;
    border: 1px solid #444 !important;
    box-shadow: none !important;
    outline: none !important;
}

/* Input focused - bright white text + border glow */
input:focus, textarea:focus {
    color: white !important;
    background-color: #1E1E2F !important;
    border: 1px solid #00C9A7 !important;
    box-shadow: 0 0 6px #00C9A7 !important;
}

/* Kill ALL borders on every BaseWeb element */
[data-baseweb="input"],
[data-baseweb="base-input"],
[data-baseweb="input"] > div,
[data-baseweb="base-input"] > div,
[data-baseweb="input"] input,
[data-baseweb="base-input"] input {
    border: none !important;
    box-shadow: none !important;
    outline: none !important;
    background-color: #1E1E2F !important;
    color: white !important;
}

/* Streamlit's own input wrapper */
div[class*="stTextInput"] > div,
div[class*="stTextInput"] > div > div,
div[class*="stTextInput"] > div > div > input {
    border: none !important;
    box-shadow: none !important;
    outline: none !important;
    background-color: #1E1E2F !important;
    color: white !important;
}

/* Radio button labels - bold and white */
.stRadio label, .stRadio div[role="radiogroup"] label {
    color: white !important;
    font-weight: bold !important;
    font-size: 15px !important;
}

/* Radio button question text */
.stRadio > label {
    color: white !important;
    font-weight: 600 !important;
}

/* Buttons */
.stButton>button {
    background: linear-gradient(90deg, #00C9A7, #845EC2);
    color: white;
    border-radius: 10px;
    height: 50px;
    font-size: 16px;
    border: none;
}

/* Cards */
.card {
    background-color: #1E1E2F;
    padding: 20px;
    border-radius: 15px;
    margin: 10px 0;
    color: white;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #111827;
    color: white;
}

/* Selectbox text */
[data-baseweb="select"] * {
    color: white !important;
    background-color: #1E1E2F !important;
}

/* Slider label */
.stSlider label {
    color: white !important;
    font-weight: bold !important;
}

/* Number input */
.stNumberInput input {
    color: white !important;
    background-color: #1E1E2F !important;
}

</style>
""", unsafe_allow_html=True)


# SESSION STATE
if "page" not in st.session_state:
    st.session_state.page = "home"

def go_to(page):
    st.session_state.page = page

# HOME PAGE
if st.session_state.page == "home":

    st.title("EduVibe AI")

    # ---------- NOTICE BANNER ----------
    st.markdown("""
        <div style='
            background-color: #1E1E2F;
            border-left: 4px solid #F4A261;
            padding: 12px 16px;
            border-radius: 8px;
            margin-bottom: 20px;
        '>
            <span style='color: #F4A261; font-weight: bold;'>⚠️ Notice: </span>
            <span style='color: #CCCCCC;'>This app is powered by a free-tier AI model. Responses may be limited during usage.</span>
        </div>
    """, unsafe_allow_html=True)

    # Name input with helper text on the right
    col_input, col_hint = st.columns([3, 1])

    with col_input:
        name = st.text_input("Enter your name:", placeholder="e.g. Muiz")

    with col_hint:
        st.markdown("""
            <div style='padding-top: 30px; color: #00C9A7; font-size: 13px;'>
                Your name personalises all AI responses
            </div>
        """, unsafe_allow_html=True)

    st.session_state.name = name

    if name:
        st.write(f"Hi **{name}**, Choose what you want to do:")
    else:
        st.write("Please enter your name to get started.")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Prediction"):
            go_to("prediction")

        if st.button("Career Advisor"):
            go_to("career")

        if st.button("AI File Assistant"):
            go_to("file_ai")

    with col2:
        if st.button("Schedule Planner"):
            go_to("schedule")

        if st.button("Reading Timetable"):
            go_to("timetable")

# IMPORT PAGES
elif st.session_state.page == "prediction":
    from prediction import show_prediction
    show_prediction()

elif st.session_state.page == "career":
    from career import show_career
    show_career()

elif st.session_state.page == "schedule":
    from schedule import show_schedule
    show_schedule()

elif st.session_state.page == "timetable":
    from timetable import show_timetable
    show_timetable()

elif st.session_state.page == "file_ai":
    from pdf_ai import show_pdf_ai
    show_pdf_ai()