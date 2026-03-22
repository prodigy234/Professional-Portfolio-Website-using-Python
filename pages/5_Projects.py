import streamlit as st
from components import render, spacer

st.header(" Projects & Systems")

# -----------------------------
# DATA SCIENCE & AI PROJECTS
# -----------------------------
st.subheader(" Data Science & AI Projects")

projects = {
    "Jumia AI Supply Chain Intelligence": "https://jumia-inspired-ai-iot-supply-chain.onrender.com/"
}

col1, col2 = st.columns(2)

project_items = list(projects.items())

with col1:
    for name, link in project_items[::2]:
        st.markdown(
            f" <a href='{link}' target='_blank' style='color:#60a5fa; text-decoration:none;'><b>{name}</b></a>",
            unsafe_allow_html=True
        )

with col2:
    for name, link in project_items[1::2]:
        st.markdown(
            f" <a href='{link}' target='_blank' style='color:#60a5fa; text-decoration:none;'><b>{name}</b></a>",
            unsafe_allow_html=True
        )

spacer()

# -----------------------------
# MARKETING & PRODUCT ANALYTICS
# -----------------------------
st.subheader(" Marketing & Product Analytics")

marketing_projects = {
    "Access Bank AI Customer Service": "https://ifoodanalytics.streamlit.app/"
}

render("<div class='card'>")

for name, link in marketing_projects.items():
    st.markdown(
        f" <a href='{link}' target='_blank' style='color:#60a5fa; text-decoration:none;'><b>{name}</b></a>",
        unsafe_allow_html=True
    )

render("</div>")