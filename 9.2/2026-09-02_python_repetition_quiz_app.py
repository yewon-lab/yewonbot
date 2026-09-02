import streamlit as st

st.set_page_config(page_title="🐍 Python 반복문 & 자료구조 정복 테스트", page_icon="🐍", layout="centered")

QUESTIONS = [
    # level, question, options, answer_index, explanation
    ("LEVEL 1", "`for`문의 역할은?", ["데이터를 한 번만 출력", "같은 작업을 여러 번 반복", "숫자를 계산", "데이터를 삭제"], 1,
     "`for`문은 반복 가능한 데이터를 하나씩 꺼내 같은 작업을 반복할 때 사용합니다."),
    ("LEVEL 1", "다음 코드에서 `number`의 역할은?", ["반복 횟수를 정하는 함수", "반복할 때마다 값을 받아주는 변수", "리스트를 만드는 변수", "반복문을 종료하는 변수"], 1,
     "`number`는 반복할 때마다 `range(3)`에서 나온 값을 하나씩 받아주는 반복 변수입니다."),
    ("LEVEL 1", "`i`를 `number`로 바꿔도 될까?", ["O", "X"], 0,
     "가능합니다. `i`는 특별한 이름이 아니며, 원하는 변수 이름을 사용할 수 있습니다."),
    ("LEVEL 1", "`range(5)`가 만들어내는 숫자는?", ["1, 2, 3, 4, 5", "0, 1, 2, 3, 4", "0, 1, 2, 3, 4, 5", "5"], 1,
     "`range(5)`는 0부터 시작해서 5 직전까지인 0, 1, 2, 3, 4를 만듭니다."),
    ("LEVEL 1", "`for i in range(7): print('안녕')`에서 '안녕'은 몇 번 출력될까?", ["5번", "6번", "7번", "8번"], 2,
     "`range(7)`에는 0~6까지 7개의 값이 있으므로 7번 반복됩니다. `i`에는 0, 1, 2, 3, 4, 5, 6이 들어갑니다."),

    ("LEVEL 2", "`for i in range(4): print(i)`의 출력은?", ["0, 1, 2, 3", "1, 2, 3, 4", "0, 1, 2, 3, 4", "4"], 0,
     "`range(4)`는 0부터 3까지입니다."),
    ("LEVEL 2", "`for i in range(2, 7): print(i)`의 출력은?", ["2, 3, 4, 5, 6", "2, 3, 4, 5, 6, 7", "1, 2, 3, 4, 5, 6", "7, 6, 5, 4, 3"], 0,
     "`range(시작, 끝)`에서 끝값은 포함하지 않습니다. 따라서 2~6입니다."),
    ("LEVEL 2", "`range(5, 0, -1)`의 출력은?", ["5, 4, 3, 2, 1", "5, 4, 3, 2, 1, 0", "0, 1, 2, 3, 4", "5, 3, 1"], 0,
     "증가폭이 -1이므로 5에서 1까지 내려갑니다. 끝값 0은 포함하지 않습니다."),
    ("LEVEL 2", "5, 4, 3, 2, 1, 0을 출력하려면 `range(5, ???, -1)`의 ???는?", ["0", "-1", "1", "5"], 1,
     "끝값은 포함되지 않으므로 0까지 포함하려면 끝을 -1로 설정해야 합니다."),

    ("LEVEL 3", "[10, 20, 30, 40, 50]에서 30의 인덱스는?", ["1", "2", "3", "30"], 1,
     "인덱스는 0부터 시작하므로 10=0, 20=1, 30=2입니다."),
    ("LEVEL 3", "`numbers = [10,20,30,40,50]`일 때 `numbers[2]`의 결과는?", ["20", "30", "40", "50"], 1,
     "인덱스 2는 세 번째 값인 30을 가리킵니다."),
    ("LEVEL 3", "리스트의 첫 번째 값 10을 가져오는 코드는?", ["numbers[0]", "numbers[1]", "numbers[-1]", "numbers[10]"], 0,
     "리스트 인덱스는 0부터 시작하므로 첫 번째 값은 [0]입니다."),
    ("LEVEL 3", "리스트의 마지막 값 50을 가져오는 코드는?", ["numbers[4]", "numbers[5]", "numbers[-1]", "①과 ③ 모두 가능"], 3,
     "5개짜리 리스트의 마지막 인덱스는 4이고, 음수 인덱스 -1도 마지막 값을 의미합니다."),
    ("LEVEL 3", "`for number in [10,20,30]: print(number)`의 출력은?", ["10, 20, 30", "0, 1, 2", "[10,20,30]", "30, 20, 10"], 0,
     "리스트를 직접 반복하면 요소가 하나씩 반복 변수에 들어갑니다."),
    ("LEVEL 3", "위 반복문에서 첫 번째/두 번째/세 번째 반복의 `number` 값은?", ["10 → 20 → 30", "0 → 1 → 2", "10 → 30 → 20", "[10,20,30]"], 0,
     "첫 번째 요소부터 순서대로 10, 20, 30이 들어갑니다."),

    ("LEVEL 4", "`for character in 'ABC': print(character)`의 출력은?", ["ABC 한 줄", "A, B, C가 각각 한 줄", "0, 1, 2", "오류"], 1,
     "문자열도 반복 가능한 자료이므로 문자를 하나씩 꺼낼 수 있습니다."),
    ("LEVEL 4", "'안녕하세요'는 리스트이기 때문에 for문으로 반복할 수 있다.", ["O", "X"], 1,
     "문자열은 리스트가 아닙니다. 하지만 문자열도 반복 가능한 자료이므로 for문으로 문자 하나씩 반복할 수 있습니다."),

    ("LEVEL 5", "`reversed([10,20,30,40])`를 for문으로 출력하면?", ["10,20,30,40", "40,30,20,10", "30,20", "오류"], 1,
     "`reversed()`는 반복 가능한 자료를 역순으로 순회하게 해줍니다."),
    ("LEVEL 5", "`numbers[::-1]`의 결과는?", ["[10,20,30,40]", "[40,30,20,10]", "[30,20]", "오류"], 1,
     "슬라이싱에서 간격을 -1로 하면 뒤에서부터 전체를 가져옵니다."),
    ("LEVEL 5", "`numbers[::-1]`에서 시작, 끝, 간격은?", ["시작=처음, 끝=마지막, 간격=1", "시작=자동, 끝=자동, 간격=-1", "시작=-1, 끝=0, 간격=1", "모두 0"], 1,
     "시작과 끝을 비워두면 전체 범위를 사용하고, -1 간격으로 역순이 됩니다."),

    ("LEVEL 6", "[[1,2,3],[4,5,6],[7,8]]`의 구조는?", ["숫자 하나", "문자열", "리스트 안에 리스트", "딕셔너리"], 2,
     "바깥 리스트의 각 요소가 또 하나의 리스트이므로 중첩 리스트입니다."),
    ("LEVEL 6", "첫 번째 for의 `items`에는 무엇이 들어갈까?", ["1,2,3 → 4,5,6 → 7,8", "1 → 2 → 3", "[1,2,3] → [4,5,6] → [7,8]", "인덱스 0 → 1 → 2"], 2,
     "첫 번째 for는 바깥 리스트의 요소인 '각 안쪽 리스트'를 하나씩 가져옵니다."),
    ("LEVEL 6", "`for items in list_of_list: for item in items: print(items)`의 출력은?", ["1,2,3,4,5,6,7,8", "[1,2,3] 세 번, [4,5,6] 세 번, [7,8] 두 번", "각 안쪽 리스트가 그 안의 요소 수만큼 반복 출력", "오류"], 2,
     "`print(items)`는 숫자 하나가 아니라 현재의 안쪽 리스트를 출력하므로 각 리스트가 자기 요소 개수만큼 반복됩니다."),
    ("LEVEL 6", "같은 코드에서 `print(item)`으로 바꾸면?", ["1,2,3,4,5,6,7,8", "[1,2,3],[4,5,6],[7,8]", "0,1,2", "오류"], 0,
     "두 번째 for가 안쪽 리스트의 요소를 하나씩 꺼내므로 숫자가 순서대로 출력됩니다."),
    ("LEVEL 6", "중첩 for에서 첫 번째/두 번째 for의 역할은?", ["첫 번째=숫자, 두 번째=리스트", "첫 번째=안쪽 리스트, 두 번째=그 리스트 안의 요소", "둘 다 같은 역할", "첫 번째=Key, 두 번째=Value"], 1,
     "바깥 for가 안쪽 리스트를 가져오고, 안쪽 for가 그 안쪽 리스트의 요소를 하나씩 가져옵니다."),

    ("LEVEL 7", "dictionary에서 Key와 Value의 올바른 짝은?", ['name → "7D 건조 망고"', 'type → "당절임"', 'origin → "필리핀"', "위의 세 가지 모두 맞음"], 3,
     "딕셔너리는 Key와 Value를 한 쌍으로 저장합니다."),
    ("LEVEL 7", "`dictionary['name']`의 결과는?", ["name", "7D 건조 망고", "당절임", "필리핀"], 1,
     "Key 'name'에 연결된 Value를 가져옵니다."),
    ("LEVEL 7", "`dictionary['origin']`의 결과는?", ["origin", "7D 건조 망고", "당절임", "필리핀"], 3,
     "Key 'origin'에 연결된 Value는 '필리핀'입니다."),
    ("LEVEL 7", "`'age': 20`에서 Key와 Value는?", ["Key=20, Value='age'", "Key='age', Value=20", "둘 다 Key", "둘 다 Value"], 1,
     "콜론 왼쪽이 Key, 오른쪽이 Value입니다."),
    ("LEVEL 7", "리스트와 딕셔너리는 각각 무엇으로 데이터를 관리할까?", ["리스트=Key, 딕셔너리=인덱스", "리스트=인덱스, 딕셔너리=Key", "둘 다 인덱스", "둘 다 Key"], 1,
     "리스트는 위치를 나타내는 인덱스, 딕셔너리는 Key로 값을 찾습니다."),

    ("LEVEL 8", "`person = {'name':'철수'}`에 age 20을 추가하는 코드는?", ["person['age'] = 20", "person[20] = 'age'", "person.add('age',20)", "person = 20"], 0,
     "새로운 Key에 값을 할당하면 딕셔너리에 데이터가 추가됩니다."),
    ("LEVEL 8", "`person['name'] = '영희'` 실행 후 name의 값은?", ["철수", "영희", "name", "오류"], 1,
     "이미 존재하는 Key에 새 값을 할당하면 기존 Value가 수정됩니다."),
    ("LEVEL 8", "딕셔너리에서 age를 삭제하는 방법은?", ["del person['age']", "person.delete('age')", "remove person['age']", "person['age'] = delete"], 0,
     "`del 딕셔너리[Key]` 형태로 해당 항목을 삭제할 수 있습니다."),

    ("LEVEL 9", "`'name' in person`의 결과는?", ["True", "False"], 0,
     "딕셔너리에서 `in`은 기본적으로 Key가 존재하는지 확인합니다."),
    ("LEVEL 9", "`'height' in person`의 결과는?", ["True", "False"], 1,
     "person에 height라는 Key가 없으므로 False입니다."),
    ("LEVEL 9", "`if key in dictionary:`의 의미는?", ["Key가 딕셔너리에 존재하는지 확인", "Value가 숫자인지 확인", "Key를 삭제", "딕셔너리를 반복"], 0,
     "`in`은 포함 여부를 확인합니다. 딕셔너리에서는 기본적으로 Key의 존재 여부를 검사합니다."),

    ("LEVEL 10", "`for key in dictionary`에서 key에 들어가는 것은?", ["Value", "Key", "인덱스", "딕셔너리 전체"], 1,
     "딕셔너리를 그대로 for문에 넣으면 Key가 하나씩 반복 변수에 들어갑니다."),
    ("LEVEL 10", "현재 `key = 'name'`일 때 `dictionary[key]`와 같은 코드는?", ['dictionary["type"]', 'dictionary["name"]', 'dictionary["origin"]'], 1,
     "변수 key 안에 'name'이 들어 있으므로 dictionary[key]는 dictionary['name']과 같습니다."),
    ("LEVEL 10", "`for key in dictionary:`의 `:`와 `print(key, ':', dictionary[key])`의 `':'` 차이는?", ["둘 다 문법 기호", "첫 번째는 for문 블록 시작을 나타내고, 두 번째는 출력할 문자열 ':'", "첫 번째는 문자열, 두 번째는 블록 시작", "둘 다 오류"], 1,
     "문장 끝의 콜론은 코드 블록 시작을 알리는 문법이고, 따옴표 안의 ':'는 그냥 출력하는 문자열입니다."),

    ("FINAL BOSS", "다음 코드의 최종 목적은?", ["딕셔너리 삭제", "딕셔너리의 Key와 그에 해당하는 Value를 함께 출력", "리스트 역순 출력", "숫자 계산"], 1,
     "for로 Key를 하나씩 꺼내고 dictionary[key]로 그 Key의 Value를 찾아 Key : Value 형태로 출력합니다."),
    ("FINAL BOSS", "`ingredient`의 Value는 어떤 자료형인가?", ["정수", "문자열", "리스트", "딕셔너리"], 2,
     "ingredient에 연결된 값은 ['망고', '설탕', '치자황색소']이므로 리스트입니다."),

    ("BONUS", "`numbers = [15,25,35,45,55]`를 for로 하나씩 출력하려면?", ["for number in numbers: print(number)", "for number in range(numbers): print(number)", "for numbers in number: print(numbers)", "print(numbers[5])"], 0,
     "range 없이 리스트 자체를 반복하면 요소가 하나씩 number에 들어갑니다."),
    ("BONUS", "위 리스트를 reversed()로 역순 출력하려면?", ["for number in reversed(numbers): print(number)", "for number in reverse(numbers): print(number)", "for number in numbers.reverse(): print(number)", "reversed(numbers) = print(number)"], 0,
     "`reversed(numbers)`를 for문에서 순회하면 55부터 15까지 출력됩니다."),
    ("BONUS", "person의 Key와 Value를 `name : 철수`처럼 출력하는 가장 적절한 코드는?", ["for key in person: print(key, ':', person[key])", "for value in person: print(value)", "print(person[0])", "for key in range(person): print(key)"], 0,
     "Key를 반복 변수로 받고 person[key]로 해당 Value를 가져오면 됩니다."),
]

