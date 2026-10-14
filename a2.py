# : 은 연속적 (리터럴 값) 번역을 한번에, ; 은 끝남
# =  대입 , == 같다
# if 분기문 제어문
# 조건문 (if-else)

user = "admin"
if user == "admin":   
    print("관리자님 안녕하세요")
else:
    print("일반 사용자 입니다")

today = "m"
if today == "m":
    print("좋은 아침입니다")
else:
    print("더 주무셔도 됩니다")

# 반복문 (for) 분기문 제어문
# for - in

tasks = ["대시보드 UI 기획","데이터베이스 연동", "사용자 테스트 진행"]

print("=== 오늘 할 일 목록===")
for task in tasks:
    print(task)

days = ["9:00 출근","12:00 점심시간","18:00 퇴근"]

print("★ Today Schedule ★")
for day in days:
    print(day)

# 조건문 & 반복문
# f*{s[]} 서식문자 string으로 표현해줌

students = [{"name": "철수", "score": 85},{"name":"영희","score":55}]

for s in students:
    if s["score"] >=60:
        result = "합격"
    else:
        result = "재시험"
    print(f"{s['name']}: {result}")

cs = [{"name": "GARY","pay":10000},{"name":"TOMMY","pay":90000}]

for c in cs:
    if c["pay"] >= 50000:
        result="VIP 고객입니다"
    else:
        result="일반 고객입니다"
    print(f"{c['name']}:{result}")

# 함수 재사용
def calculate_stats(score_list):
    total = sum(score_list)
    avg = total / len(score_list)
    return total, avg

total, avg = calculate_stats([90,80,100])
print(f"총점: {total},평균: {avg:.1f}")

def cl(list):
    total = sum(list)
    avg = total / len(list)
    return total, avg
list = [55,45,13,12,43,100]

total,avg = cl(list)
print(f"총점:{total},평균:{avg:.2f}")
