import streamlit as st
from PIL import Image
from constant import *

st.sidebar.markdown(info['Photo'],unsafe_allow_html=True)

img_1 = Image.open("website-main/images/1.jpg")
img_2 = Image.open("website-main/images/2.png")
img_3 = Image.open("website-main/images/3.png")

st.title("🫶 Hobbies")

col1, col2, col3 = st.columns(3)

with col1:
   st.image(img_1)
   
with col2:
   st.image(img_2)

with col3:
   st.image(img_3)
