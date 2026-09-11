import streamlit as st

st.set_page_config(page_title="Python 기초 정복 퀴즈", page_icon="🐍", layout="centered")

st.title("🐍 Python 기초 정복 퀴즈")
st.caption("for · range · 리스트 · 슬라이싱 · 중첩 리스트 · 딕셔너리 · in · CRUD")

questions = [
    {
        "category": "Ⅰ. for 반복문",
        "q": "1. for문의 가장 중요한 역할은 무엇일까요?",
        "options": ["데이터를 한 번만 출력한다", "같은 작업을 여러 번 반복한다", "데이터를 삭제한다", "숫자를 계산한다"],
        "answer": 1,
        "explain": "for문은 같은 작업을 여러 번 반복할 때 사용하는 반복문입니다."
    },
    {
        "category": "Ⅰ. for 반복문",
        "q": "2. 다음 코드에서 number의 역할은 무엇일까요?\n\nfor number in range(3):\n    print(number)",
        "options": ["반복 횟수를 정하는 함수", "반복할 때마다 값을 받아주는 변수", "리스트를 만드는 변수", "반복문을 종료하는 변수"],
        "answer": 1,
        "explain": "number는 반복할 때마다 range에서 나온 값을 하나씩 받아주는 반복자(변수)입니다."
    },
    {
        "category": "Ⅰ. for 반복문",
        "q": "3. i는 꼭 i라고 써야 할까요?",
        "options": ["O. 반드시 i여야 한다", "X. 다른 변수 이름으로 바꿔도 된다"],
        "answer": 1,
        "explain": "i는 단순한 변수 이름입니다. number, x 등 다른 이름을 사용할 수 있습니다."
    },
    {
        "category": "Ⅰ. for 반복문",
        "q": "4. range(5)가 만들어내는 숫자는 무엇일까요?",
        "options": ["1, 2, 3, 4, 5", "0, 1, 2, 3, 4", "0, 1, 2, 3, 4, 5", "5"],
        "answer": 1,
        "explain": "range(5)는 0부터 시작해서 5 직전인 4까지입니다. 총 5개의 숫자입니다."
    },
    {
        "category": "Ⅰ. for 반복문",
        "q": "5. 다음 코드는 '안녕'을 몇 번 출력할까요?\n\nfor i in range(7):\n    print('안녕')",
        "options": ["5번", "6번", "7번", "8번"],
        "answer": 2,
        "explain": "range(7)은 0~6까지 총 7개의 값을 만들기 때문에 7번 반복합니다."
    },
    {
        "category": "Ⅰ. for 반복문",
        "q": "6. 다음 코드의 출력 결과는?\n\nfor i in range(4):\n    print(i)",
        "options": ["1, 2, 3, 4", "0, 1, 2, 3", "0, 1, 2, 3, 4", "4"],
        "answer": 1,
        "explain": "range(4)는 0, 1, 2, 3입니다."
    },
    {
        "category": "Ⅰ. for 반복문",
        "q": "7. 다음 코드의 출력 결과는?\n\nfor i in range(2, 7):\n    print(i)",
        "options": ["2, 3, 4, 5, 6", "2, 3, 4, 5, 6, 7", "1, 2, 3, 4, 5, 6", "3, 4, 5, 6, 7"],
        "answer": 0,
        "explain": "range(시작, 끝)에서 끝값은 포함하지 않습니다. 따라서 2~6입니다."
    },
    {
        "category": "Ⅰ. for 반복문",
        "q": "8. 다음 코드에서 0이 출력되지 않는 이유는?\n\nfor i in range(5, 0, -1):\n    print(i)",
        "options": ["-1이기 때문에", "range의 끝값은 포함하지 않기 때문에", "for문은 0을 출력할 수 없기 때문에", "문법 오류이기 때문에"],
        "answer": 1,
        "explain": "range의 끝값은 포함하지 않습니다. 그래서 5,4,3,2,1까지만 출력됩니다."
    },
    {
        "category": "Ⅱ. 리스트와 반복",
        "q": "9. 다음 리스트에서 숫자 30의 인덱스는?\n\nnumbers = [10, 20, 30, 40, 50]",
        "options": ["1", "2", "3", "30"],
        "answer": 1,
        "explain": "리스트 인덱스는 0부터 시작합니다. 10은 0, 20은 1, 30은 2입니다."
    },
    {
        "category": "Ⅱ. 리스트와 반복",
        "q": "10. 다음 코드의 결과는?\n\nnumbers = [10, 20, 30, 40, 50]\nprint(numbers[2])",
        "options": ["10", "20", "30", "40"],
        "answer": 2,
        "explain": "인덱스 2에는 세 번째 값인 30이 있습니다."
    },
    {
        "category": "Ⅱ. 리스트와 반복",
        "q": "11. 리스트의 첫 번째 값 10을 가져오는 코드는?",
        "options": ["numbers[1]", "numbers[0]", "numbers[-1]", "numbers[10]"],
        "answer": 1,
        "explain": "리스트의 인덱스는 0부터 시작하므로 첫 번째 값은 numbers[0]입니다."
    },
    {
        "category": "Ⅱ. 리스트와 반복",
        "q": "12. 다음 코드에서 number에는 어떤 값이 차례대로 들어갈까요?\n\nnumbers = [10, 20, 30]\nfor number in numbers:\n    print(number)",
        "options": ["0, 1, 2", "10, 20, 30", "1, 2, 3", "10만 반복"],
        "answer": 1,
        "explain": "리스트를 직접 for로 반복하면 요소가 앞에서부터 하나씩 반복자에 들어갑니다."
    },
    {
        "category": "Ⅱ. 리스트와 반복",
        "q": "13. len([10, 20, 30, 40, 50])의 결과는?",
        "options": ["4", "5", "10", "50"],
        "answer": 1,
        "explain": "len()은 리스트에 들어 있는 요소의 개수를 반환합니다. 총 5개입니다."
    },
    {
        "category": "Ⅱ. 리스트와 반복",
        "q": "14. 다음 코드의 결과는?\n\nfor character in 'ABC':\n    print(character)",
        "options": ["ABC가 한 줄로 출력된다", "A, B, C가 한 글자씩 출력된다", "오류가 난다", "문자열은 for로 반복할 수 없다"],
        "answer": 1,
        "explain": "문자열도 순서가 있어 문자를 하나씩 꺼내 반복할 수 있습니다."
    },
    {
        "category": "Ⅲ. 역순과 슬라이싱",
        "q": "15. reversed(numbers)의 역할은?",
        "options": ["숫자를 더한다", "순서를 뒤집어서 반복할 수 있게 한다", "리스트를 삭제한다", "리스트의 길이를 구한다"],
        "answer": 1,
        "explain": "reversed()는 역순으로 값을 꺼내 반복할 수 있게 합니다."
    },
    {
        "category": "Ⅲ. 역순과 슬라이싱",
        "q": "16. 다음 코드의 결과는?\n\nnumbers = [10, 20, 30, 40]\nprint(numbers[::-1])",
        "options": ["[10, 20, 30, 40]", "[40, 30, 20, 10]", "[30, 20]", "오류"],
        "answer": 1,
        "explain": "[::-1]은 전체를 간격 -1로 가져와 뒤에서부터 순서대로 만듭니다."
    },
    {
        "category": "Ⅲ. 역순과 슬라이싱",
        "q": "17. 슬라이싱의 기본 형태는 무엇일까요?",
        "options": ["리스트[값]", "리스트[시작:끝:간격]", "리스트{시작,끝}", "리스트(시작,끝)"],
        "answer": 1,
        "explain": "슬라이싱은 [시작:끝:간격] 형태입니다."
    },
    {
        "category": "Ⅲ. 역순과 슬라이싱",
        "q": "18. numbers[::-1]에서 -1은 무엇을 의미할까요?",
        "options": ["마지막 인덱스", "간격을 -1로 한다", "첫 번째 값을 삭제한다", "숫자 -1을 출력한다"],
        "answer": 1,
        "explain": "세 번째 자리인 간격(step)에 -1을 지정해 뒤쪽 방향으로 하나씩 이동합니다."
    },
    {
        "category": "Ⅳ. 중첩 리스트",
        "q": "19. 다음 자료의 구조는 무엇일까요?\n\nlist_of_list = [[1, 2, 3], [4, 5], [6, 7]]",
        "options": ["문자열", "리스트 안에 리스트가 있는 중첩 리스트", "딕셔너리", "숫자 하나"],
        "answer": 1,
        "explain": "큰 리스트 안에 여러 개의 작은 리스트가 들어 있으므로 중첩 리스트입니다."
    },
    {
        "category": "Ⅳ. 중첩 리스트",
        "q": "20. 다음 코드에서 첫 번째 for의 items에는 무엇이 들어갈까요?\n\nfor items in list_of_list:\n    print(items)",
        "options": ["숫자 하나", "안쪽 리스트 하나", "인덱스 번호만", "딕셔너리의 Key"],
        "answer": 1,
        "explain": "첫 번째 for는 큰 리스트에서 안쪽 리스트를 하나씩 가져옵니다."
    },
    {
        "category": "Ⅳ. 중첩 리스트",
        "q": "21. 중첩 for문에서 두 번째 for의 역할은?",
        "options": ["바깥 리스트를 삭제한다", "가져온 안쪽 리스트의 요소를 하나씩 처리한다", "반복을 종료한다", "Key를 만든다"],
        "answer": 1,
        "explain": "첫 번째 for가 작은 리스트를 가져오면 두 번째 for가 그 안의 요소를 하나씩 꺼냅니다."
    },
    {
        "category": "Ⅴ. 딕셔너리",
        "q": "22. 딕셔너리는 어떤 방식으로 데이터를 관리할까요?",
        "options": ["인덱스만 사용", "Key와 Value를 연결해서 관리", "순서 없이 숫자만 관리", "문자열만 관리"],
        "answer": 1,
        "explain": "딕셔너리는 Key와 Value를 한 쌍으로 저장하고 Key를 이용해 값을 찾습니다."
    },
    {
        "category": "Ⅴ. 딕셔너리",
        "q": "23. 다음에서 Key는 무엇일까요?\n\n{'name': '철수'}",
        "options": ["철수", "name", "name과 철수 모두", "중괄호"],
        "answer": 1,
        "explain": "'name'이 Key이고 '철수'가 Value입니다."
    },
    {
        "category": "Ⅴ. 딕셔너리",
        "q": "24. 다음 코드의 결과는?\n\ndictionary = {'name': '철수', 'age': 20}\nprint(dictionary['name'])",
        "options": ["name", "철수", "age", "20"],
        "answer": 1,
        "explain": "dictionary['name']은 name Key에 연결된 Value인 '철수'를 가져옵니다."
    },
    {
        "category": "Ⅴ. 딕셔너리",
        "q": "25. 딕셔너리에서 같은 Key를 중복해서 사용할 수 있을까요?",
        "options": ["O", "X"],
        "answer": 1,
        "explain": "Key는 중복될 수 없습니다. 같은 Key에 새 값을 넣으면 기존 값이 새 값으로 대체됩니다."
    },
    {
        "category": "Ⅴ. 딕셔너리",
        "q": "26. 다음 코드에서 'age'를 삭제하는 방법은?",
        "options": ["remove dictionary['age']", "del dictionary['age']", "delete dictionary['age']", "dictionary.remove('age')"],
        "answer": 1,
        "explain": "딕셔너리의 특정 Key와 Value를 삭제할 때 del dictionary['age']를 사용할 수 있습니다."
    },
    {
        "category": "Ⅴ. 딕셔너리",
        "q": "27. CRUD에서 U는 무엇을 의미할까요?",
        "options": ["User", "Update", "Undo", "Use"],
        "answer": 1,
        "explain": "CRUD는 Create(추가), Read(읽기), Update(수정), Delete(삭제)입니다."
    },
    {
        "category": "Ⅴ. 딕셔너리",
        "q": "28. 다음 코드에서 in의 역할은?\n\nif key in dictionary:",
        "options": ["Key가 dictionary 안에 존재하는지 확인", "Key를 삭제", "Value를 수정", "딕셔너리를 생성"],
        "answer": 0,
        "explain": "in은 포함 여부를 확인합니다. 딕셔너리에서는 기본적으로 해당 Key가 존재하는지 확인합니다."
    },
    {
        "category": "Ⅴ. 딕셔너리",
        "q": "29. 다음 코드의 결과는?\n\nperson = {'name': '철수', 'age': 20}\nprint('name' in person)",
        "options": ["True", "False", "name", "철수"],
        "answer": 0,
        "explain": "'name'이라는 Key가 person 딕셔너리에 존재하므로 True입니다."
    },
    {
        "category": "Ⅴ. 딕셔너리",
        "q": "30. 다음 코드에서 key에는 무엇이 들어갈까요?\n\nperson = {'name': '철수', 'age': 20}\nfor key in person:\n    print(key)",
        "options": ["철수, 20", "name, age", "0, 1", "name:철수, age:20"],
        "answer": 1,
        "explain": "딕셔너리를 for로 반복하면 기본적으로 Key가 하나씩 반복자에 들어갑니다."
    },
    {
        "category": "Ⅴ. 딕셔너리",
        "q": "31. 다음 코드에서 dictionary[key]는 무엇을 의미할까요?\n\nfor key in dictionary:\n    print(dictionary[key])",
        "options": ["현재 Key에 해당하는 Value", "모든 Key", "인덱스", "딕셔너리의 길이"],
        "answer": 0,
        "explain": "현재 key를 이용해 그 Key에 연결된 Value를 가져옵니다."
    },
    {
        "category": "Ⅴ. 딕셔너리",
        "q": "32. 다음 코드의 ':'는 무엇일까요?\n\nprint(key, ':', dictionary[key])",
        "options": ["Key와 Value를 연결하는 Python 문법", "그냥 콜론이라는 문자를 출력하는 문자열", "반복을 시작하는 기호", "삭제 기호"],
        "answer": 1,
        "explain": "따옴표로 감싸진 ':'는 단순히 콜론이라는 문자를 출력하기 위한 문자열입니다."
    },
]

