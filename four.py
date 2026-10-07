import streamlit as st

st.title("◈ 나의 첫 웹앱")
st.info("파이썬만으로 제작하는 UI")

col1, col2 = st.columns(2)
with col1:
    st.success("왼쪽 영역")
with col2:
    st.write("오른쪽 영역")

# 새로고침 시 데이터 유지
if "user_list" not in st.session_state:
    st.session_state.user_list = []

with st.form("input_form"):
    name = st.text_input("이름")
    if st.form_submit_button("등록") and name :
        st.session_state.user_list.append(name)

import streamlit as st

tasks = [
    "1.  API 스펙 문서 작성",
    "2. 프론트엔드 컴포넌트 개발",
    "3. 배포 파이프라인(CI/CD) 구축"

]

st.subheader("※ 금일 할 일 목록")

for task in tasks:
    # border = Ture를 주면 각 반복 요소가 단정한 상자로 감싸진다.
    
    with st.container(border=True):
        st.write(task)

import streamlit as st

# 페이지 제목 설정

st.title("나의 첫 Streamlit 앱")

# 텍스트 출력

st.write("Streamlit을 이용해 만든 웹 애플리케이션입니다.")

#사용자 입력 받기

name = st.text_input("이름을 입력하세요:")

#버튼 클릭 이벤트

if st.button("인사하기"):
    if name:
        st.success(f"안녕하세요,{name}님! 즐거운 하루 되세요!")
    else:
        st.warning("이름을 입력해주세요.")
