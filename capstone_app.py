from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
from model import process_and_generate_exam

app = FastAPI(title="Chronos Exam Engine API")

class ExamRequest(BaseModel):
    subject: str
    total_marks: int

@app.post("/generate-exam")
def generate_exam(request: ExamRequest):
    if not request.subject.strip():
        raise HTTPException(status_code=400, detail="Subject topic cannot be empty.")
    
    exam_paper = process_and_generate_exam(request.subject, request.total_marks)
    
    conn = sqlite3.connect('capstone.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO generated_exams (subject, total_marks, questions_json) VALUES (?, ?, ?)",
                   (request.subject, request.total_marks, exam_paper))
    conn.commit()
    conn.close()
    
    return {"status": "success", "exam_paper": exam_paper}

@app.get("/health")
def health_check():
    return {"status": "Chronos Engine Active"}