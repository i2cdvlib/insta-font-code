import streamlit as st

# Render the label using Markdown with HTML
st.markdown('<label for="username">Enter username:</label>', unsafe_allow_html=True)

# Create a text input element
username = st.text_input("", value="", max_chars=75, key='username')

# Display the entered value
st.write("Entered value:", username)
