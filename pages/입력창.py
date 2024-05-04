import streamlit as st
import random

# 입력창 만들기 practice

# title
st.title("여러 가지 입력창")

# reset button
st.button("리셋 버튼", type = "primary")
if st.button("랜덤 숫자 생성"):
    st.write(random.random())
else:
    st.write("Goodbye")

# download button
text_contents = """This is some Text"""
st.download_button('Download some text', text_contents)

# link button
st.link_button("Go to gallery", "https://streamlit.io/gallery")

# checkbox button
agree = st.checkbox('동의하십니까')
if agree:
    st.write("Great!")
else:
    st.write("동의 버튼을 눌러주세요!")

# multiselect button
options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'])
st.write("You selected: ", options)

