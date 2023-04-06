import streamlit as st

# Set page title
st.set_page_config(page_title='Instagram Login')

# Page header
st.title('Instagram Login')

# Input fields
username = st.text_input('Username')
password = st.text_input('Password', type='password')

# Login button
if st.button('Login'):
    # Add your authentication logic here
    if username == 'myusername' and password == 'mypassword':
        st.success('Login successful!')
        # Add your post-login logic here
    else:
        st.error('Invalid username or password. Please try again.')
