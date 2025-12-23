import streamlit as st
import requests

API_URL = "http://localhost:8000/api/signup/"

st.title("HR Signup")

# session init
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "email" not in st.session_state:  # FIX
    st.session_state.email = None


# ---------- CLEAN UI ----------
st.markdown("""
<style>

.signup-box {
    width: 450px;
    margin: auto;
}

.signup-box input {
    height: 40px !important;
    font-size: 16px !important;
}

.signup-btn button {
    width: 200px !important;
    margin: auto;
    display: block;
}

</style>
""", unsafe_allow_html=True)


# ---------- FORM ----------
st.markdown("<div class='signup-box'>", unsafe_allow_html=True)

with st.form("signup_form"):
    hr_name = st.text_input("HR Name", placeholder="Enter Name")
    email = st.text_input("Email", placeholder="Enter Email")
    phone = st.text_input("Phone Number", placeholder="Enter Phone")
    company_name = st.text_input("Company Name", placeholder="Enter Company")
    password = st.text_input("Password", type="password", placeholder="Enter Password")

    st.markdown("<div class='signup-btn'>", unsafe_allow_html=True)
    submit = st.form_submit_button("Signup")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)




# ---------- BACKEND CALL ----------
if submit:
    if not hr_name or not email or not phone or not company_name or not password:
        st.error("All fields are required!")
    else:
        data = {
            "hr_name": hr_name,
            "email": email,
            "phone": phone,
            "company_name": company_name,
            "password": password
        }

        response = requests.post(API_URL, json=data)

        if response.status_code == 201:
            st.success("Signup successful! 🎉")

            # Save the session email
            st.session_state.email = email
            st.session_state.logged_in = True

            # Redirect to HR Profile page properly
            st.switch_page("pages/profile.py")

        else:
            try:
                st.error(response.json())
            except:
                st.error("Signup failed!")
