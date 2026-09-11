
import streamlit as st
import random

st.set_page_config(
    page_title="9월 1일 파이썬 복습 퀴즈",
    page_icon="🐍",
    layout="centered"
)

QUESTIONS = [
    {
        "q": "파이썬은 어떤 방식으로 코드를 실행하는 언어인가요?",
        "options": ["컴파일 방식", "인터프리터 방식", "수동 실행 방식", "하드웨어 방식"],
        "answer": 1,
        "explanation": "파이썬은 일반적으로 인터프리터 방식으로 코드를 한 줄씩 해석하고 실행합니다."
    },
    {
        "q": "프로그램의 실행 흐름을 여러 방향으로 나누는 것을 무엇이라고 하나요?",
        "options": ["반복", "분기", "형변환", "정렬"],
        "answer": 1,
        "explanation": "조건에 따라 실행할 내용을 나누는 것을 분기라고 합니다. 파이썬에서는 if문을 사용합니다."
    },
    {
        "q": "if문의 조건이 False일 때 다른 조건을 검사하기 위해 사용하는 키워드는?",
        "options": ["for", "elif", "while", "append"],
        "answer": 1,
        "explanation": "elif는 앞의 if 조건이 False일 때 다른 조건을 검사합니다."
    },
    {
        "q": "Boolean 자료형이 가질 수 있는 값은?",
        "options": ["0과 1만", "문자열만", "True와 False", "양수와 음수"],
        "answer": 2,
        "explanation": "Boolean은 참과 거짓을 나타내며 파이썬에서는 True와 False를 사용합니다."
    },
    {
        "q": "다음 중 '같다'를 비교하는 연산자는?",
        "options": ["=", "==", "!=", ">="],
        "answer": 1,
        "explanation": "==는 두 값이 같은지 비교합니다. =는 변수에 값을 할당할 때 사용합니다."
    },
    {
        "q": "10 <= 100의 결과는?",
        "options": ["True", "False", "10", "100"],
        "answer": 0,
        "explanation": "10은 100보다 작으므로 10 <= 100은 True입니다."
    },
    {
        "q": "다음 중 논리 연산자가 아닌 것은?",
        "options": ["and", "or", "not", "append"],
        "answer": 3,
        "explanation": "and, or, not은 논리 연산자이고 append는 리스트에 요소를 추가하는 메서드입니다."
    },
    {
        "q": "input()으로 입력받은 값은 기본적으로 어떤 자료형인가요?",
        "options": ["int", "float", "str", "bool"],
        "answer": 2,
        "explanation": "input()은 사용자가 입력한 값을 문자열(str)로 반환합니다."
    },
    {
        "q": "문자열을 정수로 형변환할 때 사용하는 함수는?",
        "options": ["str()", "int()", "bool()", "list()"],
        "answer": 1,
        "explanation": "int()를 사용하면 문자열 등의 값을 정수형으로 변환할 수 있습니다."
    },
    {
        "q": "같은 작업을 반복적으로 수행하도록 만드는 제어문은?",
        "options": ["반복문", "조건문", "변수", "주석"],
        "answer": 0,
        "explanation": "반복문은 같은 작업을 자동으로 반복 수행하도록 합니다."
    },
    {
        "q": "반복할 범위가 정해져 있을 때 주로 사용하는 반복문은?",
        "options": ["if", "for", "while", "elif"],
        "answer": 1,
        "explanation": "for문은 반복할 대상이나 범위가 정해져 있을 때 사용하기 좋습니다."
    },
    {
        "q": "특정 조건이 True인 동안 계속 반복하는 반복문은?",
        "options": ["for", "if", "while", "elif"],
        "answer": 2,
        "explanation": "while문은 조건이 True인 동안 반복합니다."
    },
    {
        "q": "while문에서 조건이 계속 True라서 반복이 끝나지 않는 것을 무엇이라고 하나요?",
        "options": ["분기", "무한 루프", "형변환", "인덱싱"],
        "answer": 1,
        "explanation": "반복을 멈출 조건이 없거나 계속 True라면 무한 루프가 발생할 수 있습니다."
    },
    {
        "q": "파이썬 리스트는 어떤 기호로 묶나요?",
        "options": ["()", "{}", "[]", "<>"],
        "answer": 2,
        "explanation": "리스트는 대괄호 []를 사용합니다. 예: [10, 20, 30]"
    },
    {
        "q": "리스트에서 첫 번째 요소의 인덱스는 몇 번인가요?",
        "options": ["0", "1", "-1", "첫 번째에는 인덱스가 없다"],
        "answer": 0,
        "explanation": "파이썬의 인덱스는 0부터 시작합니다."
    },
    {
        "q": "리스트 안에 들어 있는 각각의 데이터를 무엇이라고 하나요?",
        "options": ["인덱스", "요소(Element)", "연산자", "피연산자"],
        "answer": 1,
        "explanation": "리스트 내부에 들어 있는 각각의 데이터를 요소(Element)라고 합니다."
    },
    {
        "q": "리스트의 맨 마지막에 요소를 추가하는 메서드는?",
        "options": ["insert()", "append()", "remove()", "clear()"],
        "answer": 1,
        "explanation": "append()는 리스트의 끝에 요소 하나를 추가합니다."
    },
    {
        "q": "insert()의 올바른 형태는?",
        "options": ["insert(값)", "insert(인덱스, 값)", "insert(값, 인덱스)", "insert()만 사용"],
        "answer": 1,
        "explanation": "insert(인덱스, 값) 형태로 원하는 위치에 요소를 삽입합니다."
    },
    {
        "q": "remove()는 같은 값이 여러 개 있을 때 어떻게 삭제하나요?",
        "options": ["모두 삭제", "가장 먼저 발견되는 하나를 삭제", "마지막 하나만 삭제", "삭제하지 않음"],
        "answer": 1,
        "explanation": "remove(값)는 해당 값을 찾았을 때 가장 먼저 발견되는 요소 하나만 삭제합니다."
    },
    {
        "q": "리스트의 모든 요소를 삭제하는 메서드는?",
        "options": ["pop()", "remove()", "clear()", "del()"],
        "answer": 2,
        "explanation": "clear()는 리스트 안의 모든 요소를 제거하여 빈 리스트로 만듭니다."
    },
    {
        "q": "pop()의 특징으로 가장 알맞은 것은?",
        "options": ["값을 추가한다", "요소를 꺼내면서 삭제한다", "리스트를 정렬한다", "모든 요소를 삭제한다"],
        "answer": 1,
        "explanation": "pop()은 지정한 인덱스의 요소를 리스트에서 삭제하면서 그 값을 반환합니다."
    },
    {
        "q": "리스트를 오름차순으로 정렬하는 메서드는?",
        "options": ["sort()", "reverse()", "clear()", "extend()"],
        "answer": 0,
        "explanation": "sort()는 기본적으로 오름차순으로 리스트를 정렬합니다."
    },
    {
        "q": "리스트를 내림차순으로 정렬하려면?",
        "options": ["sort(False)", "sort(reverse=True)", "reverse=False", "descending()"],
        "answer": 1,
        "explanation": "sort(reverse=True)를 사용하면 내림차순으로 정렬됩니다."
    },
    {
        "q": "CRUD의 R은 무엇을 의미하나요?",
        "options": ["Create", "Read", "Update", "Delete"],
        "answer": 1,
        "explanation": "CRUD는 Create(생성), Read(조회), Update(수정), Delete(삭제)의 약자입니다."
    },
    {
        "q": "다음 코드의 결과는 무엇인가요?\n\nnumbers = [10, 20, 30]\nprint(numbers[1])",
        "options": ["10", "20", "30", "오류"],
        "answer": 1,
        "explanation": "인덱스는 0부터 시작하므로 numbers[1]은 두 번째 요소인 20입니다."
    },
    {
        "q": "다음 중 두 리스트를 합쳐 새로운 리스트를 만들 때 사용할 수 있는 것은?",
        "options": ["+", "-", "%", "=="],
        "answer": 0,
        "explanation": "리스트끼리 + 연산자를 사용하면 두 리스트를 합친 새로운 리스트가 만들어집니다."
    },
    {
        "q": "extend()의 역할은?",
        "options": ["리스트를 비운다", "기존 리스트에 다른 리스트의 요소를 추가한다", "요소 하나를 삭제한다", "정렬한다"],
        "answer": 1,
        "explanation": "extend()는 기존 리스트에 다른 리스트의 요소들을 이어 붙여 리스트를 확장합니다."
    },
    {
        "q": "연산의 대상이 되는 값을 무엇이라고 하나요?",
        "options": ["연산자", "피연산자", "키워드", "인덱스"],
        "answer": 1,
        "explanation": "연산을 당하는 대상이 피연산자(Operand)입니다. 예: 3 + 5에서 3과 5."
    },
    {
        "q": "3 + 5에서 '+'는 무엇인가요?",
        "options": ["피연산자", "연산자", "요소", "인덱스"],
        "answer": 1,
        "explanation": "+는 두 값을 더하는 연산자입니다."
    },
    {
        "q": "format()에서 {}는 무엇을 넣는 자리로 생각하면 쉬울까요?",
        "options": ["주석", "변수의 값", "인덱스만", "조건문"],
        "answer": 1,
        "explanation": "'{}'.format(값) 형태에서 {}는 format에 전달한 값이 들어가는 자리입니다."
    },
    {
        "q": "현재 날짜와 시간을 가져올 때 사용할 수 있는 모듈은?",
        "options": ["random", "datetime", "list", "boolean"],
        "answer": 1,
        "explanation": "import datetime 후 datetime.datetime.now()를 사용하면 현재 날짜와 시간을 가져올 수 있습니다."
    },
]

