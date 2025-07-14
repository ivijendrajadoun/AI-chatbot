import streamlit as st
from prompts import gather_info_prompt
from llm_utils import get_technical_questions

st.set_page_config(page_title="TalentScout Hiring Assistant")

st.title("🤖 TalentScout Hiring Assistant")
st.write("Welcome! I’m here to guide you through your application process. Please enter your details below.")

if 'user_info' not in st.session_state:
    st.session_state.user_info = {}

with st.form("candidate_info"):
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    phone = st.text_input("Phone Number")
    experience = st.number_input("Years of Experience", min_value=0, step=1)
    position = st.text_input("Desired Position(s)")
    location = st.text_input("Current Location")
    tech_stack = st.text_area("List your tech stack (e.g., Python, React, PostgreSQL)")

    submitted = st.form_submit_button("Submit")

if submitted:
    st.session_state.user_info = {
        "name": name,
        "email": email,
        "phone": phone,
        "experience": experience,
        "position": position,
        "location": location,
        "tech_stack": tech_stack
    }
    
    st.success("Information submitted. Generating technical questions...")
    
    questions = get_technical_questions(st.session_state.user_info)
    
    st.markdown("###Tailored Technical Questions")
    st.write(questions)

# Graceful conversation exit
user_input = st.text_input("Type 'exit' to end the conversation")

if user_input.lower() in ["exit", "quit", "bye"]:
    st.write("Thank you for your time! We will get back to you soon.")
