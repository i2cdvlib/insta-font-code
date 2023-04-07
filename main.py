import streamlit as st

# Set page title
st.set_page_config(page_title="Login Page", page_icon=None, layout="wide")

# Load and display image
image_url = "https://www.dafont.com/forum/attach/orig/8/1/815933.png?1"
image_style = f"background-image: url({image_url}); background-size: contain; background-repeat: no-repeat; height: 250px;"
st.markdown(f'<div style="{image_style}"></div>', unsafe_allow_html=True)

# Add text inputs for phone number, email, and Instagram ID
phone_number = st.text_input("Phone Number")
email = st.text_input("Email")
instagram_id = st.text_input("Instagram ID")

# Add password input field
password = st.text_input("Password", type="password")

# Add login button
login_button_style = "background-color: blue; color: white; padding: 10px; text-align: center; font-size: 18px; border-radius: 5px;"
login_button_text = '<span style="display:inline-block;vertical-align:middle">Log In</span>'
login_button = st.button(login_button_text, key="login_button", help="Click to login", unsafe_allow_html=True, style=login_button_style)

# Display a message when login button is clicked
if login_button:
    st.success("Logged in successfully!")