st.title("🐍 Python 반복문 & 자료구조 기초 정복 테스트")
st.caption("반복문 · 리스트 · 인덱스 · 슬라이싱 · 중첩 for · 딕셔너리 · CRUD · in")

if "answers" not in st.session_state:
    st.session_state.answers = {}
if "submitted" not in st.session_state:
    st.session_state.submitted = False

st.info(f"총 {len(QUESTIONS)}문제 · 먼저 풀고 마지막에 채점하세요!")

with st.sidebar:
    st.header("📚 문제 범위")
    levels = {}
    for level, *_ in QUESTIONS:
        levels[level] = levels.get(level, 0) + 1
    for level, count in levels.items():
        st.write(f"**{level}** — {count}문제")
    st.divider()
    st.write("💡 정답 제출 후 문제별 해설을 볼 수 있어요.")

for idx, (level, q, options, answer, explanation) in enumerate(QUESTIONS, start=1):
    st.subheader(f"{idx}. {q}")
    st.caption(level)
    current = st.session_state.answers.get(idx)
    default_index = current if current is not None else None
    choice = st.radio(
        "답을 선택하세요",
        options,
        index=default_index,
        key=f"q_{idx}",
        label_visibility="collapsed"
    )
    if choice is not None:
        st.session_state.answers[idx] = options.index(choice)

