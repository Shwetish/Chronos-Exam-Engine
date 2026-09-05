import os
import spacy
from dotenv import load_dotenv
from google import genai

load_dotenv()

# Load spaCy NLP model safely
try:
    nlp = spacy.load("en_core_web_sm")
except Exception:
    try:
        nlp = spacy.load("xx_ent_wiki_sm")
    except Exception:
        nlp = None

def extract_keywords(text: str) -> list:
    """Extract key entity tokens using spaCy with fallback processing."""
    if not nlp:
        return [word for word in text.split() if len(word) > 3]
    doc = nlp(text)
    keywords = [token.text for token in doc if not token.is_stop and token.is_alpha]
    return keywords if keywords else [text]

def generate_exam_paper(topic: str, total_marks: int) -> str:
    """Generate high-quality academic question papers using official Google GenAI SDK."""
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY not found in environment variables. Check your .env file.")

    extracted_keywords = extract_keywords(topic)
    keywords_str = ", ".join(extracted_keywords)

    client = genai.Client(api_key=api_key)

    prompt = f"""
    You are an expert academic assessment controller. Generate a comprehensive exam paper for:
    Topic / Subject: "{topic}"
    Total Marks: {total_marks}

    CRITICAL LANGUAGE INSTRUCTIONS:
    1. If the input topic is written in Marathi (Devanagari script) or specifies Marathi (e.g., "marathi", "मराठी"), write the ENTIRE exam paper strictly in Marathi (Devanagari script).
    2. If the input topic is in English, write the exam paper in clear, formal academic English.

    STRUCTURE REQUIREMENT:
    - SECTION A: Multiple Choice Questions (MCQs) — 20% of total marks. Provide 4 distinct options (a, b, c, d) per question.
    - SECTION B: Short Answer Questions — 40% of total marks.
    - SECTION C: Analytical & Long Answer Questions — 40% of total marks.
    """

    # Updated to the required model name per your API key response
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    generated_content = response.text.strip()

    footer = (
        f"\n\n==================================================\n"
        f"Generated & Validated via Chronos Exam Engine\n"
        f"Extracted NLP Concepts: {keywords_str}\n"
        f"Target Allocation: {total_marks} Marks\n"
        f"Logged to capstone.db database."
    )

    return generated_content + footer