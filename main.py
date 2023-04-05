import streamlit as st

# Add CSS to center the Instagram font image and style the text boxes
st.write(
    """
    <style>
    .center {
        display: flex;
        justify-content: center;
    }
    .small-font {
        font-size: 12px;
    }
    .small-img {
        width: 200px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Add the Instagram font image
st.image('https://i0.wp.com/www.dafontfree.io/wp-content/uploads/2020/12/instagram-new.png?resize=1100%2C750&ssl=1', 
         width=200, 
         output_format='PNG', 
         use_column_width=True,
         style={'width': '200px', 'margin': '0 auto'})

# Add text boxes for the username and password fields
username = st.text_input("Username", value="", max_chars=None, key=None, type='default', 
                         help=None, placeholder='Username', 
                         autocomplete='on', 
                         style={'font-size': '12px'})
password = st.text_input("Password", value="", max_chars=None, key=None, type='password', 
                         help=None, placeholder='Password', 
                         autocomplete='on', 
                         style={'font-size': '12px'})
