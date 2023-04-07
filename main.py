import streamlit as st

# Set page title
st.set_page_config(page_title="Login Page", page_icon=None, layout="wide")

# Centered image
image_url = "https://www.dafont.com/forum/attach/orig/8/1/815933.png?1"
image_style = f"background-image: url({image_url}); background-size: contain; background-repeat: no-repeat; height: 150px; width: 150px; margin: 0 auto;"
st.markdown(f'<div style="{image_style}"></div>', unsafe_allow_html=True)

# Add text input boxes for phone number, email, and Instagram ID
info = st.text_input("Phone Number, Email, Instagram ID", max_chars=50, key="info", height=30)

# Add password input field
password = st.text_input("Password", type="password", height=30)

# Add login button
login_button_style = "background-color: blue; color: white; padding: 10px; text-align: center; font-size: 18px; border-radius: 5px; width: 150px; margin: 0 auto;"
login_button = st.button("Log In", key="login_button", help="Click to login", style=login_button_style)

# Display a message when login button is clicked
if login_button:
    st.success("Logged in successfully!")
