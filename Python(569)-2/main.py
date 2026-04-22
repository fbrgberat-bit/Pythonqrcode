import streamlit as st
import pyqrcode
import png

mail = st.text_input("Gmail Adresiniz: ")
telefon = "905054407855"
link = "https://wa.me/" + telefon + "?text=" + mail

qr = pyqrcode.create(link)
qr.png("Wp.png", scale = 12)

st.image("wp.png")