import streamlit as st
import random

st.set_page_config(page_title="파이썬 출력값 맞히기 1~14", page_icon="🐍")

# 핵심 학습 방식:
# "빈칸에 코드를 넣는 문제"가 아니라
# "완성된 코드를 보고 실행 결과를 맞히는 문제"입니다.
questions = [
    {
        "number": 1,
        "question": "다음 코드를 실행하면 무엇이 출력될까요?",
        "code": """numbers = [12, 25, 7, 33, 18]
total = 0

for number in numbers:
    total += number

print(total)""",
        "options": ["85", "90", "95", "100"],
        "answer": "95",
        "explanation": """total은 0에서 시작합니다.

12를 더하면 12
25를 더하면 37
7을 더하면 44
33을 더하면 77
18을 더하면 95

따라서 print(total)의 결과는 95입니다.

핵심은 total += number가
'기존 total에 number를 더해서 다시 total에 저장한다'는 뜻이라는 점입니다."""
    },
    {
        "number": 2,
        "question": "다음 코드를 실행하면 무엇이 출력될까요?",
        "code": """numbers = [10, 20, 30, 40]
total = 0

for number in numbers:
    total += number

print(total / len(numbers))""",
        "options": ["20", "25", "30", "35"],
        "answer": "25",
        "explanation": """먼저 total에 모든 숫자를 더합니다.

10 + 20 + 30 + 40 = 100

len(numbers)는 numbers 안에 값이 몇 개인지 알려줍니다.
숫자는 4개이므로 len(numbers)는 4입니다.

따라서 100 / 4 = 25입니다.

len()을 쓰면 리스트의 개수가 바뀌어도 현재 개수를 자동으로 계산할 수 있습니다."""
    },
    {
        "number": 3,
        "question": "다음 코드에서 print문은 몇 번 실행될까요?",
        "code": """for i in range(1, 5):
    print(i)""",
        "options": ["3번", "4번", "5번", "6번"],
        "answer": "4번",
        "explanation": """range(1, 5)는 1부터 시작해서 5 바로 전까지 만듭니다.

즉:
1, 2, 3, 4

총 4개의 숫자가 만들어지므로 print()도 4번 실행됩니다.

range()의 끝 숫자는 포함되지 않는다는 점이 중요합니다."""
    },
    {
        "number": 4,
        "question": "다음 코드를 실행하면 무엇이 출력될까요?",
        "code": """numbers = [5, 12, 3, 20, 8]
big = numbers[0]

for number in numbers:
    if number > big:
        big = number

print(big)""",
        "options": ["12", "20", "8", "5"],
        "answer": "20",
        "explanation": """처음에는 big = 5입니다.

12 > 5 → big = 12
3 > 12 → 거짓, 그대로 12
20 > 12 → big = 20
8 > 20 → 거짓

따라서 최종적으로 가장 큰 값은 20입니다.

max()를 사용하지 않고도 반복하면서 '현재까지 가장 큰 값'을 기억할 수 있습니다."""
    },
    {
        "number": 5,
        "question": "다음 코드를 실행하면 어떤 순서로 출력될까요?",
        "code": """character = {"name": "기사", "hp": 200, "level": 5}

for key in character:
    print(key)""",
        "options": ["기사, 200, 5", "name, hp, level", "0, 1, 2", "name, 기사, hp"],
        "answer": "name, hp, level",
        "explanation": """딕셔너리를 for문으로 직접 순회하면 기본적으로 key가 하나씩 나옵니다.

첫 번째: name
두 번째: hp
세 번째: level

따라서 name, hp, level이 순서대로 출력됩니다.

값을 출력하려면 character[key]처럼 key를 이용해 값을 꺼내야 합니다."""
    },
    {
        "number": 6,
        "question": "다음 코드를 실행하면 무엇이 출력될까요?",
        "code": """i = 1

while i <= 5:
    print(i)
    i += 1""",
        "options": ["1 2 3 4", "1 2 3 4 5", "2 3 4 5 6", "5 4 3 2 1"],
        "answer": "1 2 3 4 5",
        "explanation": """i는 1부터 시작합니다.

i <= 5인 동안 반복하므로:
1 출력
2 출력
3 출력
4 출력
5 출력

5를 출력한 뒤 i += 1로 i가 6이 됩니다.
6 <= 5는 거짓이므로 반복이 끝납니다."""
    },
    {
        "number": 7,
        "question": "다음 코드를 실행하면 무엇이 출력될까요?",
        "code": """numbers = [3, 8, 15, 22, 7, 40, 11]
count = 0

for number in numbers:
    if number % 2 == 0:
        count += 1

print(count)""",
        "options": ["2", "3", "4", "5"],
        "answer": "3",
        "explanation": """짝수만 세는 코드입니다.

3 → 홀수
8 → 짝수 → count 1
15 → 홀수
22 → 짝수 → count 2
7 → 홀수
40 → 짝수 → count 3
11 → 홀수

따라서 짝수는 8, 22, 40 총 3개입니다.

%는 나머지를 구하는 연산자이고,
number % 2 == 0은 '2로 나눈 나머지가 0인가?'라는 뜻입니다."""
    },
    {
        "number": 8,
        "question": "다음 코드를 실행하면 어떤 순서로 출력될까요?",
        "code": """word = "Python"

for letter in reversed(word):
    print(letter, end="")""",
        "options": ["Python", "nohtyP", "Ptoynh", "nhytoP"],
        "answer": "nohtyP",
        "explanation": """reversed(word)는 문자열을 뒤에서부터 순서대로 꺼냅니다.

Python
↓
n → o → h → t → y → P

그리고 print(..., end="")는 줄을 바꾸지 않고 이어서 출력합니다.

따라서 nohtyP가 출력됩니다."""
    },
    {
        "number": 9,
        "question": "다음 코드를 실행하면 무엇이 출력될까요?",
        "code": """array = [273, 32, 103, 57, 52]

for i in range(len(array)):
    if array[i] == 57:
        print(i)
        break""",
        "options": ["2", "3", "4", "57"],
        "answer": "3",
        "explanation": """인덱스는 0부터 시작합니다.

273 → 인덱스 0
32  → 인덱스 1
103 → 인덱스 2
57  → 인덱스 3

57을 찾았을 때 print(i)가 실행되므로 3이 출력됩니다.

break는 57을 찾은 순간 반복문을 완전히 끝냅니다."""
    },
    {
        "number": 10,
        "question": "다음 코드를 실행하면 무엇이 출력될까요?",
        "code": """i = 1
total = 0

while i <= 5:
    total += i
    i += 1

print(total)""",
        "options": ["10", "12", "15", "20"],
        "answer": "15",
        "explanation": """total에 1부터 5까지 차례대로 더합니다.

0 + 1 = 1
1 + 2 = 3
3 + 3 = 6
6 + 4 = 10
10 + 5 = 15

따라서 15가 출력됩니다.

여기서 i는 반복할 숫자를 관리하고, total은 누적해서 더한 결과를 관리합니다."""
    },
    {
        "number": 11,
        "question": "다음 코드를 실행하면 print()는 총 몇 번 실행될까요?",
        "code": """for dan in range(2, 5):
    for i in range(1, 4):
        print(dan, i)""",
        "options": ["6번", "8번", "9번", "12번"],
        "answer": "9번",
        "explanation": """바깥 for문은 2, 3, 4로 총 3번 반복합니다.

안쪽 for문은 1, 2, 3으로 총 3번 반복합니다.

중첩 반복문에서는
바깥 반복 횟수 × 안쪽 반복 횟수

= 3 × 3
= 9

따라서 print()는 총 9번 실행됩니다."""
    },
    {
        "number": 12,
        "question": "다음 코드의 출력 결과는 무엇일까요?",
        "code": """for number in range(1, 7):
    if number % 3 == 0:
        print("Fizz")
    else:
        print(number)""",
        "options": ["1 2 Fizz 4 5 Fizz", "Fizz 2 3 Fizz 5 6", "1 Fizz 3 4 Fizz 6", "1 2 3 4 5 6"],
        "answer": "1 2 Fizz 4 5 Fizz",
        "explanation": """1부터 6까지 확인합니다.

1 → 3의 배수 아님 → 1
2 → 3의 배수 아님 → 2
3 → 3의 배수 → Fizz
4 → 4
5 → 5
6 → 3의 배수 → Fizz

따라서 '1 2 Fizz 4 5 Fizz'가 됩니다."""
    },
    {
        "number": 13,
        "question": "다음 코드를 실행하면 무엇이 출력될까요?",
        "code": """numbers = [3, 8, 15, 22, 7, 40, 11, 6]
even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)""",
        "options": ["[3, 15, 7, 11]", "[8, 22, 40, 6]", "[3, 8, 15, 22, 7, 40, 11, 6]", "[8, 15, 22, 40]"],
        "answer": "[8, 22, 40, 6]",
        "explanation": """even_numbers는 빈 리스트 []로 시작합니다.

짝수인 값만 append()로 추가합니다.

8 → 추가
22 → 추가
40 → 추가
6 → 추가

따라서 최종 리스트는 [8, 22, 40, 6]입니다.

append()는 리스트의 맨 뒤에 값을 하나 추가합니다."""
    },
    {
        "number": 14,
        "question": "다음 코드를 실행하면 무엇이 출력될까요?",
        "code": """key_list = ["name", "hp", "mp", "level"]
value_list = ["기사", 200, 30, 5]

character = {}

for i in range(len(key_list)):
    character[key_list[i]] = value_list[i]

print(character["level"])""",
        "options": ["name", "200", "5", "level"],
        "answer": "5",
        "explanation": """key_list와 value_list의 같은 위치에 있는 값을 연결해 딕셔너리를 만듭니다.

name → 기사
hp → 200
mp → 30
level → 5

따라서 character["level"]은 5입니다.

len(key_list)는 key_list의 현재 개수를 자동으로 구합니다.
그래서 리스트의 개수가 바뀌어도 반복 횟수를 자동으로 맞출 수 있습니다."""
    },
]

