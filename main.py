import streamlit as st

# Create a text input element with a default placeholder value
username = st.text_input("Enter your username", value="", max_chars=75, key='username')

# Display the entered value
st.write("Entered value:", username)
