import json
import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore

if not firebase_admin._apps:
    key_string = st.secrets["firebase_key"]
    cred_dict = json.loads(key_string)
    cred = credentials.Certificate(cred_dict)
    firebase_admin.initialize_app(cred)

db = firestore.client()

st.title("오늘의 메뉴")

tab_title = ["월","화","수","목","금"]
tab1,tab2,tab3,tab4,tab5 = st.tabs(tab_title)

with tab1:
    st.header("월")
    st.write("잡곡밥")
    st.write("시래기국")
    st.write("제육볶음")
with tab2:
    st.header("화")
    st.write("백미밥")
    st.write("미역국")
    st.write("소세지야채볶음")
with tab3:
    st.header("수")
    st.write("짜장밥")
    st.write("계란국")
    st.write("탕수육")
with tab4:
    st.header("목")
    st.write("휴무")
with tab5:
    st.header("금")
    st.write("휴무")

with st.form("input_form",clear_on_submit=True):
    task = st.text_input("결식하실분들은 이름을 적으세요")
    sub = st.form_submit_button("추가")

if sub and task:
    db.collection("todos").add({"content":task, "at":firestore.SERVER_TIMESTAMP})
    st.success(f"'{task}'추가됨!")