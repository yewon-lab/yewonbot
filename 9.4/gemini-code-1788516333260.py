import streamlit as st

st.set_page_config(page_title="파이썬 기초 25제 퀴즈", page_icon="🐍", layout="centered")

# 퀴즈 데이터 정의 (총 25문제)
quiz_data = [
    {
        "num": 1,
        "title": "리스트 중복 제거",
        "question": "다음 코드를 실행했을 때 출력되는 `result` 값은 무엇일까요?",
        "code": "numbers = [1, 3, 2, 3, 5, 1, 4, 2]\nresult = []\nfor num in numbers:\n    if num not in result:\n        result.append(num)\nprint(result)",
        "options": ["a) [1, 2, 3, 4, 5]", "b) [1, 3, 2, 5, 4]", "c) [1, 3, 2, 3, 5]", "d) [5, 4, 3, 2, 1]", "e) [1, 2, 3, 5, 4]"],
        "answer": "b) [1, 3, 2, 5, 4]",
        "exp": "for 문이 `numbers`의 원소를 순서대로 순회하므로 처음 등장하는 순서인 1, 3, 2, 5, 4 순서로 `result`에 추가됩니다."
    },
    {
        "num": 2,
        "title": "별 삼각형 만들기 (오름차순)",
        "question": "다음 별 피라미드를 출력하려고 합니다. 빈칸 (가)에 들어갈 range 조건으로 올바른 것은?",
        "code": "for i in range(1, 6):\n    print('*' * (가))\n\n# [출력 결과]\n# *\n# **\n# ***\n# ****\n# *****",
        "options": ["a) i - 1", "b) i", "c) i + 1", "d) 5 - i", "e) 6 - i"],
        "answer": "b) i",
        "exp": "i가 1부터 5까지 변할 때 별도 1개부터 5개까지 출력되어야 하므로 `i`가 들어가야 합니다."
    },
    {
        "num": 3,
        "title": "별 삼각형 만들기 (역삼각형)",
        "question": "다음 역삼각형을 출력하는 코드의 빈칸 (가)와 (나)에 들어갈 숫자로 올바른 것은?",
        "code": "for i in range((가), (나), -1):\n    print('*' * i)\n\n# [출력 결과]\n# *****\n# ****\n# ***\n# **\n# *",
        "options": ["a) (가): 5, (나): 1", "b) (가): 5, (나): 0", "c) (가): 6, (나): 0", "d) (가): 4, (나): -1", "e) (가): 5, (나): -1"],
        "answer": "b) (가): 5, (나): 0",
        "exp": "5부터 1까지 감소하며 반복해야 하므로 `range(5, 0, -1)`을 써야 합니다."
    },
    {
        "num": 4,
        "title": "최댓값 / 최솟값 찾기",
        "question": "다음 코드의 실행 결과로 올바른 것은?",
        "code": "numbers = [45, 12, 89, 3, 67, 21]\nmax_val = min_val = numbers[0]\nfor num in numbers:\n    if num > max_val:\n        max_val = num\n    if num < min_val:\n        min_val = num\nprint(max_val, min_val)",
        "options": ["a) 89 12", "b) 89 3", "c) 67 3", "d) 45 3", "e) 89 45"],
        "answer": "b) 89 3",
        "exp": "리스트 내 가장 큰 숫자는 89, 가장 작은 숫자는 3입니다."
    },
    {
        "num": 5,
        "title": "딕셔너리 조건 필터링",
        "question": "점수가 80점 이상인 사람의 이름만 리스트에 담으려고 합니다. 빈칸 (가)에 올바른 코드는?",
        "code": "scores = {\"철수\": 85, \"영희\": 72, \"민수\": 91, \"지은\": 68}\npassed = []\nfor name, score in scores.items():\n    if (가):\n        passed.append(name)\nprint(passed)",
        "options": ["a) score > 80", "b) score >= 80", "c) scores[name] == 80", "d) name >= 80", "e) score <= 80"],
        "answer": "b) score >= 80",
        "exp": "80점 '이상'이므로 크거나 같다인 `>= 80` 조건문이 들어가야 합니다."
    },
    {
        "num": 6,
        "title": "while + break 조건식",
        "question": "1부터 누적 합을 구하다가 합이 500을 '초과'하는 순간 반복을 종료하려고 합니다. 빈칸 (가)는?",
        "code": "total = 0\nnum = 1\nwhile True:\n    total += num\n    if (가):\n        break\n    num += 1\nprint(num, total)",
        "options": ["a) total == 500", "b) total > 500", "c) total >= 500", "d) num > 500", "e) total < 500"],
        "answer": "b) total > 500",
        "exp": "500을 넘는(초과하는) 순간이므로 `total > 500`일 때 break합니다."
    },
    {
        "num": 7,
        "title": "리스트 뒤집기 (반복문)",
        "question": "슬라이싱이나 reverse() 없이 리스트를 뒤집는 코드입니다. 빈칸 (가)에 알맞은 메서드는?",
        "code": "numbers = [1, 2, 3, 4, 5]\nreversed_list = []\nfor num in numbers:\n    reversed_list.(가)(0, num)\nprint(reversed_list)  # [5, 4, 3, 2, 1]",
        "options": ["a) append", "b) insert", "c) push", "d) add", "e) extend"],
        "answer": "b) insert",
        "exp": "`insert(0, num)`을 사용하면 매번 맨 앞 인덱스(0번)에 값을 삽입하여 순서를 뒤집을 수 있습니다."
    },
    {
        "num": 8,
        "title": "소수(Prime) 판별",
        "question": "다음은 `number = 17`이 소수인지 판별하는 코드입니다. 빈칸 (가)의 조건으로 올바른 것은?",
        "code": "number = 17\nis_prime = True\nfor i in range(2, number):\n    if (가):\n        is_prime = False\n        break\nprint(is_prime)",
        "options": ["a) number % i == 0", "b) number / i == 0", "c) number // i == 0", "d) i % number == 0", "e) number % i != 0"],
        "answer": "a) number % i == 0",
        "exp": "2부터 (number-1)까지 나누어떨어지는지 확인하는 나머지가 0인지 구하는 조건(`number % i == 0`)이 들어가야 합니다."
    },
    {
        "num": 9,
        "title": "특정 문자 개수 세기",
        "question": "다음 코드가 실행된 후 `count`에 저장되는 값은 얼마일까요?",
        "code": "sentence = \"banana\"\ntarget = \"a\"\ncount = 0\nfor char in sentence:\n    if char == target:\n        count += 1\nprint(count)",
        "options": ["a) 1", "b) 2", "c) 3", "d) 4", "e) 6"],
        "answer": "c) 3",
        "exp": "\"banana\"에서 알파벳 'a'는 총 3개 포함되어 있습니다."
    },
    {
        "num": 10,
        "title": "버블 정렬 (Bubble Sort)",
        "question": "오름차순 버블 정렬 코드의 빈칸 (가)에 들어가야 할 비교 연산자는?",
        "code": "numbers = [5, 2, 9, 1, 7]\nn = len(numbers)\nfor i in range(n):\n    for j in range(0, n - i - 1):\n        if numbers[j] (가) numbers[j + 1]:\n            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]",
        "options": ["a) <", "b) >", "c) ==", "d) <=", "e) !="],
        "answer": "b) >",
        "exp": "오름차순 정렬 시 앞의 값이 뒤의 값보다 크면 위치를 바꾸어야 하므로 `>` 연산자가 필요합니다."
    },
    {
        "num": 11,
        "title": "continue 문 활용",
        "question": "1부터 50까지 중 3의 배수를 제외하고 합산하는 코드입니다. 빈칸 (가)에 알맞은 조건식은?",
        "code": "total = 0\nfor i in range(1, 51):\n    if (가):\n        continue\n    total += i",
        "options": ["a) i % 3 != 0", "b) i % 3 == 0", "c) i // 3 == 0", "d) i / 3 == 0", "e) i == 3"],
        "answer": "b) i % 3 == 0",
        "exp": "3의 배수일 때 연산을 스킵(continue)해야 하므로 `i % 3 == 0`이 정답입니다."
    },
    {
        "num": 12,
        "title": "딕셔너리 리스트에서 최고점 찾기",
        "question": "최고 점수를 받은 학생의 이름을 출력하는 코드의 실행 결과는?",
        "code": "students = [\n    {\"name\": \"철수\", \"score\": 85},\n    {\"name\": \"영희\", \"score\": 92},\n    {\"name\": \"민수\", \"score\": 78},\n]\ntop_student = students[0]\nfor student in students:\n    if student[\"score\"] > top_student[\"score\"]:\n        top_student = student\nprint(top_student[\"name\"])",
        "options": ["a) 철수", "b) 영희", "c) 민수", "d) 92", "e) Error"],
        "answer": "b) 영희",
        "exp": "가장 높은 점수(92점)를 보유한 '영희'가 top_student가 됩니다."
    },
    {
        "num": 13,
        "title": "range 3개 매개변수 사용",
        "question": "1부터 100까지 짝수의 합을 구하려 합니다. 빈칸 (가)에 들어갈 range 구문은?",
        "code": "total = sum(range((가)))\nprint(total)",
        "options": ["a) 1, 100, 2", "b) 2, 101, 2", "c) 2, 100, 2", "d) 0, 100, 2", "e) 1, 101, 2"],
        "answer": "b) 2, 101, 2",
        "exp": "짝수는 2부터 시작하여 100까지 포함해야 하므로 `range(2, 101, 2)` 형태가 되어야 합니다."
    },
    {
        "num": 14,
        "title": "두 번째로 큰 값 찾기",
        "question": "다음 코드 실행 후 `second` 변수의 최종 출력값은?",
        "code": "numbers = [45, 12, 89, 3, 67, 21]\nfirst = second = float('-inf')\nfor num in numbers:\n    if num > first:\n        second = first\n        first = num\n    elif num > second and num != first:\n        second = num\nprint(second)",
        "options": ["a) 89", "b) 45", "c) 67", "d) 21", "e) 12"],
        "answer": "c) 67",
        "exp": "가장 큰 값은 89이며, 두 번째로 큰 값은 67입니다."
    },
    {
        "num": 15,
        "title": "while 문 팩토리얼 계산",
        "question": "5! (5 팩토리얼)을 구하는 코드의 빈칸 (가)에 들어갈 연산식은?",
        "code": "n = 5\nfact = 1\nwhile n > 0:\n    fact *= n\n    (가)\nprint(fact)  # 120",
        "options": ["a) n += 1", "b) n -= 1", "c) n *= 1", "d) n = fact - 1", "e) break"],
        "answer": "b) n -= 1",
        "exp": "n이 5, 4, 3, 2, 1로 감소하며 곱해져야 하므로 `n -= 1`이 들어가야 합니다."
    },
    {
        "num": 16,
        "title": "과목별 평균 점수 구하기",
        "question": "다음 학생들의 수학(math) 평균 점수로 올바른 값은?",
        "code": "data = [\n    {\"math\": 80, \"eng\": 90},\n    {\"math\": 70, \"eng\": 85},\n    {\"math\": 90, \"eng\": 95}\n]\ntotal_math = sum(s[\"math\"] for s in data)\nprint(total_math / len(data))",
        "options": ["a) 75.0", "b) 80.0", "c) 85.0", "d) 90.0", "e) 240.0"],
        "answer": "b) 80.0",
        "exp": "(80 + 70 + 90) / 3 = 240 / 3 = 80.0 이 됩니다."
    },
    {
        "num": 17,
        "title": "리스트 컴프리헨션 변환",
        "question": "다음 for 문과 동일하게 작동하는 리스트 컴프리헨션 구문은?",
        "code": "# for 문 구문\nresult = []\nfor x in range(10):\n    if x % 2 == 0:\n        result.append(x)",
        "options": [
            "a) [x for x in range(10) if x % 2 == 0]",
            "b) [x if x % 2 == 0 for x in range(10)]",
            "c) [for x in range(10) if x % 2 == 0]",
            "d) [x % 2 == 0 for x in range(10)]",
            "e) [x for x in range(10)]"
        ],
        "answer": "a) [x for x in range(10) if x % 2 == 0]",
        "exp": "필터링 if문은 리스트 컴프리헨션 맨 뒤에 위치합니다: `[표현식 for 변수 in 이터러블 if 조건]`"
    },
    {
        "num": 18,
        "title": "문자열 뒤집기 (반복문)",
        "question": "다음 문자를 반대로 뒤집는 코드의 실행 결과는?",
        "code": "text = \"Python\"\nreversed_text = \"\"\nfor char in text:\n    reversed_text = char + reversed_text\nprint(reversed_text)",
        "options": ["a) Python", "b) nohtyP", "c) P y t h o n", "d) PYTHON", "e) Error"],
        "answer": "b) nohtyP",
        "exp": "매 루프마다 문자열 앞에 새 문자를 덧붙이므로 `nohtyP`로 순서가 반대가 됩니다."
    },
    {
        "num": 19,
        "title": "중첩 반복문 구구단",
        "question": "다음 구구단 코드에서 `print()`문이 실행되는 총 횟수는?",
        "code": "for dan in range(2, 10):\n    for i in range(1, 10):\n        print(f\"{dan} x {i} = {dan * i}\")",
        "options": ["a) 72", "b) 81", "c) 90", "d) 64", "e) 100"],
        "answer": "a) 72",
        "exp": "dan은 8개(2~9), i는 9개(1~9)이므로 총 8 x 9 = 72번 실행됩니다."
    },
    {
        "num": 20,
        "title": "리스트 요소 수정",
        "question": "다음 코드가 실행된 후 `numbers`의 최종 상태는?",
        "code": "numbers = [10, 20, 30, 40]\nfor i in range(len(numbers)):\n    numbers[i] += 5\nprint(numbers)",
        "options": [
            "a) [10, 20, 30, 40]",
            "b) [15, 25, 35, 45]",
            "c) [5, 5, 5, 5]",
            "d) [10, 20, 30, 40, 5]",
            "e) Error"
        ],
        "answer": "b) [15, 25, 35, 45]",
        "exp": "인덱스로 리스트 각 요소에 접근하여 5씩 더했으므로 모든 값에 5가 더해집니다."
    },
    {
        "num": 21,
        "title": "딕셔너리 값 다루기",
        "question": "다음 딕셔너리의 모든 값(Value)의 합으로 올바른 것은?",
        "code": "data = {'a': 10, 'b': 20, 'c': 30}\ntotal = 0\nfor val in data.values():\n    total += val\nprint(total)",
        "options": ["a) 10", "b) 30", "c) 60", "d) abc", "e) Error"],
        "answer": "c) 60",
        "exp": "`data.values()`는 10, 20, 30을 반환하므로 합은 60입니다."
    },
    {
        "num": 22,
        "title": "while - continue 활용",
        "question": "다음 코드의 출력 결과로 올바른 것은?",
        "code": "i = 0\nwhile i < 3:\n    i += 1\n    if i == 2:\n        continue\n    print(i, end=' ')",
        "options": ["a) 1 2 3", "b) 1 3", "c) 2 3", "d) 1 2", "e) 3"],
        "answer": "b) 1 3",
        "exp": "i가 2일 때 `continue`를 만나 아래 `print()`를 건너뛰므로 1과 3만 출력됩니다."
    },
    {
        "num": 23,
        "title": "무한 루프 탈출 조건",
        "question": "다음 while 문이 멈추기 위한 조건으로 빈칸 (가)에 적절한 것은?",
        "code": "count = 10\nwhile True:\n    if (가):\n        break\n    count -= 1\nprint('종료')",
        "options": ["a) count > 0", "b) count == 0", "c) count == 10", "d) count < 0", "e) count != 0"],
        "answer": "b) count == 0",
        "exp": "count가 10에서 1씩 감소하므로 0이 되는 순간 break해야 정상 종료됩니다."
    },
    {
        "num": 24,
        "title": "자료형 확인 및 필터링",
        "question": "다음 리스트에서 정수형(int) 데이터의 개수는 몇 개일까요?",
        "code": "mixed = [1, \"hello\", 3.14, True, 42, \"python\"]\ncount = 0\nfor item in mixed:\n    if type(item) == int:\n        count += 1\nprint(count)",
        "options": ["a) 1개", "b) 2개", "c) 3개", "d) 4개", "e) 5개"],
        "answer": "b) 2개",
        "exp": "`type(item) == int` 비교 시 strict하게 정수형만 셀 수 있습니다. 1과 42 총 2개입니다."
    },
    {
        "num": 25,
        "title": "2차원 리스트 순회",
        "question": "다음 2차원 리스트의 모든 요소를 더한 결과는?",
        "code": "matrix = [\n    [1, 2],\n    [3, 4],\n    [5, 6]\n]\ntotal = 0\nfor row in matrix:\n    for val in row:\n        total += val\nprint(total)",
        "options": ["a) 15", "b) 21", "c) 12", "d) 20", "e) 25"],
        "answer": "b) 21",
        "exp": "1 + 2 + 3 + 4 + 5 + 6 = 21 입니다."
    }
]

