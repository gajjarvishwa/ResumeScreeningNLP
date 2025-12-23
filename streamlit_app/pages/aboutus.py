import streamlit as st

st.set_page_config(page_title="About Us — SkillSort", layout="wide")

# ---- TITLE ----
st.title("✨ About SkillSort")
st.caption("Smart hiring. Simple experience.")

st.write("")

# ---- CARD CONTAINER ----
with st.container():
    st.markdown(
        """
        ### 🌟 What We Do
        SkillSort is built to make resume screening faster and easier.  
        With AI scoring and clean UI, we help recruiters shortlist the right candidates without any stress.
        """,
    )

    st.divider()

    st.markdown(
        """
        ### 🎯 Our Focus
        - Clean & simple UI  
        - Accurate AI skill matching  
        - Smooth HR workflow  
        """,
    )

    st.divider()

    st.markdown(
        """
        ### 👩‍💻 Made By
        **Vish** — Developer & Designer  
        Focused on building tools that make hiring feel better.
        """,
    )
