"""
起動するときはF5ではなく
streamlit run yubaba.py
"""
from sqlalchemy import true
import streamlit as st
import random

name = st.text_input("契約書だよ。そこに名前を書きな。")

# if name != "":
new_name = random.choice(name)
st.write(f"フン。**{name}**というのかい。贅沢な名だねぇ。")
st.write(f"### 今からお前の名前は**{new_name}**だ。")
st.write(f"## いいかい、**{new_name}**だよ。")
st.write(f"# 分かったら返事をするんだ、**{new_name}**!!")

st.write("---")
st.write("<div style='text-align: right;'>制作・著作　Y・B・B</div>", unsafe_allow_html=True)