st.divider()

if st.button("📝 전체 채점하기", type="primary", use_container_width=True):
    st.session_state.submitted = True

if st.session_state.submitted:
    correct = sum(st.session_state.answers.get(i) == ans for i, (_, _, _, ans, _) in enumerate(QUESTIONS, start=1))
    total = len(QUESTIONS)
    score = round(correct / total * 100)
    st.header("🏆 채점 결과")
    st.metric("점수", f"{score}점", f"{correct}/{total} 정답")

    if score >= 90:
        st.success("🔥 거의 정복했어요! 이제 직접 코드를 작성해보면 됩니다.")
    elif score >= 70:
        st.info("👍 기본기는 잘 잡혔어요. 틀린 문제의 해설을 다시 확인해보세요.")
    else:
        st.warning("🌱 괜찮아요! 특히 range, 인덱스, Key/Value를 다시 연습하면 좋아요.")

    st.subheader("📖 답안지 & 해설")
    for idx, (level, q, options, ans, explanation) in enumerate(QUESTIONS, start=1):
        user = st.session_state.answers.get(idx)
        if user == ans:
            st.success(f"{idx}번 ✅ 정답: {options[ans]}")
        else:
            user_text = options[user] if user is not None else "미응답"
            st.error(f"{idx}번 ❌ 내 답: {user_text}  |  정답: {options[ans]}")
        st.write(f"💡 **해설:** {explanation}")

    st.divider()
    st.subheader("🎯 복습 포인트")
    st.write("""
- `for 변수 in 반복가능한자료:` → 자료에서 값을 하나씩 꺼내 반복
- `range(끝)` → 0부터 끝 직전까지
- 리스트 → 인덱스로 접근, 첫 번째는 0
- `reversed()` / `[::-1]` → 역순
- 중첩 리스트 → 바깥 for는 안쪽 리스트, 안쪽 for는 요소
- 딕셔너리 → Key와 Value의 쌍
- `dictionary[key]` → 해당 Key의 Value
- `in` → 딕셔너리에서는 기본적으로 Key 존재 여부 확인
- CRUD → 추가/수정/삭제/조회
- 코드 끝의 `:`와 문자열 `":"`은 완전히 다름
""")

if st.button("🔄 다시 풀기", use_container_width=True):
    st.session_state.answers = {}
    st.session_state.submitted = False
    st.rerun()
