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



tasks = [
    "1. 점심 메뉴 고민하기",
    "2. 버스 시간표 확인",
    "3. 15분 명상"

]

st.subheader("※ 금일 할 일 목록")

for task in tasks:
    # border = Ture를 주면 각 반복 요소가 단정한 상자로 감싸진다.
    
    with st.container(border=True):
        st.write(task)



# 페이지 제목 설정

st.title("오늘의 명언 뽑기!")

# 텍스트 출력

st.write("오늘 하루 기분이 좋아지는 사자성어.")

#사용자 입력 받기

name = st.text_input("이름을 입력하세요:")
if name == 49:
    if name:
        st.success
    else:
        st.warning("이름을 입력해주세요.")
#버튼 클릭 이벤트

if st.button("명언 뽑기"):
    if name:
        st.success(f"안녕하세요,{name}님! 오늘의 명언은 '결자해지(結者解之)' 입니다!")
    else:
        st.warning("이름을 입력해주세요.")


st.title("랜덤뽑기")
st.write("당신의 운을 시험해보세요!")

cs = ["1","2","3","4"]


if st.button("랜덤뽑기"):
    if cs:
        st.success(f"{cs}!")
    else:
        st.warning("다시뽑기")

st.title("오늘 배운거 복습")

ds = ["오늘 하루 알찼습니다",
      "내일 되면 까먹겠다",
      "0과1로 이루어진 컴퓨터 언어"]

st.subheader("오늘 하루도 고생했어")

for d in ds:
    with st.container(border=True):
        st.write(markdown)
