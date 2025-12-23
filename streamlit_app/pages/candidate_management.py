import streamlit as st
import requests

API_FETCH = "http://127.0.0.1:8000/api/candidate/list/"

st.title("Accepted Candidates")

# Table CSS for clean UI
st.markdown("""
<style>
.table-container {
    width: 100%;
    border-collapse: collapse;
}

.table-header {
    background-color: #EDF2FA;
    padding: 12px;
    font-weight: bold;
    border-bottom: 2px solid #D0D8E8;
    font-size: 18px;
}

.table-row {
    padding: 10px;
    border-bottom: 1px solid #E5E5E5;
    font-size: 16px;
}

.table-row:hover {
    background-color: #F7FAFF;
}
</style>
""", unsafe_allow_html=True)


res = requests.get(API_FETCH)

if res.status_code != 200:
    st.error("Error fetching data")
else:
    data = res.json()

    # Table Header
    col1, col2, col3, col4 = st.columns([2, 3, 2, 2])
    col1.markdown("<div class='table-header'>Name</div>", unsafe_allow_html=True)
    col2.markdown("<div class='table-header'>Email</div>", unsafe_allow_html=True)
    col3.markdown("<div class='table-header'>Resume</div>", unsafe_allow_html=True)
    col4.markdown("<div class='table-header'>Action</div>", unsafe_allow_html=True)

    st.write("")  # small spacing

    # Table Rows
    for idx, c in enumerate(data):

        col1, col2, col3, col4 = st.columns([2, 3, 2, 2])

        col1.markdown(f"<div class='table-row'>{c['name']}</div>", unsafe_allow_html=True)
        col2.markdown(f"<div class='table-row'>{c['email']}</div>", unsafe_allow_html=True)
        col3.markdown(
            f"<div class='table-row'><a href='http://127.0.0.1:8000{c['resume_file']}' target='_blank'>View Resume</a></div>",
            unsafe_allow_html=True
        )

        # Action button stays the same
        if col4.button("Schedule Interview", key=f"int_{idx}_{c['email']}"):
            st.session_state["interview_email"] = c["email"]
            st.session_state["interview_name"] = c["name"]
            st.switch_page("pages/interview.py")