# 세션 상태
if "current" not in st.session_state:
    st.session_state.current = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "answered" not in st.session_state:
    st.session_state.answered = False
if "last_correct" not in st.session_state:
    st.session_state.last_correct = False
if "answers" not in st.session_state:
    st.session_state.answers = []

def reset_quiz():
    st.session_state.current = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.last_correct = False
    st.session_state.answers = []

q = questions[st.session_state.current]

st.progress((st.session_state.current) / len(questions))
st.write(f"**{st.session_state.current + 1} / {len(questions)} 문제**")
st.caption(q["category"])

st.markdown("### " + q["q"].replace("\n", "  \n"))

if not st.session_state.answered:
    choice = st.radio("정답을 골라보세요 👇", q["options"], index=None, key=f"choice_{st.session_state.current}")
    if st.button("✅ 정답 확인", use_container_width=True):
        if choice is None:
            st.warning("먼저 답을 골라주세요!")
        else:
            selected = q["options"].index(choice)
            st.session_state.last_correct = selected == q["answer"]
            if st.session_state.last_correct:
                st.session_state.score += 1
                st.success("🎉 정답!")
            else:
                st.error("❌ 아쉬워요! 다시 생각해봐요.")
            st.session_state.answers.append(selected)
            st.session_state.answered = True
            st.rerun()
