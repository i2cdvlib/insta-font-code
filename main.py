import streamlit as st

# Define the HTML code
html_code = '''
<div style="background-color: #F8D7DA; padding: 20px; border-radius: 10px;">
    <h1 style="color: #721C24; text-align: center;">Welcome to my Streamlit app!</h1>
    <p style="color: #721C24; text-align: center;">Here's some text that I've styled using HTML and CSS.</p>
</div>
'''

# Define the CSS code
css_code = '''
body {
    font-family: Arial, sans-serif;
    background-color: #F0F2F6;
    padding: 20px;
}

h1 {
    font-size: 36px;
    text-align: center;
}

p {
    font-size: 24px;
    text-align: center;
}
'''

# Render the HTML and CSS in Streamlit
st.markdown(html_code, unsafe_allow_html=True)
st.write('')
st.markdown(f'<style>{css_code}</style>', unsafe_allow_html=True)

# Add some Streamlit elements below the HTML and CSS
st.write('Here are some Streamlit elements:')
st.slider('Select a value', 0, 10, 5)
st.button('Click me')
