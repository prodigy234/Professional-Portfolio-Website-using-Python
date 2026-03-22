import streamlit as st

def render(html):
    st.markdown(html, unsafe_allow_html=True)

def section(title):
    st.markdown(f"## {title}")

def spacer():
    st.markdown("<br>", unsafe_allow_html=True)