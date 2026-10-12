import streamlit as st

# 웹 이름
st.title("오늘의 운세 확인하기")
st.info("오늘은 좋은 날 일 겁니다")

#대길 대흉

col1, col2 , col3 = st.columns(3)
with col1:    
    st.write("2026/10/12")
with col2:    
    st.write("대길")
    st.write("토끼띠")
    st.write("소띠")
    st.write("말띠")
with col3:    
    st.write("대흉")
    st.write("용띠")
    st.write("쥐띠")
    st.write("뱀띠")

with st.container(border=True):
    st.write(st.columns{3})
#나의 운세 확인하기

st.title ("당신의 운세")

#생년월일 입력

birthday = st.text_input("생년월일을 입력하세요")

if st.button("확인하기"):
    if birthday:
        st.success(f"{birthday}")



