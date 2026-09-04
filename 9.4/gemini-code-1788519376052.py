import streamlit as st

st.set_page_config(page_title="파이썬 기초 25제 코드 문법/수식 퀴즈", page_icon="🐍", layout="centered")

# 퀴즈 데이터 정의 (총 25문제 - 출력값 계산 제거, 빈칸 채우기 및 조건 수식 중심)
quiz_data = [
    {
        "num": 1,
        "title": "리스트 중복 제거 조건식",
        "question": "리스트에서 중복을 제거하며 새로운 리스트에 담으려 합니다. 빈칸 (가)에 들어갈 조건식으로 올바른 것은?",
        "code": "numbers = [1, 3, 2, 3, 5, 1, 4, 2]\nresult = []\nfor num in numbers:\n    if (가):\n        result.append(num)",
        "options": ["a) num in result", "b) num not in result", "c) result is num", "d) num == result", "e) not num"],
        "answer": "b) num not in result",
        "exp": "새 리스트 `result`에 현재 숫자 `num`이 들어있지 않을 때만(`not in`) 추가해야 중복이 제거됩니다."
    },
    {
        "num": 2,
        "title": "별 삼각형 오름차순 출력 수식",
        "question": "i가 1부터 5까지 변할 때, 별을 1개부터 5개까지 늘려가며 출력하려 합니다. 빈칸 (가)에 들어갈 수식은?",
        "code": "for i in range(1, 6):\n    print('*' * (가))",
        "options": ["a) i - 1", "b) i", "c) i + 1", "d) 5 - i", "e) 6 - i"],
        "answer": "b) i",
        "exp": "파이썬에서 문자열에 숫자를 곱하면 해당 횟수만큼 반복됩니다. i가 1~5로 늘어나므로 `i`를 곱해야 합니다."
    },
    {
        "num": 3,
        "title": "역삼각형 출력을 위한 range 매개변수",
        "question": "별 5개부터 1개까지 줄어드는 역삼각형을 만들려고 합니다. range의 빈칸 (가)와 (나)로 올바른 것은?",
        "code": "for i in range((가), (나), -1):\n    print('*' * i)",
        "options": ["a) (가): 5, (나): 1", "b) (가): 5, (나): 0", "c) (가): 6, (나): 0", "d) (가): 4, (나): -1", "e) (가): 5, (나): -1"],
        "answer": "b) (가): 5, (나): 0",
        "exp": "range(시작, 끝, 증감)에서 끝값은 포함되지 않으므로 1까지 감소시키려면 끝값을 0으로 설정해야 합니다."
    },
    {
        "num": 4,
        "title": "최댓값 갱신 조건식",
        "question": "반복문으로 리스트를 순회하며 최댓값을 찾으려 합니다. 빈칸 (가)에 들어갈 조건식은?",
        "code": "numbers = [45, 12, 89, 3, 67, 21]\nmax_val = numbers[0]\nfor num in numbers:\n    if (가):\n        max_val = num",
        "options": ["a) num < max_val", "b) num > max_val", "c) num == max_val", "d) num != max_val", "e) max_val >= num"],
        "answer": "b) num > max_val",
        "exp": "현재 검사 중인 숫자(`num`)가 기존 최댓값(`max_val`)보다 클 때만 최댓값을 새 값으로 교체합니다."
    },
    {
        "num": 5,
        "title": "딕셔너리 키-값 동시 순회 메서드",
        "question": "딕셔너리의 키(이름)와 값(점수)을 동시에 가져와 반복문에서 다루려고 합니다. 빈칸 (가)에 들어갈 메서드는?",
        "code": "scores = {\"철수\": 85, \"영희\": 72, \"민수\": 91}\nfor name, score in scores.(가)():\n    if score >= 80:\n        print(name)",
        "options": ["a) keys", "b) values", "c) items", "d) get", "e) list"],
        "answer": "c) items",
        "exp": "딕셔너리의 `items()` 메서드는 (Key, Value) 쌍을 튜플 형태로 반환하여 동시 순회를 가능하게 합니다."
    },
    {
        "num": 6,
        "title": "while 문 탈출을 위한 break 문 위치",
        "question": "누적 합이 500을 넘는 순간 반복을 즉시 중단하려 합니다. 빈칸 (가)에 들어갈 제어문은?",
        "code": "total = 0\nnum = 1\nwhile True:\n    total += num\n    if total > 500:\n        (가)\n    num += 1",
        "options": ["a) pass", "b) continue", "c) break", "d) return", "e) exit()"],
        "answer": "c) break",
        "exp": "`break`는 자신을 감싸고 있는 가장 가까운 반복문(while/for)을 즉시 종료하고 탈출합니다."
    },
    {
        "num": 7,
        "title": "리스트 맨 앞에 요소를 추가하는 메서드",
        "question": "기존 메서드나 슬라이싱 없이 리스트의 0번 인덱스(맨 앞)에 요소를 넣어 순서를 뒤집으려 합니다. 빈칸 (가)는?",
        "code": "numbers = [1, 2, 3, 4, 5]\nreversed_list = []\nfor num in numbers:\n    reversed_list.(가)(0, num)",
        "options": ["a) append", "b) insert", "c) push", "d) add", "e) extend"],
        "answer": "b) insert",
        "exp": "`insert(index, element)` 메서드는 지정한 인덱스 위치에 데이터를 삽입합니다. 0번에 넣으면 기존 요소가 뒤로 밀립니다."
    },
    {
        "num": 8,
        "title": "소수 판별 나누어떨어짐 연산자",
        "question": "숫자 number가 i로 '나누어떨어지는지(약수인지)' 판단하는 조건 수식으로 올바른 것은?",
        "code": "for i in range(2, number):\n    if (가):\n        is_prime = False\n        break",
        "options": ["a) number % i == 0", "b) number / i == 0", "c) number // i == 0", "d) i % number == 0", "e) number % i != 0"],
        "answer": "a) number % i == 0",
        "exp": "`%` 연산자는 나눗셈의 나머지를 구합니다. 나머지가 0(`== 0`)이면 나누어떨어진다는 의미입니다."
    },
    {
        "num": 9,
        "title": "문자열 내 특정 문자 검색 수식",
        "question": "문자열을 한 글자씩 순회하며 target 문자와 일치하는지 비교하려 합니다. 빈칸 (가)는?",
        "code": "sentence = \"banana\"\ntarget = \"a\"\ncount = 0\nfor char in sentence:\n    if (가):\n        count += 1",
        "options": ["a) char is target", "b) char == target", "c) char in target", "d) target != char", "e) char = target"],
        "answer": "b) char == target",
        "exp": "두 값의 내용이 일치하는지 비교할 때는 동등 비교 연산자 `==`를 사용합니다."
    },
    {
        "num": 10,
        "title": "버블 정렬의 오름차순 교환 조건 수식",
        "question": "인접한 두 요소를 비교하여 앞의 값이 뒤의 값보다 크면 위치를 교환하려 합니다. 빈칸 (가)는?",
        "code": "for j in range(0, n - i - 1):\n    if numbers[j] (가) numbers[j + 1]:\n        numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]",
        "options": ["a) <", "b) >", "c) ==", "d) <=", "e) !="],
        "answer": "b) >",
        "exp": "오름차순 정렬에서는 앞의 요소(`numbers[j]`)가 뒤의 요소(`numbers[j+1]`)보다 크면(`>`) 위치를 맞바꿉니다."
    },
    {
        "num": 11,
        "title": "3의 배수를 스킵하는 continue 조건식",
        "question": "3의 배수인 경우 아래 코드를 실행하지 않고 다음 루프로 건너뛰려 합니다. 빈칸 (가)는?",
        "code": "total = 0\nfor i in range(1, 51):\n    if (가):\n        continue\n    total += i",
        "options": ["a) i % 3 != 0", "b) i % 3 == 0", "c) i // 3 == 0", "d) i / 3 == 0", "e) i == 3"],
        "answer": "b) i % 3 == 0",
        "exp": "3의 배수는 3으로 나눈 나머지가 0인 수이므로 `i % 3 == 0`일 때 `continue`를 실행합니다."
    },
    {
        "num": 12,
        "title": "딕셔너리 리스트의 특정 키 접근 수식",
        "question": "학생 딕셔너리에서 'score' 키에 해당하는 값에 접근하는 올바른 수식은?",
        "code": "students = [{\"name\": \"철수\", \"score\": 85}, ...]\nfor student in students:\n    if (가) > 90:\n        print(student[\"name\"])",
        "options": ["a) student.score", "b) student[\"score\"]", "c) student(score)", "d) student.get.score", "e) students[\"score\"]"],
        "answer": "b) student[\"score\"]",
        "exp": "파이썬 딕셔너리의 값에 접근할 때는 대괄호 안에 키 이름을 문자열 형태로 지정합니다: `student[\"score\"]`"
    },
    {
        "num": 13,
        "title": "짝수만 생성하는 range 매개변수 수식",
        "question": "if문 없이 range 함수만 사용하여 2부터 100까지 짝수만 생성하는 수식은?",
        "code": "even_sum = sum(range((가)))",
        "options": ["a) 1, 100, 2", "b) 2, 101, 2", "c) 2, 100, 2", "d) 0, 100, 2", "e) 2, 101, 1"],
        "answer": "b) 2, 101, 2",
        "exp": "2부터 시작하여 100을 포함(끝값 101 미만)하고 2씩 증가시키는 `range(2, 101, 2)`가 정답입니다."
    },
    {
        "num": 14,
        "title": "음의 무한대로 초기화하는 수식",
        "question": "최댓값 비교 시 어떤 숫자보다도 작은 기본값(음의 무한대)으로 변수를 초기화하는 파이썬 수식은?",
        "code": "first = second = (가)",
        "options": ["a) float('inf')", "b) float('-inf')", "c) int('-inf')", "d) math.nan", "e) None"],
        "answer": "b) float('-inf')",
        "exp": "`float('-inf')`는 음의 무한대(Negative Infinity)를 뜻하며, 수치 비교 알고리즘에서 초기 최댓값 변수로 사용됩니다."
    },
    {
        "num": 15,
        "title": "팩토리얼 감소 연산 수식",
        "question": "while 문으로 n 팩토리얼을 구할 때, n을 1씩 줄여나가는 단축 대입 연산 수식은?",
        "code": "n = 5\nfact = 1\nwhile n > 0:\n    fact *= n\n    (가)",
        "options": ["a) n =+ 1", "b) n -= 1", "c) n =-- 1", "d) n--", "e) n -= fact"],
        "answer": "b) n -= 1",
        "exp": "파이썬에는 `n--` 증감 연산자가 없으므로 단축 대입 연산자 `n -= 1` (또는 `n = n - 1`)을 사용해야 합니다."
    },
    {
        "num": 16,
        "title": "리스트 요소의 개수를 구하는 내장함수 수식",
        "question": "평균을 구하기 위해 데이터 전체의 개수(길이)를 구하는 파이썬 내장함수 수식은?",
        "code": "data = [80, 70, 90]\naverage = sum(data) / (가)",
        "options": ["a) count(data)", "b) size(data)", "c) len(data)", "d) length(data)", "e) data.length()"],
        "answer": "c) len(data)",
        "exp": "파이썬에서 시퀀스(리스트, 문자열 등)의 길이는 `len()` 내장함수로 구합니다."
    },
    {
        "num": 17,
        "title": "리스트 컴프리헨션 문법 수식",
        "question": "0부터 9까지 숫자 중 짝수만 추출하는 리스트 컴프리헨션의 올바른 표현식은?",
        "code": "result = (가)",
        "options": [
            "a) [x for x in range(10) if x % 2 == 0]",
            "b) [if x % 2 == 0 for x in range(10) x]",
            "c) [x if x % 2 == 0 for x in range(10)]",
            "d) [for x in range(10) if x % 2 == 0 x]",
            "e) [x for x in range(10) else x % 2 == 0]"
        ],
        "answer": "a) [x for x in range(10) if x % 2 == 0]",
        "exp": "기본 리스트 컴프리헨션 필터링 구조는 `[표현식 for 변수 in 이터러블 if 조건식]` 입니다."
    },
    {
        "num": 18,
        "title": "문자열 역순 연결 수식",
        "question": "반복문으로 문자를 하나씩 가져와 문자열을 역순으로 이어 붙이는 수식은?",
        "code": "text = \"Python\"\nreversed_text = \"\"\nfor char in text:\n    reversed_text = (가)",
        "options": ["a) reversed_text + char", "b) char + reversed_text", "c) char * reversed_text", "d) reversed_text.append(char)", "e) char[::-1]"],
        "answer": "b) char + reversed_text",
        "exp": "새 문자(`char`)를 기존 문자열(`reversed_text`)의 '앞'에 붙여야 글자 순서가 뒤집힙니다."
    },
    {
        "num": 19,
        "title": "f-string 문자열 포맷팅 수식",
        "question": "구구단 변수 dan과 i의 곱을 문자열 안에 직접 삽입하는 f-string 수식은?",
        "code": "dan = 3\ni = 5\nprint(f\"{dan} x {i} = (가)\")",
        "options": ["a) %d\" % (dan*i)", "b) {dan * i}", "c) (dan * i)", "d) [dan * i]", "e) ${dan * i}"],
        "answer": "b) {dan * i}",
        "exp": "f-string(`f\"...\"`) 내부에서는 중괄호 `{}` 안에 변수나 파이썬 수식을 직접 작성할 수 있습니다."
    },
    {
        "num": 20,
        "title": "인덱스를 통한 리스트 요소 수정 수식",
        "question": "리스트의 각 인덱스 위치에 접근하여 값을 5씩 증가시키는 올바른 대입 수식은?",
        "code": "numbers = [10, 20, 30, 40]\nfor i in range(len(numbers)):\n    (가)",
        "options": ["a) i += 5", "b) numbers[i] += 5", "c) numbers += 5", "d) numbers.append(5)", "e) numbers[i] =+ 5"],
        "answer": "b) numbers[i] += 5",
        "exp": "리스트 원소를 직접 변경하려면 인덱스로 해당 요소에 접근(`numbers[i]`)한 후 값을 변경해야 합니다."
    },
    {
        "num": 21,
        "title": "딕셔너리의 Value만 추출하는 메서드 수식",
        "question": "딕셔너리에서 값(Value)들만 모아서 순회하고자 할 때 사용하는 메서드 수식은?",
        "code": "data = {'a': 10, 'b': 20, 'c': 30}\nfor val in data.(가)():\n    print(val)",
        "options": ["a) keys", "b) values", "c) items", "d) elements", "e) get_values"],
        "answer": "b) values",
        "exp": "`values()` 메서드는 딕셔너리의 값들로 구성된 dict_values 객체를 반환합니다."
    },
    {
        "num": 22,
        "title": "루프의 다음 회차로 건너뛰는 제어문",
        "question": "특정 조건을 만족할 때 반복문의 남아있는 아래 코드를 실행하지 않고 바로 다음 루프로 넘어가게 하는 제어문은?",
        "code": "for i in range(5):\n    if i == 2:\n        (가)\n    print(i)",
        "options": ["a) break", "b) continue", "c) pass", "d) skip", "e) next"],
        "answer": "b) continue",
        "exp": "`continue`문은 현재 루프의 남은 구문을 건너뛰고 바로 다음 반복 단계로 진행합니다."
    },
    {
        "num": 23,
        "title": "무한 루프(while True) 조건식 구조",
        "question": "조건이 항상 참인 무한 루프를 만드는 파이썬 키워드는?",
        "code": "count = 10\nwhile (가):\n    if count == 0:\n        break\n    count -= 1",
        "options": ["a) 1 == 0", "b) True", "c) False", "d) None", "e) count"],
        "answer": "b) True",
        "exp": "파이썬에서 `while True:` 구문은 탈출 조건(`break`)을 만날 때까지 영구히 반복되는 무한 루프를 만듭니다."
    },
    {
        "num": 24,
        "title": "자료형 타입을 엄격히 비교하는 수식",
        "question": "변수의 자료형이 정확히 정수형(int)인지 엄격하게 비교하는 조건 수식은?",
        "code": "item = True\nif (가):\n    print(\"정수입니다.\")",
        "options": ["a) isinstance(item, int)", "b) type(item) == int", "c) typeof(item) == 'int'", "d) item.isint()", "e) is_integer(item)"],
        "answer": "b) type(item) == int",
        "exp": "`bool` 타입은 `int`의 하위 클래스이므로 `isinstance` 사용 시 True도 정수로 간주됩니다. 엄격히 정수만 구별하려면 `type(item) == int`를 사용합니다."
    },
    {
        "num": 25,
        "title": "2차원 리스트 행(row) 순회 수식",
        "question": "2차원 리스트의 각 행(1차원 리스트)을 차례대로 꺼내오기 위한 바깥쪽 for문 변수 수식은?",
        "code": "matrix = [[1, 2], [3, 4], [5, 6]]\nfor (가) in matrix:\n    for val in row:\n        print(val)",
        "options": ["a) row", "b) val", "c) i, j", "d) key", "e) matrix[row]"],
        "answer": "a) row",
        "exp": "2차원 리스트를 순회할 때 바깥쪽 for문은 행 단위(리스트)를 꺼내므로 변수명을 `row` 등으로 작성합니다."
    }
]

# 세션 상태 초기화
if "score" not in st.session_state:
    st.session_state.score = 0
if "answered" not in st.session_state:
    st.session_state.answered = [False] * len(quiz_data)
if "user_choices" not in st.session_state:
    st.session_state.user_choices = [None] * len(quiz_data)

st.title("🐍 파이썬 기초 25제 코드 문법/수식 퀴즈")
st.caption("출력 결과 계산이 아닌 코드 빈칸 채우기 및 조건 수식 중심 문제")
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