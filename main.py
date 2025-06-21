import streamlit as st
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="AI Interview Assistant", layout="centered")
st.title("🎤 AI Interview Assistant")

job_title = st.text_input("Enter the Job Title:")
job_description = st.text_area("Paste the Job Description:")

if st.button("Generate Questions"):
    if job_title and job_description:
        with st.spinner("Generating interview questions..."):
            prompt = f"""
            You're an expert recruiter. Based on the following job title and description, generate 10 technical and HR interview questions:
            Job Title: {job_title}
            Job Description: {job_description}
            """
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=700
            )
            st.subheader("Generated Questions")
            st.write(response.choices[0].message.content)
    else:
        st.warning("Please provide both the job title and description.")
