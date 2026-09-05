import streamlit as st
import requests
import pandas as pd
import sqlite3

st.set_page_config(page_title="Chronos Exam Engine", page_icon="⚡", layout="wide")

st.title("⚡ Chronos Exam Engine")
st.caption("AI-Powered Exam Paper Generator & Optimization System")

tab1, tab2 = st.tabs(["📝 Generate Exam", "📊 Database Logs (capstone.db)"])

API_URL = "http://127.0.0.1:8000"

with tab1:
    col1, col2 = st.columns([1, 1.2])
    
    with col1:
        st.subheader("⚙️ Input Parameters")
        topic_input = st.text_input("Exam Topic / Subject:", value="Mathematics")
        marks_input = st.number_input("Total Marks Required:", min_value=10, max_value=100, value=50, step=5)
        generate_btn = st.button("Generate Exam Paper", type="primary", use_container_width=True)

    with col2:
        st.subheader("📜 Generated Exam Output")
        if generate_btn:
            if not topic_input.strip():
                st.warning("Please enter a valid subject or topic.")
            else:
                with st.spinner("Processing NLP tags and generating exam paper..."):
                    try:
                        response = requests.post(
                            f"{API_URL}/generate-exam",
                            json={"topic": topic_input, "total_marks": marks_input},
                            timeout=60
                        )
                        if response.status_code == 200:
                            exam_data = response.json()["exam_paper"]
                            st.success("Exam paper generated and logged to capstone.db successfully!")
                            st.text_area("Exam Output:", value=exam_data, height=450)
                            st.download_button(
                                label="📥 Download Exam Paper (.txt)",
                                data=exam_data,
                                file_name=f"{topic_input.replace(' ', '_')}_Exam_Paper.txt",
                                mime="text/plain"
                            )
                        else:
                            st.error(f"Backend API Error [{response.status_code}]: {response.text}")
                    except requests.exceptions.ConnectionError:
                        st.error("Could not connect to FastAPI backend on port 8000. Please make sure Uvicorn is running in Terminal 1.")
                    except Exception as e:
                        st.error(f"Unexpected error: {str(e)}")

with tab2:
    st.subheader("📊 Historical Database Entries")
    try:
        conn = sqlite3.connect("capstone.db")
        df = pd.read_sql_query("SELECT * FROM exam_logs ORDER BY id DESC", conn)
        conn.close()
        st.dataframe(df, use_container_width=True)
    except Exception:
        st.info("No database entries found yet or database table initializing.")