else:
    if st.session_state.last_correct:
        st.success("🎉 정답!")
    else:
        st.error(f"❌ 오답! 정답은 **{q['options'][q['answer']]}**")
    st.info("💡 해설: " + q["explain"])

    if st.session_state.current < len(questions) - 1:
        if st.button("➡️ 다음 문제", use_container_width=True):
            st.session_state.current += 1
            st.session_state.answered = False
            st.rerun()
    else:
        st.balloons()
        st.markdown(f"## 🏆 퀴즈 완료!")
        st.markdown(f"### {len(questions)}문제 중 **{st.session_state.score}문제 정답**")
        percent = round(st.session_state.score / len(questions) * 100)
        if percent >= 90:
            st.success("🔥 완벽해요! 기초 개념을 거의 정복했어요.")
        elif percent >= 70:
            st.success("👏 잘했어요! 몇 가지 개념만 다시 보면 됩니다.")
        elif percent >= 50:
            st.warning("💪 좋아요! 틀린 문제의 해설을 다시 보면 실력이 확 올라갈 거예요.")
        else:
            st.info("🌱 괜찮아요! 지금은 개념을 익히는 단계예요. 다시 풀어보면 됩니다.")
        st.button("🔄 처음부터 다시 풀기", on_click=reset_quiz, use_container_width=True)

with st.sidebar:
    st.header("📚 학습 범위")
    st.write("1. for / 반복자 / range")
    st.write("2. 리스트 / 인덱스 / len")
    st.write("3. reversed / 슬라이싱")
    st.write("4. 중첩 리스트 / 중첩 for")
    st.write("5. 딕셔너리 / Key·Value")
    st.write("6. CRUD / in / 딕셔너리 for")
    st.divider()
    st.write(f"현재 점수: **{st.session_state.score}점**")
    st.button("🔄 퀴즈 초기화", on_click=reset_quiz)
