# Real-world-AI-Capstone#Chronos Exam Engine ⚡

An AI-powered assessment generation system built with FastAPI, Streamlit, and Google GenAI SDK. Chronos dynamically generates structured academic question papers while analyzing
key concepts using spaCy NLP and logging exam metadata locally.

## Features

- **Dynamic Exam Generation**: Automatically allocates marks across MCQs, short answers, and long analytical questions.
- **Multilingual Support**: Supports exam paper generation in English and regional scripts (e.g., Marathi).
- **NLP Concept Extraction**: Uses spaCy to process topics and extract domain keywords.
- **Async API Architecture**: Asynchronous FastAPI backend connected to an interactive Streamlit frontend UI.
- **Audit Logging**: Persists assessment logs in an SQLite database (`capstone.db`).

## Tech Stack

- **Backend**: FastAPI, Uvicorn
- **Frontend**: Streamlit
- **AI/LLM**: Google GenAI SDK (`gemini-3.6-flash`)
- **NLP & Tools**: spaCy, `python-dotenv`
- **Database**: SQLite

## Local Setup & Installation

1. **Clone the Repository**
   ```bash
   git clone [https://github.com/Shwetish/Chronos-Exam-Engine.git](https://github.com/Shwetish/Chronos-Exam-Engine.git)
   cd Chronos-Exam-Engine
