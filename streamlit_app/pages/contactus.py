
import streamlit as st
import smtplib
from email.message import EmailMessage

st.set_page_config(page_title="Contact Us — SkillSort", layout="wide")

st.title("📩 Contact Us")
st.caption("We're here to help — reach out anytime.")

st.write("")

# ---------------- SAME UI STYLE (CENTERED + SMALL INPUTS) ----------------
st.markdown("""
<style>

.contact-box {
    width: 500px;
    margin: auto;
}

.contact-box input, .contact-box textarea {
    font-size: 16px !important;
    height: 40px !important;
}

/* textarea height */
.contact-box textarea {
    height: 130px !important;
}

/* center send button */
.contact-btn button {
    width: 200px !important;
    margin: auto;
    display: block;
}

</style>
""", unsafe_allow_html=True)
# --------------------------------------------------------------------------


# ---- Form Wrapper ----
st.markdown("<div class='contact-box'>", unsafe_allow_html=True)

with st.form("contact_form"):
    name = st.text_input("Your Name", placeholder="Enter your name")
    email = st.text_input("Your Email", placeholder="Enter your email")
    message = st.text_area("Message", placeholder="Write your message here...")

    st.markdown("<div class='contact-btn'>", unsafe_allow_html=True)
    submitted = st.form_submit_button("Send Message")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)


# ------------------- EMAIL LOGIC (Untouched) -------------------
if submitted:
    if name and email and message:
        try:
            msg = EmailMessage()
            msg["Subject"] = f"New Contact Message from {name}"
            msg["From"] = email
            msg["To"] = "contact.skillsort@gmail.com"

            msg.set_content(f"""
            Name: {name}
            Email: {email}

            Message:
            {message}
            """)

            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.login("gajjarvishwa36@gmail.com", "noge yewf urzb dgdj")
            server.send_message(msg)
            server.quit()

            st.success("Message sent successfully! We'll get back to you soon.")
        except Exception as e:
            st.error(f"Failed to send message ❌ ({e})")
    else:
        st.warning("Please fill all the fields.")
