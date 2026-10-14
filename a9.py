import streamlit as st

# 1. 사이드 바 : 데이터 입력부

with st.sidebar:
    st.header("메모 작성")
    name = st.text_input("작성자")
    msg = st.text_input("메모 내용")
    if st.button("등록"):
        db.collextion("memos").add({"user": name,"text":msg})
        st.rerun()

# 2. 메인 : 데이터 출력부

st.title("실시간 메모 게시판")

docs = db.collection("memos").stream()
for doc in docs:
    m = doc.to_dict()
    st.info(f"**{m['user']}**:{m['text']}")