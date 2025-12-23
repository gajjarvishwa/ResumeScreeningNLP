import streamlit as st
import requests

st.set_page_config(page_title="HR Profile", layout="wide")

st.title("👤 HR Profile")

# ------------------------------
# EMAIL MUST COME FROM SESSION
# ------------------------------
email = st.session_state.get("email")

if not email:
    st.error("You must login or signup first!")
    st.stop()

API_URL = "http://127.0.0.1:8000/api/hrprofile/profile/"

# ------------------------------
# Load HR profile data
# ------------------------------
response = requests.get(API_URL, params={"email": email})

if response.status_code != 200:
    st.error("Failed to load HR profile")
    st.stop()

profile = response.json()

col1, col2 = st.columns(2)

with col1:
    hr_name = st.text_input("HR Name", profile.get("hr_name", ""))
    phone = st.text_input("Phone Number", profile.get("phone", ""))

with col2:
    company = st.text_input("Company Name", profile.get("company_name", ""))
    st.text_input("Email (Read Only)", email, disabled=True)

st.write("---")

if st.button("Update Profile", use_container_width=True):
    updated = {
        "email": email,
        "hr_name": hr_name,
        "phone": phone,
        "company_name": company
    }

    upd = requests.put(API_URL, json=updated)

    if upd.status_code == 200:
        st.success("Profile updated!")
    else:
        st.error("Update failed.")