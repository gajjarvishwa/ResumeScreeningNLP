"""
Shared UI components for SkillSort application
- Global header and footer
- Access control functions
- Sidebar hiding
"""
import streamlit as st

def hide_sidebar():
    """Hide the Streamlit sidebar completely"""
    st.markdown("""
    <style>
    section[data-testid="stSidebar"] {
        display: none !important;
    }
    div[data-testid="collapsedControl"] {
        display: none !important;
    }
    button[data-testid="baseButton-header"] {
        display: none !important;
    }
    </style>
    """, unsafe_allow_html=True)

def render_header():
    """Render the global header with logo and navigation menu"""
    st.markdown("""
    <style>
    .header-container {
        background: linear-gradient(135deg, #132440 0%, #234766 100%);
        padding: 1rem 2rem;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        position: sticky;
        top: 0;
        z-index: 1000;
        margin: -1rem -1rem 2rem -1rem;
    }
    .header-content {
        display: flex;
        justify-content: space-between;
        align-items: center;
        max-width: 1400px;
        margin: 0 auto;
    }
    .logo {
        font-size: 28px;
        font-weight: 900;
        color: white;
        font-family: 'Poppins', sans-serif;
        text-decoration: none;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    .logo span {
        color: #E62727;
    }
    .nav-menu {
        display: flex;
        gap: 1.5rem;
        align-items: center;
        flex-wrap: wrap;
    }
    .nav-link {
        color: white;
        text-decoration: none;
        font-size: 16px;
        font-weight: 500;
        padding: 0.5rem 1rem;
        border-radius: 6px;
        transition: all 0.3s;
        font-family: 'Poppins', sans-serif;
    }
    .nav-link:hover {
        background-color: rgba(255,255,255,0.15);
        transform: translateY(-2px);
    }
    @media (max-width: 768px) {
        .header-content {
            flex-direction: column;
            gap: 1rem;
            padding: 1rem;
        }
        .nav-menu {
            justify-content: center;
            gap: 1rem;
        }
        .nav-link {
            font-size: 14px;
            padding: 0.4rem 0.8rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="header-container">
        <div class="header-content">
            <a href="/" class="logo" style="text-decoration: none;">
                🚀 Skill<span>Sort</span>
            </a>
            <div class="nav-menu">
                <a href="/pages/home" class="nav-link">Home</a>
                <a href="/pages/aboutus" class="nav-link">About Us</a>
                <a href="/pages/contactus" class="nav-link">Contact Us</a>
                <a href="/pages/upload_resume" class="nav-link">Upload Resume</a>
                <a href="/pages/hrprofile" class="nav-link">HR Profile</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_footer():
    """Render the global footer"""
    st.markdown("""
    <style>
    .footer-container {
        background-color: #132440;
        color: white;
        padding: 2.5rem 2rem;
        margin-top: 4rem;
        text-align: center;
        font-family: 'Poppins', sans-serif;
    }
    .footer-content {
        max-width: 1400px;
        margin: 0 auto;
    }
    .footer-logo {
        font-size: 24px;
        font-weight: 700;
        margin-bottom: 1rem;
    }
    .footer-logo span {
        color: #E62727;
    }
    .footer-text {
        color: #9CA3AF;
        font-size: 14px;
        margin: 0.5rem 0;
        line-height: 1.6;
    }
    .footer-divider {
        border-top: 1px solid rgba(255,255,255,0.1);
        margin: 1.5rem 0;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="footer-container">
        <div class="footer-content">
            <div class="footer-logo">
                🚀 Skill<span>Sort</span>
            </div>
            <div class="footer-text">Smart Resume Screening & Candidate Ranking Platform</div>
            <div class="footer-divider"></div>
            <div class="footer-text">© 2024 SkillSort. All rights reserved.</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def check_access():
    """Check if user has access to protected pages"""
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "user_email" not in st.session_state:
        st.session_state.user_email = None
    if "email" not in st.session_state:
        st.session_state.email = None
    
    # Check if user is logged in via either session key
    return st.session_state.logged_in or st.session_state.get("email") or st.session_state.get("user_email")

def require_login():
    """Show login required message and redirect option"""
    st.markdown("""
    <style>
    .access-warning {
        background: linear-gradient(135deg, #FEF3C7 0%, #FDE68A 100%);
        border-left: 4px solid #F59E0B;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 2rem 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    .access-warning h3 {
        color: #92400E;
        margin-bottom: 0.5rem;
        font-family: 'Poppins', sans-serif;
    }
    .access-warning p {
        color: #78350F;
        margin: 0.5rem 0;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="access-warning">
        <h3>⚠️ Authentication Required</h3>
        <p>Please login or signup to access this page.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("Go to Login", use_container_width=True, type="primary"):
            st.switch_page("pages/login.py")

