import streamlit as st
import base64
from constant import *

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        
local_css("style/style.css")

st.sidebar.markdown(info['Photo'],unsafe_allow_html=True)

st.title("📝 Resume")

st.write("[Click here if it's blocked by your browser](https://drive.google.com/file/d/1e_trgOgzwYIY6eMSvjmyjgqBcCOdueZ1/view?usp=sharing)")

with open("images/resume.pdf","rb") as f:
      base64_pdf = base64.b64encode(f.read()).decode('utf-8')
      pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="1000mm" height="1000mm" type="application/pdf"></iframe>'
      st.markdown(pdf_display, unsafe_allow_html=True)
        
# -----------------  footer  ----------------- #
footer="""
<div class="footer">
<p>Developed with Streamlit by <a href={} target="_blank">Vicky Kuo</a></p></div>
""".format(foot['url'])
st.markdown(footer,unsafe_allow_html=True)
