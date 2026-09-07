# Chronos Exam Engine ⚡

An AI-powered assessment generation system built with FastAPI, Streamlit, and Google GenAI SDK. Chronos dynamically generates structured academic question papers while analyzing key concepts using spaCy NLP and logging exam metadata locally to ensure academic integrity and prevent paper leaks.

---

## Features

- **Dynamic Exam Generation**: Automatically allocates marks across MCQs, short answers, and long analytical questions.
- **Multilingual Support**: Supports exam paper generation in English and regional scripts (e.g., Marathi).
- **NLP Concept Extraction**: Uses spaCy to process topics and extract domain keywords.
- **Async API Architecture**: Asynchronous FastAPI backend connected to an interactive Streamlit frontend UI.
- **Audit Logging**: Persists assessment logs in an SQLite database (`capstone.db`).
- **Security First**: Utilizes local `.env` isolation to prevent secret credential exposure.

---

## Tech Stack

- **Backend**: FastAPI, Uvicorn
- **Frontend**: Streamlit
- **AI/LLM**: Google GenAI SDK (`gemini-3.6-flash`)
- **NLP & Tools**: spaCy, `python-dotenv`
- **Database**: SQLite

---

## How to Run Locally

Follow these steps to set up and launch the application on your local machine:

### 1. Clone the Repository
```bash
git clone [https://github.com/Shwetish/Real-world-AI-Capstone.git](https://github.com/Shwetish/Real-world-AI-Capstone.git)
cd Real-world-AI-Capstone
2. Configure Environment Variables
Create a .env file in the root project directory and paste your Gemini API key:

Code snippet
GOOGLE_API_KEY=my_actual_api_key_here
3. Install Dependencies
Bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
4. Launch the Application
Terminal 1 — Start FastAPI Backend:

Bash
uvicorn capstone_app:app --reload --port 8000
Terminal 2 — Start Streamlit Frontend:

Bash
streamlit run frontend.py
Access the interactive user interface in your browser at http://localhost:8501.
