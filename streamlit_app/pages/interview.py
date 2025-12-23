import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/api/interview/schedule/"

st.set_page_config(page_title="Interview", layout="wide")

st.title("Schedule Interview")

candidate_name = st.session_state.get("interview_name", "")
candidate_email = st.session_state.get("interview_email", "")

st.write(f"Candidate: **{candidate_name}**")
st.write(f"Email: {candidate_email}")

date = st.date_input("Pick Interview Date")
time = st.time_input("Pick Interview Time")

venue = st.text_input("Interview Venue", placeholder="Office / Google Meet Link")
mode = st.selectbox("Interview Mode", ["Online", "Offline"])

if st.button("Send Interview Invite"):
    payload = {
        "candidate_name": candidate_name,
        "candidate_email": candidate_email,
        "date": str(date),
        "time": str(time),
        "venue": venue,
        "mode": mode
    }

    res = requests.post(API_URL, json=payload)

    if res.status_code == 200:
        st.success("Interview Scheduled & Email Sent!")
    else:
        st.error("Something went wrong!")
