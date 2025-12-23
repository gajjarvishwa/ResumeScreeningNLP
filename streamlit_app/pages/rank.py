import streamlit as st
import requests
import webbrowser
import os

# --- APIs ---
API_EMAIL = "http://127.0.0.1:8000/api/email/send/"
API_SAVE_ACCEPTED = "http://127.0.0.1:8000/api/candidate/save/"

st.title("Top 5 Matched Candidates")

results = st.session_state.get("results", [])

if not results:
    st.error("No results found!")
    st.stop()

# ---------------- TABLE CSS (same as candidate management) ----------------
st.markdown("""
<style>
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
# -------------------------------------------------------------------------


# ---- Table Header ----
h1, h2, h3, h4, h5, h6 = st.columns([2, 1.2, 2, 1.4, 1.2, 1.2])

h1.markdown("<div class='table-header'>Name</div>", unsafe_allow_html=True)
h2.markdown("<div class='table-header'>Score</div>", unsafe_allow_html=True)
h3.markdown("<div class='table-header'>Email</div>", unsafe_allow_html=True)
h4.markdown("<div class='table-header'>Resume</div>", unsafe_allow_html=True)
h5.markdown("<div class='table-header'>Accept</div>", unsafe_allow_html=True)
h6.markdown("<div class='table-header'>Reject</div>", unsafe_allow_html=True)

st.write("")


# ---- Table Rows ----
for idx, r in enumerate(results):

    safe_name = os.path.basename(r["resume_file"]).replace("/", "_").replace(".", "_")
    unique_key = f"{idx}_{safe_name}"

    col1, col2, col3, col4, col5, col6 = st.columns([2, 1.2, 2, 1.4, 1.2, 1.2])

    # NAME
    col1.markdown(f"<div class='table-row'><b>{r['name']}</b></div>", unsafe_allow_html=True)

    # SCORE
    col2.markdown(f"<div class='table-row'><b>{r['score']}%</b></div>", unsafe_allow_html=True)

    # EMAIL
    col3.markdown(f"<div class='table-row'>{r['email']}</div>", unsafe_allow_html=True)

    # VIEW BUTTON
    with col4:
        if st.button("📄 View", key=f"view_{unique_key}"):
            resume_url = f"http://127.0.0.1:8000{r['resume_file']}"
            webbrowser.open_new_tab(resume_url)

    # ACCEPT BUTTON
    with col5:
        if st.button("✔ Accept", key=f"accept_{unique_key}"):

            payload_email = {
                "name": r["name"],
                "email": r["email"],
                "mode": "accept"
            }
            email_res = requests.post(API_EMAIL, json=payload_email)

            payload_save = {
                "name": r["name"],
                "email": r["email"],
                "resume": r["resume_file"],
                "score": r["score"],
            }
            save_res = requests.post(API_SAVE_ACCEPTED, json=payload_save)

            if email_res.status_code == 200:
                st.success(f"Accepted ✓ Email sent to: {r['name']}")
            else:
                st.error("Email sending failed!")

    # REJECT BUTTON
    with col6:
        if st.button("❌ Reject", key=f"reject_{unique_key}"):

            payload = {
                "name": r["name"],
                "email": r["email"],
                "mode": "reject"
            }
            res = requests.post(API_EMAIL, json=payload)

            if res.status_code == 200:
                st.error(f"Rejected ❌ Email sent to: {r['name']}")
            else:
                st.error("Email sending failed!")

    st.markdown("---")
