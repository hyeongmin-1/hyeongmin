import streamlit as st

# 웹 이름
st.title("오늘의 운세 확인하기")
st.info("오늘은 좋은 날 일 겁니다")

#오늘의 날짜
st.title("오늘의 날짜")

from datetime import date

today = date.today()
st.text(today)
#대길 대흉

col1, col2 , col3 ,col4 = st.columns(4)
with col1:    
    st.subheader("대길")
    st.subheader("대흉")
with col2:    
    st.subheader("토끼띠")
    st.subheader("개띠")   
with col3:        
    st.subheader("돼지띠")
    st.subheader("뱀띠")
with col4:
    st.subheader("말띠")
    st.subheader("쥐띠")

#나의 운세 확인하기

st.title ("당신의 운세")

#생년월일 입력

birthday = st.text_input("생년월일을 입력하세요")

if st.button("확인하기"):
    if birthday:
        st.success(f"{birthday}")