def init_quiz():
    st.session_state.questions = random.sample(QUESTIONS, len(QUESTIONS))
    st.session_state.current = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.selected = None
    st.session_state.finished = False
    st.session_state.total = min(st.session_state.get("quiz_count", 15), len(QUESTIONS))

if "questions" not in st.session_state:
    st.session_state.quiz_count = 15
    init_quiz()

st.title("🐍 9월 1일 파이썬 복습 퀴즈")
st.caption("오늘 배운 조건문 · 반복문 · 리스트 · 연산자 · 형변환을 퀴즈로 복습해보세요!")

if st.session_state.finished:
    st.success("🎉 퀴즈 완료!")
    total = st.session_state.total
    score = st.session_state.score
    percent = round(score / total * 100)

    st.metric("점수", f"{score} / {total}")
    st.progress(score / total if total else 0)

    if percent == 100:
        st.balloons()
        st.write("🏆 완벽해요! 오늘 배운 내용을 아주 잘 이해하고 있어요.")
    elif percent >= 80:
        st.write("👏 잘했어요! 조금만 더 복습하면 완벽합니다.")
    elif percent >= 60:
        st.write("💪 좋아요! 틀린 문제의 해설을 다시 확인해보세요.")
    else:
        st.write("📚 괜찮아요! 해설을 보면서 다시 풀어보면 됩니다.")

    if st.button("🔄 처음부터 다시 풀기", use_container_width=True):
        init_quiz()
        st.rerun()

    st.stop()

