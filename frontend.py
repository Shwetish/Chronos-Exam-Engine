import sqlite3
import pandas as pd
import requests
import streamlit as st

st.set_page_config(page_title="Chronos Exam Engine", page_icon="⚡", layout="wide")

# Header section
st.title("⚡ Chronos Exam Engine")
st.caption("AI-Powered Exam Paper Generator & Optimization System")

st.markdown("---")

tab1, tab2 = st.tabs(["📝 Generate Exam", "🗄️ Database Logs (capstone.db)"])

# TAB 1: GENERATION INTERFACE
with tab1:
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### ⚙️ Input Parameters")
        subject = st.text_input("Exam Topic / Subject:", placeholder="e.g., Machine learning")
        total_marks = st.number_input("Total Marks Required:", min_value=10, max_value=100, value=50, step=5)
        generate_btn = st.button("Generate Exam Paper", type="primary", use_container_width=True)

    with col2:
        st.markdown("### 📜 Generated Exam Output")
        if generate_btn:
            if not subject.strip():
                st.warning("Please enter a subject topic before generating.")
            else:
                with st.spinner("Processing spaCy NLP tags & optimizing mark allocations..."):
                    try:
                        response = requests.post(
                            "http://127.0.0.1:8000/generate-exam",
                            json={"subject": subject, "total_marks": total_marks},
                            timeout=60
                        )
                        if response.status_code == 200:
                            data = response.json()
                            exam_text = data["exam_paper"]
                            st.success("Exam paper generated and logged to capstone.db successfully!")
                            st.text_area("Exam Output:", value=exam_text, height=380)
                            
                            # Download button for generated paper
                            file_name = f"{subject.lower().replace(' ', '_')}_exam_paper.txt"
                            st.download_button(
                                label="📥 Download Exam Paper (.txt)",
                                data=exam_text,
                                file_name=file_name,
                                mime="text/plain",
                                use_container_width=True
                            )
                        else:
                            st.error(f"API Error ({response.status_code}): {response.text}")
                    except Exception as e:
                        st.error(f"Could not connect to FastAPI backend: {str(e)}")
        else:
            st.info("Enter subject details on the left and click 'Generate Exam Paper' to view results.")

# TAB 2: DATABASE LOGS
with tab2:
    st.markdown("### 📊 Stored Exam Records (`capstone.db`)")
    try:
        conn = sqlite3.connect("capstone.db")
        
        # Fetch table data safely without hardcoding specific content column names
        df = pd.read_sql_query("SELECT * FROM generated_exams ORDER BY id DESC", conn)
        conn.close()

        if df.empty:
            st.info("No exam records found in the database yet.")
        else:
            # Display general summary metrics
            m1, m2 = st.columns(2)
            m1.metric("Total Generated Exams", len(df))
            m2.metric("Latest Exam Subject", df.iloc[0]["subject"])
            
            st.markdown("---")
            st.dataframe(df, use_container_width=True)
            
            # Interactive viewer for specific log IDs
            st.markdown("#### 🔍 Inspector & Export")
            selected_id = st.selectbox("Select Record ID to Inspect:", df["id"].tolist())
            selected_row = df[df["id"] == selected_id].iloc[0]
            
            # Identify which column holds the text content dynamically
            text_col = [c for c in df.columns if c in ["exam_paper", "generated_paper", "content", "paper_text"] or "paper" in c or "content" in c]
            paper_content = selected_row[text_col[0]] if text_col else str(selected_row.to_dict())
            
            st.text_area("Stored Record Details:", value=str(paper_content), height=300)
            
            # Download button for selected historical exam record
            db_file_name = f"exam_record_{selected_id}_{selected_row['subject'].lower().replace(' ', '_')}.txt"
            st.download_button(
                label="📥 Download Selected Exam Record (.txt)",
                data=str(paper_content),
                file_name=db_file_name,
                mime="text/plain",
                use_container_width=True
            )
            
    except Exception as e:
        st.error(f"Database Query Warning: {str(e)}")