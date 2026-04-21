import streamlit as st
import PyPDF2
import google.generativeai as genai
import os
from dotenv import load_dotenv
import docx
import pandas as pd
from utils import navigation

# ---------- LOAD ENV ----------
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemini-2.5-flash-lite")

# ---------- FILE READER FUNCTION ----------
def extract_text(uploaded_file):

    file_type = uploaded_file.name.split(".")[-1]

    text = ""

    # PDF
    if file_type == "pdf":
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        for page in pdf_reader.pages:
            if page.extract_text():
                text += page.extract_text()

    # TXT
    elif file_type == "txt":
        text = uploaded_file.read().decode("utf-8")

    # CSV
    elif file_type == "csv":
        df = pd.read_csv(uploaded_file)
        text = df.to_string()

    # DOCX
    elif file_type == "docx":
        doc = docx.Document(uploaded_file)
        for para in doc.paragraphs:
            text += para.text + "\n"

    else:
        return None

    return text


def show_pdf_ai():

    navigation()

    # ---------- HEADER ----------
    st.title("EduVibe AI - File Assistant")

    st.warning("Max file size: 5MB due to the low AI model employed | Supported: PDF, TXT, CSV, DOCX")

    # ---------- UPLOAD ----------
    uploaded_file = st.file_uploader(
        "Upload your file",
        type=["pdf", "txt", "csv", "docx"]
    )

    if uploaded_file is not None:

        text = extract_text(uploaded_file)

        if not text:
            st.error("Could not extract text from file.")
            return

        st.success("File loaded successfully!")

        # ---------- ACTION ----------
        action = st.selectbox(
            "What do you want to do?",
            ["Summarize", "Ask Question", "Generate Flashcards"]
        )

        with st.spinner("AI is creating your plan..."):
            # ---------- SUMMARIZE ----------
            if action == "Summarize":

                if st.button("Generate Summary"):

                    prompt = f"""
                    Summarize this content in bullet points.

                    Content:
                    {text[:4000]}
                    """

                    res = model.generate_content(prompt)

                    st.write("### Summary")
                    st.write(res.text)

            # ---------- Q&A ----------
            elif action == "Ask Question":

                question = st.text_input("Enter your question")

                if st.button("Get Answer"):

                    prompt = f"""
                    Content:
                    {text[:4000]}

                    Question:
                    {question}

                    Answer clearly.
                    """

                    res = model.generate_content(prompt)

                    st.write("### Answer")
                    st.write(res.text)

            # ---------- FLASHCARDS ----------
            elif action == "Generate Flashcards":

                if st.button("Create Flashcards"):

                    prompt = f"""
                    Generate 10 flashcards.

                    Format:
                    Q: ...
                    A: ...

                    Content:
                    {text[:4000]}
                    """

                    res = model.generate_content(prompt)

                    st.write("###Flashcards")

                    flashcards = res.text.split("Q:")

                    for i, card in enumerate(flashcards[1:]):

                        parts = card.split("A:")

                        if len(parts) == 2:
                            q = parts[0].strip()
                            a = parts[1].strip()

                            with st.expander(f"Flashcard {i+1}: {q}"):
                                st.write(a)