import streamlit as st
import requests


import streamlit as st

st.set_page_config(
    page_title="SkillSort — Resume Upload",
    layout="wide",
    initial_sidebar_state="collapsed"
)

#👇 Hide sidebar completely
hide_sidebar_style = """
    <style>
        section[data-testid="stSidebar"] {
            display: none !important;
        }
        div[data-testid="collapsedControl"] {
            display: none !important;
        }
    </style>
"""
st.markdown(hide_sidebar_style, unsafe_allow_html=True)









st.set_page_config(page_title='SkillSort — Resume Upload', layout='wide')
st.title('SkillSort — Resume Upload')

API_UPLOAD = "http://localhost:8000/api/upload/"

st.header("Upload Resume")

with st.form("upload_form"):
    department = st.text_input("Department")
    uploaded_file = st.file_uploader("Upload Resume (PDF/DOCX)", type=["pdf", "docx"])
    submit = st.form_submit_button("Upload")

if submit:
    if not department or not uploaded_file:
        st.error("Department + Resume file required!")
    else:
        files = {"resume_file": (uploaded_file.name, uploaded_file.getvalue())}
        data = {"department": department}

        try:
            with st.spinner("Uploading..."):
                resp = requests.post(API_UPLOAD, data=data, files=files)

            if resp.status_code == 201:
                st.success("✨ Resume uploaded successfully!")
            else:
                st.error(f"Upload failed ({resp.status_code})")
                st.write(resp.text)

        except Exception as e:
            st.error("Backend error")
            st.exception(e)
