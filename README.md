# EduVibe AI
EduVibe AI is an intelligent student productivity platform that combines Machine Learning and Generative AI to help students improve academic performance, discover career paths, and enhance learning efficiency.

---

## FEATURES

### Academic Performance Prediction
- Predicts whether a student will **Pass or Fail**
- Powered by a **Random Forest model**
- Uses behavioral and academic features such as:
  - Study hours
  - Attendance
  - Reading habits
  - Class engagement

---

### AI Career Advisor
- Generates **personalized career guidance**
- Dynamically adapts based on user responses
- Uses Generative AI for intelligent recommendations

---

### File AI Assistant
Upload files and interact with them using AI.
Supported formats:
- PDF
- TXT
- CSV
- DOCX

Capabilities:
- Summarization
- Question & Answer
- Flashcard Generation

---

### Schedule Planner
- Create personalized daily schedules
- AI-assisted productivity planning

---

### Reading Timetable
- Build structured study plans
- Supports daily and weekly modes

---

## TECH STACK

### Core
- Python
- Streamlit

### Machine Learning
- Scikit-learn (Random Forest, Logistic Regression)

### Data Processing
- Pandas
- NumPy

### Generative AI
- Google Gemini API (Gemini 2.5 Flash)

### File Handling
- PyPDF2 (PDF)
- python-docx (DOCX)
- Pandas (CSV)

---

## UI FEATURES
- Custom dark-themed dashboard
- Responsive layout
- Interactive components

---

## LIMITATIONS
- AI responses depend on API limits (free-tier constraints)
- Large documents are truncated due to token limits
- Dataset size limits prediction accuracy (~65%)

---

## FUTURE IMPROVEMENTS
- RAG-based document understanding
- Chat with uploaded files
- Quiz mode from flashcards
- Downloadable study materials
- Model optimization & feature engineering

---

## INSTALLATION

```bash
git clone https://github.com/Schwoz17/Capstone-Project-Streamlit-App.git
cd your-repo
pip install -r requirements.txt
streamlit run app.py
```

---

## AUTHOR

## Author
**Adeyemi Muiz**

- Data Scientist & AI  
- GitHub: https://github.com/Schwoz17  
- LinkedIn: https://linkedin.com/in/adeyemimuiz
