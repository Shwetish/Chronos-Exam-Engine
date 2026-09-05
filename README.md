# Chronos Exam Engine

An AI-powered, end-to-end local application stack that automates balanced assessment paper generation using spaCy NLP concept tagging, dynamic mark optimization algorithms, a FastAPI backend, and an interactive Streamlit dashboard backed by an SQLite database.

---

##  Features

* **NLP Keyword Tagging**: Automatically extracts key subject entities and noun chunks using `spaCy`.
* **Dynamic Mark Allocation**: Programmatically distributes marks across easy (MCQs), medium (Short Answer), and hard (Analytical) sections.
* **Microservice Architecture**: Clean separation of frontend UI (Streamlit) and backend REST API (FastAPI).
* **Database Persistence**: Logs every generated exam paper with timestamps into an SQLite database (`capstone.db`).
* **Interactive Inspection Dashboard**: Allows users to view historical papers and inspect logged database records.
* **Instant Export**: Built-in download widget to export generated papers as `.txt` files.

---

##  Project Stack & Architecture

* **Frontend**: Streamlit (Port 8501)
* **Backend**: FastAPI & Uvicorn (Port 8000)
* **NLP & Processing Engine**: spaCy (`en_core_web_sm`)
* **Database**: SQLite (`capstone.db`)
* **Environment**: Anaconda (Python 3.10)

---

##  Installation & Local Setup

### 1. Prerequisites
Ensured that i have **Anaconda** installed on my system.

### 2. Environment Setup
Opened Anaconda Prompt and created a clean Python 3.10 environment:

```bash
conda create -n capstone_env python=3.10 -y
conda activate capstone_env
