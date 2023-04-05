import streamlit as st

# Add the Instagram font image
st.image('https://i0.wp.com/www.dafontfree.io/wp-content/uploads/2020/12/instagram-new.png?resize=1100%2C750&ssl=1', 
         width=300, 
         output_format='PNG', 
         use_column_width=True)

# Add text boxes for the username and password fields
username = st.text_input("Username")
password = st.text_input("Password", type="password")
