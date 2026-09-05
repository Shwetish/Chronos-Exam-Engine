from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from model import generate_exam_paper
from Database import log_exam_to_db

app = FastAPI(title="Chronos Exam Engine API")

class ExamRequest(BaseModel):
    topic: str
    total_marks: int = 50

@app.get("/")
def read_root():
    return {"status": "Online", "service": "Chronos Exam Engine REST API"}

@app.post("/generate-exam")
def generate_exam_endpoint(request: ExamRequest):
    if not request.topic.strip():
        raise HTTPException(status_code=400, detail="Topic field cannot be empty.")
    
    try:
        paper_text = generate_exam_paper(request.topic, request.total_marks)
        log_exam_to_db(request.topic, request.total_marks, paper_text)
        return {"status": "success", "exam_paper": paper_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))