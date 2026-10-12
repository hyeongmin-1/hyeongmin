import streamlit as st

# 웹 이름
st.title("오늘의 운세 확인하기")
st.info("오늘은 좋은 날 일 겁니다")

#오늘의 날짜
st.title("★오늘의 날짜")

from datetime import date

today = date.today()
st.subheader(today)
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
        st.success(f"{birthday},조금만 더 수고하여 어려운 고비를 넘기면 마침내 얻을 수 있으니, 
                   인내심으로 참고 견디는 방법이 최선의 길이 될 것이다. 
                   사업가는 금전 융통이 수월할 수 있으니, 
                   투자 가능성이 보이는 길에 용기를 가지고 
                   과감하게 도전할 수 있을 것이다.")