# 선택지 순서를 매번 섞되, 정답 위치가 한 곳에 몰리지 않게 함
def prepare_questions():
    prepared = []
    for q in questions:
        options = q["options"].copy()
        random.shuffle(options)
        item = q.copy()
        item["options"] = options
        prepared.append(item)
    return prepared

if "quiz_questions" not in st.session_state:
    st.session_state.quiz_questions = prepare_questions()
if "current" not in st.session_state:
    st.session_state.current = 0
if "submitted" not in st.session_state:
    st.session_state.submitted = False
if "score" not in st.session_state:
    st.session_state.score = 0
if "answered" not in st.session_state:
    st.session_state.answered = set()

q = st.session_state.quiz_questions[st.session_state.current]

st.title("🐍 파이썬 출력값 맞히기")
st.caption("1~14번 개념 · 완성된 코드를 보고 실행 결과를 맞혀보세요!")

st.progress((st.session_state.current + 1) / len(questions))
st.markdown(f"## 문제 {q['number']} / 14")
st.write(q["question"])
st.code(q["code"], language="python")

selected = st.radio(
    "정답을 선택하세요.",
    q["options"],
    key=f"choice_{q['number']}"
)

if not st.session_state.submitted:
    if st.button("정답 확인", type="primary", use_container_width=True):
        st.session_state.submitted = True
        if selected == q["answer"] and q["number"] not in st.session_state.answered:
            st.session_state.score += 1
            st.session_state.answered.add(q["number"])
        st.rerun()
else:
    if selected == q["answer"]:
        st.success("🎉 정답입니다!")
    else:
        st.error("❌ 오답입니다!")

    st.info(f"정답: {q['answer']}")

    st.markdown("### 📖 자세한 풀이")
    st.write(q["explanation"])

    if st.session_state.current < len(questions) - 1:
        if st.button("다음 문제 →", type="primary", use_container_width=True):
            st.session_state.current += 1
            st.session_state.submitted = False
            st.rerun()
    else:
        st.success(f"🎊 퀴즈 완료! 점수: {st.session_state.score} / 14")
        if st.button("처음부터 다시 풀기", use_container_width=True):
            st.session_state.quiz_questions = prepare_questions()
            st.session_state.current = 0
            st.session_state.submitted = False
            st.session_state.score = 0
            st.session_state.answered = set()
            st.rerun()