# 세션 상태 초기화
if "score" not in st.session_state:
    st.session_state.score = 0
if "answered" not in st.session_state:
    st.session_state.answered = [False] * len(quiz_data)
if "user_choices" not in st.session_state:
    st.session_state.user_choices = [None] * len(quiz_data)

st.title("🐍 파이썬 기초 25제 퀴즈 앱")
st.caption("Streamlit으로 여는 파이썬 반복문/자료구조 연습 문제")
st.divider()

# 점수판
cols = st.columns(2)
cols[0].metric("풀어낸 문제 수", f"{sum(st.session_state.answered)} / {len(quiz_data)}")
cols[1].metric("현재 점수", f"{st.session_state.score} 점")

st.divider()

# 문제 렌더링
for idx, q in enumerate(quiz_data):
    st.subheader(f"Q{q['num']}. {q['title']}")
    st.write(q["question"])
    if q.get("code"):
        st.code(q["code"], language="python")

    # 선택지 UI
    choice = st.radio(
        f"문제 {q['num']}의 정답을 선택하세요:",
        q["options"],
        key=f"q_{idx}",
        disabled=st.session_state.answered[idx]
    )

    # 제출 버튼
    if not st.session_state.answered[idx]:
        if st.button(f"Q{q['num']} 정답 확인", key=f"btn_{idx}"):
            st.session_state.answered[idx] = True
            st.session_state.user_choices[idx] = choice
            if choice == q["answer"]:
                st.session_state.score += 4
            st.rerun()

    # 정답 제출 후 결과 및 해설 표시
    if st.session_state.answered[idx]:
        user_choice = st.session_state.user_choices[idx]
        if user_choice == q["answer"]:
            st.success("⭕ **정답입니다!**")
        else:
            st.error(f"❌ **오답입니다.** (선택한 답: {user_choice})")
            st.info(f"**정답:** {q['answer']}")
        
        with st.expander("💡 상세 해설 보기"):
            st.write(q["exp"])
    
    st.divider()

# 전체 결과 안내
if all(st.session_state.answered):
    st.balloons()
    st.header("🎉 모든 문제를 완료하셨습니다!")
    st.subheader(f"최종 점수: {st.session_state.score} / 100점")
    if st.button("다시 풀기"):
        st.session_state.score = 0
        st.session_state.answered = [False] * len(quiz_data)
        st.session_state.user_choices = [None] * len(quiz_data)
        st.rerun()