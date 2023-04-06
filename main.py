import streamlit as st

# Display HTML with label inside text input
st.markdown('<input aria-label="Phone number, username, or email">', unsafe_allow_html=True)
username = st.text_input("", value="", max_chars=75, key='username')
