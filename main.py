import streamlit as st

# Display a label using st.empty() to create an empty space
label_placeholder = st.empty()

# Create a text input element with a default value
username = st.text_input(" ", value="", max_chars=75, key='username', type='password')

# Update the label with the default text if input is empty
if not username:
    label_placeholder.write("Enter your username")
else:
    label_placeholder.empty()
