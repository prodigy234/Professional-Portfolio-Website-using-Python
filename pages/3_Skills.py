import streamlit as st

st.header("Skills")

skills = ["Machine Learning", "Python", "AI Strategy", "AWS"]

st.markdown("<div class='card'>", unsafe_allow_html=True)

for s in skills:
    st.markdown(f"<span class='skill'>{s}</span>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)