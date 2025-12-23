import streamlit as st

st.set_page_config(layout="wide")

# --- PAGE CENTERING USING 3 COLUMNS ---
col1, col2, col3 = st.columns([1, 2, 1])   # center column is bigger

with col2:

    # top spacing
    st.markdown("<div style='height:130px'></div>", unsafe_allow_html=True)

    # TITLE
    st.markdown("""
    <h1 style="
        font-size: 68px;
        font-weight: 900;
        margin-bottom: 5px;
        color: #132440;
        font-family: 'Poppins', sans-serif;
        text-align: center;
    ">
    🚀 Welcome to <span style="color:#E62727;">SkillSort</span>
    </h1>
    """, unsafe_allow_html=True)

    # SUBTEXT
    st.markdown("""
    <p style="
        font-size: 28px;
        color: #6B7280;
        margin-top: -10px;
        text-align: center;
        font-family: 'Poppins', sans-serif;
    ">
    Smart Resume screening & candidate ranking platform.
    </p>
    """, unsafe_allow_html=True)

    st.write("")   # spacing
    st.write("")

    # -------------- BUTTON STYLING --------------
    st.markdown("""
    <style>
        div.stButton > button {
            font-size: 26px !important;      /* ⭐ BIG FONT */
            padding: 16px 15px !important;   /* ⭐ BIG BUTTON */
            background-color: #E62727 !important;
            color: white !important;
            border-radius: 10px !important;
            border: none !important;
        }
        div.stButton > button:hover {
            background-color: #234766 !important;
        }
    </style>
    """, unsafe_allow_html=True)

    # PERFECT CENTER BUTTON
    b1, b2, b3 = st.columns([3, 1, 3])
    with b2:
        go = st.button("Go to Home")

    if go:
        st.switch_page("pages/home.py")










