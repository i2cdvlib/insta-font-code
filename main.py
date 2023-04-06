import streamlit as st

# Define the HTML code for the text box
html_code = '''
<input aria-label="Phone number, username, or email" aria-required="true" autocapitalize="off" autocorrect="off" maxlength="75" name="username" type="text" class="_aa4b _add6 _ac4d" value="">
'''

# Display the HTML code in Streamlit
st.write(html_code, unsafe_allow_html=True)
