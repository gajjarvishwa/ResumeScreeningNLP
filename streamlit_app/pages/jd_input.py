import streamlit as st
import requests

JD_API = "http://localhost:8000/api/jd/create/"
MATCH_API = "http://localhost:8000/api/jd/match/"

st.title("Enter Job Description")

# ---------------- SAME UI AS LOGIN/SIGNUP -----------------
st.markdown("""
<style>

.jd-box {
    width: 550px;      /* center content, slightly wider than login */
    margin: auto;
}

/* smaller input box */
.jd-box input {
    height: 40px !important;
    font-size: 16px !important;
}

/* smaller textarea */
.jd-box textarea {
    height: 160px !important;
    font-size: 16px !important;
}

/* center save button */
.jd-btn button {
    width: 200px !important;
    display: block;
    margin: auto;
}

</style>
""", unsafe_allow_html=True)
# -----------------------------------------------------------


# main wrapper
st.markdown("<div class='jd-box'>", unsafe_allow_html=True)

title = st.text_input("Job Title", placeholder="Enter Job Title")
desc = st.text_area("Paste Job Description Here", placeholder="Paste JD here...")

st.markdown("<div class='jd-btn'>", unsafe_allow_html=True)
submit = st.button("Save JD")
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)


# ---------------- LOGIC (unchanged) -----------------
if submit:
    if not title or not desc:
        st.error("Title and Description required.")
        st.stop()

    # Step 1 → Save JD
    resp = requests.post(JD_API, json={"title": title, "description": desc})

    if resp.status_code == 201:
        jd_id = resp.json().get("jd_id")
        st.session_state["jd_id"] = jd_id

        st.success("JD Saved!")

        # Step 2 → auto match resumes
        match_resp = requests.post(MATCH_API, json={"jd_id": jd_id})

        if match_resp.status_code == 200:
            st.session_state["results"] = match_resp.json().get("top_5")
            st.switch_page("pages/rank.py")
        else:
            st.error("Matching failed.")
    else:
        st.error("JD Save Failed.")
