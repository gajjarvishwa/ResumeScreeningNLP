
import requests
import streamlit as st

API_URL = "http://localhost:8000/api/login/"

# ---------- SMALL INPUT FIELD + CENTERED FORM CSS ----------
st.markdown("""
<style>

.login-box {
    width: 450px;               /* input width fixed */
    margin: auto;               /* center align */
}

.login-input input {
    height: 40px !important;    /* smaller height */
    font-size: 16px !important;
}

.login-button button {
    width: 200px !important;
    margin: auto;
    display: block;
}

</style>
""", unsafe_allow_html=True)
# -----------------------------------------------------------


st.markdown("<div class='login-box'>", unsafe_allow_html=True)

email = st.text_input("Email", key="email", help="", placeholder="Enter Email", label_visibility="visible")
password = st.text_input("Password", type="password", key="password", placeholder="Enter Password")

# Centered Login Button
if st.button("Login"):
    response = requests.post(API_URL, json={"email": email, "password": password})

    if response.status_code == 200:
        st.session_state.logged_in = True
        st.session_state.user_email = email
        st.success("Login success!")
        st.switch_page("pages/home.py")
    else:
        st.error("Invalid email or password")

st.markdown("</div>", unsafe_allow_html=True)
