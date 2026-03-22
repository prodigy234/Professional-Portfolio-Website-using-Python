import streamlit as st

st.header("🎓 Certifications")

col1, col2, col3, col4, col5 = st.columns(5)

certs = [
    ("cert1.jpg", "AI Marketing"),
    ("cert2.jpg", "AML & KYC"),
    ("cert3.jpg", "Anti-Money Laundering"),
    ("cert4.jpeg", "Strategic Alliances"),
    ("cert5.jpg", "AI Digital Marketing")
]

cols = [col1, col2, col3, col4, col5]

for col, (img, title) in zip(cols, certs):
    with col:
        st.image(f"assets/certificates/{img}", use_container_width=True)
        st.caption(title)