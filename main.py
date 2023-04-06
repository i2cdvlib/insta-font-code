import streamlit as st

# Define custom CSS style for the text input element
custom_css = """
<style>
.stInput > input {
    padding-left: 25px;
    background-image: url('https://img.icons8.com/material-sharp/24/000000/username.png');
    background-repeat: no-repeat;
    background-position: 5px center;
}
</style>
"""

# Render the custom CSS style using the Streamlit's write() function
st.write(custom_css, unsafe_allow_html=True)

# Create a text input element with a custom class name
username = st.text_input(" ", value="", max_chars=75, key='username', class_='stInput')

# Display the entered value
st.write("Entered value:", username)
