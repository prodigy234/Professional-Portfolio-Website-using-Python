import streamlit as st
from components import render, spacer

st.header("About")

col1, col2 = st.columns([1, 2])

with col1:
    st.image("assets/ihenacho_image.jpeg", width=220)

with col2:
    render("""
    <div class="card">

    <h3>Moses Ihenacho</h3>

    <p>
    AI Product Manager specializing in machine learning and generative AI products, with over seven years 
    of experience building intelligent systems that power personalization, recommendation engines, 
    conversational AI, and fraud detection solutions.
    </p>

    <p>
    I lead end-to-end product development for AI-driven platforms—working closely with engineering and data 
    science teams to define product requirements, evaluate model performance, and guide technical trade-offs.
    </p>

    </div>
    """)

spacer()

# IMPACT SECTION
render("""
<div class="card">

<h3>🚀 Selected Impact</h3>

<ul>
<li>Scaled a conversational AI platform to handle 40% of customer inquiries, generating $800K in annual cost savings</li>
<li>Improved recommendation system performance, increasing CTR by 22% and session duration by 3.2 minutes</li>
<li>Drove product adoption from 0 to 50K+ monthly active users within six months</li>
<li>Launched fraud detection models achieving 95% accuracy and reducing false positives by over 60%</li>
<li>Reduced ML inference latency by 45% through infrastructure and model optimization</li>
</ul>

</div>
""")

spacer()

# INTERESTS / FOCUS
render("""
<div class="card">

<h3>🧠 Focus Areas</h3>

<p>
ML platform development, model lifecycle management, LLM-powered applications, and responsible AI.
I enjoy working in ambiguous environments and translating complex machine learning concepts into 
clear, high-impact product decisions.
</p>

</div>
""")