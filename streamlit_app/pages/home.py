import streamlit as st



# ---------------- SESSION INIT ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user_email" not in st.session_state:
    st.session_state.user_email = None

st.title("SkillSort — Home Page")


# -------------- FINAL WORKING CSS: ONLY LOGIN & SIGNUP BUTTON COLOR CHANGE --------------
st.markdown("""
<style>

/* LOGIN BUTTON ONLY */
a[href="/pages/login"] > div {
    background-color: #C7DBF4 !important;  /* Light Blue */
    padding: 16px 32px !important;
    border-radius: 12px !important;
}

/* SIGNUP BUTTON ONLY */
a[href="/pages/signup"] > div {
    background-color: #E7CDF9 !important;  /* Light Purple */
    padding: 16px 32px !important;
    border-radius: 12px !important;
}

/* Increase font size for the text inside */
a[href="/pages/login"] span,
a[href="/pages/signup"] span {
    font-size: 26px !important;
}

</style>
""", unsafe_allow_html=True)
# ----------------------------------------------------------------------------------------


if st.session_state.logged_in:
    st.success(f"Logged in as: {st.session_state.user_email}")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.page_link("pages/jd_input.py", label="JD Input", icon="📝")

    with col2:
        st.page_link("pages/upload_resume.py", label="Upload Resume", icon="📤")

    with col3:
        st.page_link("pages/candidate_management.py", label="Candidate Management", icon="👥")

    col4, col5 = st.columns(2)

    with col5:
        st.page_link("pages/interview.py", label="Interview", icon="📅")

    st.markdown("---")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.user_email = None
        st.success("Logged out successfully!")

else:
    st.warning("Please login or signup to continue.")

    col1, col2 = st.columns(2)

    with col1:
        st.page_link("pages/login.py", label="Login", icon="🔐")

    with col2:
        st.page_link("pages/signup.py", label="Signup", icon="🧑‍💼")
