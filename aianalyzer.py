import streamlit as st

st.title("AI Resume Analyzer")

resume = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

job = st.text_area(
    "Job Description"
)

if st.button("Analyze"):
    st.write("Processing...")