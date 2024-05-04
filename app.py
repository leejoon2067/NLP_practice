import streamlit as st

st.title("Hello JOON!@@@")

name = st.text_input("이름을 입력해주세요.")
if name != "":
    st.write(f"{name}님! 페이지를 오신 걸 환영합니다!")

st.balloons()