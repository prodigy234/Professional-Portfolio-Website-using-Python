import streamlit as st
from components import render, spacer

st.set_page_config(
    page_title="Moses Ihenacho | AI Expert",
    page_icon="🤖",
    layout="wide"
)

# LOAD CSS
with open("assets/styles.css", encoding="utf-8") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# =========================
# SIDEBAR (ELITE VERSION)
# =========================

# PROFILE
st.sidebar.image("assets/ihenacho_image.jpeg", width=120)
st.sidebar.markdown("### Moses Ihenacho")
st.sidebar.caption("AI Product Manager")

st.sidebar.markdown("---")

# DOWNLOAD CV
st.sidebar.markdown("## 📄 Download CV")

# READ FILES AS BYTES (FIXED)
with open("assets/cv/Moses_Ihenacho_CV.pdf", "rb") as f:
    pdf_bytes = f.read()

with open("assets/cv/Moses_Ihenacho_CV.docx", "rb") as f:
    docx_bytes = f.read()

# DOWNLOAD BUTTONS
st.sidebar.download_button(
    label="⬇️ Download PDF",
    data=pdf_bytes,
    file_name="Moses_Ihenacho_CV.pdf",
    mime="application/pdf"
)

st.sidebar.download_button(
    label="⬇️ Download Word",
    data=docx_bytes,
    file_name="Moses_Ihenacho_CV.docx",
    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
)

st.sidebar.markdown("---")

# CONTACT
st.sidebar.markdown("📧 moses.ihenacho@icloud.com")

# =========================
# MAIN PAGE
# =========================

# HERO SECTION
render("""
<div class="hero">
<h1>Moses Ihenacho</h1>
<h3>AI Product Manager • AI Marketing Expert • Machine Learning Strategist</h3>
<p>📍 Austin, Texas | ✉️ moses.ihenacho@icloud.com</p>
</div>
""")

spacer()

# EXECUTIVE SUMMARY
render("""
<div class="card">
<h2>Executive Summary</h2>

<p>
AI Product Manager and AI Marketing Specialist with 7+ years of experience designing and delivering 
AI-powered products across personalization, recommendation systems, conversational AI, and predictive analytics.
</p>

<p>
I specialize in translating complex machine learning capabilities into scalable product solutions that 
drive measurable business outcomes. My work focuses on building intelligent systems that improve customer 
engagement, optimize marketing performance, and enable data-driven decision-making.
</p>

<p>
Experienced in leading cross-functional teams across product, engineering, and data science to define product 
requirements, design experimentation frameworks, and deliver production-ready AI systems supported by model 
evaluation and continuous monitoring.
</p>

<p>
My approach combines strong product strategy with technical fluency in AI and machine learning—ensuring that 
advanced models translate into practical, high-impact business solutions.
</p>

</div>
""")

spacer()

st.info("👉 Use the sidebar to explore About, Experience, Skills, Certifications, and Projects")

# FOOTER
render("""
<div class="footer">
© 2026 Moses Ihenacho • AI Product Leadership
</div>
""")