q_index = st.session_state.current
q = st.session_state.questions[q_index]
total = st.session_state.total

st.progress((q_index) / total)
st.write(f"### 문제 {q_index + 1} / {total}")
st.write(q["q"])

if not st.session_state.answered:
    selected = st.radio(
        "정답을 선택하세요.",
        q["options"],
        index=None,
        key=f"choice_{q_index}"
    )

    if st.button("✅ 정답 확인", type="primary", use_container_width=True):
        if selected is None:
            st.warning("답을 하나 선택해주세요!")
        else:
            st.session_state.selected = q["options"].index(selected)
            st.session_state.answered = True
            if st.session_state.selected == q["answer"]:
                st.session_state.score += 1
            st.rerun()
else:
    selected = st.session_state.selected
    if selected == q["answer"]:
        st.success("🎉 정답입니다!")
    else:
        st.error(f"❌ 아쉬워요! 정답은 **{q['options'][q['answer']]}** 입니다.")

    st.info(f"💡 해설: {q['explanation']}")

    if q_index + 1 < total:
        if st.button("➡️ 다음 문제", type="primary", use_container_width=True):
            st.session_state.current += 1
            st.session_state.answered = False
            st.session_state.selected = None
            st.rerun()
    else:
        if st.button("🏁 결과 보기", type="primary", use_container_width=True):
            st.session_state.finished = True
            st.rerun()

with st.sidebar:
    st.header("⚙️ 퀴즈 설정")
    new_count = st.slider(
        "문제 수",
        min_value=5,
        max_value=len(QUESTIONS),
        value=st.session_state.quiz_count,
        step=5
    )

    if new_count != st.session_state.quiz_count:
        st.session_state.quiz_count = new_count

    if st.button("🔄 새 퀴즈 시작", use_container_width=True):
        init_quiz()
        st.rerun()

    st.divider()
    st.write("### 📌 포함된 내용")
    st.write("• if / elif / else")
    st.write("• True / False")
    st.write("• 비교·논리·산술 연산자")
    st.write("• 형변환")
    st.write("• for / while")
    st.write("• 무한 루프")
    st.write("• 리스트 / 인덱스 / 요소")
    st.write("• append / insert / extend")
    st.write("• remove / pop / clear / del")
    st.write("• sort / CRUD")
    st.write("• format / datetime")
