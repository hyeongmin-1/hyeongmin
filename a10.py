import streamlit as st

st.title("학생 성적 관리 웹앱")

if "students" not in st.session_state:
    st.sesstion_state.students = []

# 입력 폼

with st.form("students_form"):
    col1,col2 = st.columns(2)
    with col1: name = st.text_input("학생 이름")
    with col2: score = st.number_input("점수", min_value=0, max_value=100, value = 80)

    if st.form_submit_button("학생 추가") and name:
        st.session_state.students.append({"이름":name,"점수":score})
        st.success(f"{name}학생 등록 완료!")

#결과 대시보드
if st.session_state.students:
    col_l,col_r = st.columns(2)
    with col_l: st.table(st.session_state.students)
    with col_r:
        avg = sum(s["점수"] for s in st.sesstion_state.students) / len(st.session_state.students)
        st.metric("총 학생 수 ",f"{len(st.session_state.students)}명")
        st.metric("평균 점수", f"{avg:.1f}점")