import streamlit as st

st.set_page_config(
    page_title="🐍 Python 새 문제 응용 테스트",
    page_icon="🐍",
    layout="centered"
)

QUESTIONS = [(1, 'for 응용', "친구 이름이 들어 있는 리스트가 있습니다. 모든 친구 이름 뒤에 '님'을 붙여 출력하려면 어떤 for문을 작성할지 코드로 작성하세요.\n\nfriends = ['민수', '지수', '철수']", "for friend in friends:\n    print(friend + '님')", '리스트의 요소를 하나씩 꺼내 문자열을 이어 붙입니다.'), (2, 'for 응용', "다음 코드에서 숫자만 출력하지 않고 '현재 숫자: 10'처럼 출력하려면 코드를 완성하세요.\n\nnumbers = [10, 20, 30]\nfor number in numbers:\n    # 여기를 작성", "for number in numbers:\n    print('현재 숫자:', number)", '반복 변수와 문자열을 함께 print할 수 있습니다.'), (3, 'for + range 응용', '1부터 10까지의 숫자 중 짝수만 출력하는 코드를 작성하세요. `for`와 `range()`를 사용하세요.', 'for number in range(1, 11):\n    if number % 2 == 0:\n        print(number)', 'range로 1~10을 만들고 나머지 연산으로 짝수를 구합니다.'), (4, 'range 사고력', '1부터 10까지의 숫자를 거꾸로 10, 9, ..., 1 순서로 출력하는 코드를 작성하세요. `reversed()`는 사용하지 마세요.', 'for number in range(10, 0, -1):\n    print(number)', 'range의 시작, 끝, 간격을 이용해 감소하는 반복을 만듭니다.'), (5, 'range 사고력', '3, 6, 9, 12, 15를 출력하려면 어떤 range를 사용할 수 있을까요? 코드를 작성하고 각 숫자가 어떻게 만들어지는지 설명하세요.', 'for number in range(3, 16, 3):\n    print(number)', '시작 3에서 3씩 증가하고 16 직전까지 반복합니다.'), (6, '리스트 + 인덱스', "다음 리스트에서 두 번째와 네 번째 과일만 출력하는 코드를 작성하세요.\n\nfruits = ['사과', '바나나', '포도', '딸기', '수박']", 'print(fruits[1])\nprint(fruits[3])', '두 번째 요소의 인덱스는 1, 네 번째 요소의 인덱스는 3입니다.'), (7, '리스트 사고력', '다음 리스트의 마지막 두 요소를 슬라이싱으로 가져오는 코드를 작성하세요.\n\nnumbers = [10, 20, 30, 40, 50]', 'print(numbers[-2:])', '마지막 두 요소는 -2부터 끝까지 슬라이싱하면 됩니다.'), (8, '슬라이싱 응용', '다음 리스트에서 가운데 세 값만 슬라이싱으로 가져오세요.\n\nnumbers = [10, 20, 30, 40, 50]', 'print(numbers[1:4])', '인덱스 1부터 4 직전까지이므로 20, 30, 40을 가져옵니다.'), (9, '슬라이싱 응용', '다음 리스트에서 홀수 인덱스에 있는 값만 슬라이싱으로 가져오세요.\n\nnumbers = [0, 10, 20, 30, 40, 50]', 'print(numbers[1::2])', '인덱스 1에서 시작하여 2칸씩 이동하면 홀수 인덱스의 값이 선택됩니다.'), (10, '역순 사고력', "다음 문자열을 뒤집어서 출력하는 코드를 `[::-1]`을 사용해 작성하세요.\n\nword = 'Python'", 'print(word[::-1])', '문자열도 슬라이싱할 수 있으며 간격 -1은 역순을 의미합니다.'), (11, 'reversed 응용', '다음 리스트를 역순으로 순회하면서 각 값에 2를 곱해 출력하세요. 원래 리스트 자체는 변경하지 않습니다.\n\nnumbers = [1, 2, 3, 4]', 'for number in reversed(numbers):\n    print(number * 2)', 'reversed로 역순 순회만 하고 원본 리스트의 값을 직접 변경하지 않습니다.'), (12, '중첩 for 응용', "다음 좌석표의 모든 좌석 번호를 출력하는 코드를 작성하세요.\n\nseats = [['A1', 'A2'], ['B1', 'B2'], ['C1', 'C2']]", 'for row in seats:\n    for seat in row:\n        print(seat)', '바깥 for는 한 줄(row), 안쪽 for는 그 줄의 좌석을 하나씩 가져옵니다.'), (13, '중첩 for 사고력', "다음 데이터에서 각 반의 학생 이름을 모두 출력하세요.\n\nclasses = [['민수', '지수'], ['철수', '영희', '수진']]", 'for students in classes:\n    for student in students:\n        print(student)', '각 반 리스트를 먼저 가져오고 그 안의 학생을 하나씩 가져옵니다.'), (14, '중첩 for', "다음 코드는 무엇을 출력할까요? 출력 결과를 적고 `name`과 `names`의 차이를 설명하세요.\n\nnames = [['A', 'B'], ['C', 'D']]\nfor names in names:\n    for name in names:\n        print(name)", 'A\nB\nC\nD\n\n두 번째 names는 현재 안쪽 리스트를 가리키고, name은 그 안의 요소를 가리킵니다.', '변수 이름을 같은 이름으로 겹쳐 쓰는 것은 피하는 것이 좋으며, 안쪽 리스트와 요소를 구분해 이해해야 합니다.'), (15, '딕셔너리 응용', "상품 딕셔너리에서 `price` 값을 5000으로 변경하는 코드를 작성하세요.\n\nproduct = {'name': '노트', 'price': 3000}", "product['price'] = 5000", '기존 Key에 새 Value를 할당하면 수정됩니다.'), (16, '딕셔너리 응용', "다음 딕셔너리에 재고 수량 `stock: 10`을 추가하는 코드를 작성하세요.\n\nproduct = {'name': '노트', 'price': 3000}", "product['stock'] = 10", '존재하지 않는 Key에 값을 할당하면 새로운 항목이 추가됩니다.'), (17, '딕셔너리 응용', "다음 딕셔너리에서 `email`이 있는 경우에만 그 값을 출력하도록 코드를 작성하세요.\n\nuser = {'name': '민수', 'email': 'minsu@example.com'}", "if 'email' in user:\n    print(user['email'])", 'in으로 Key의 존재 여부를 확인한 뒤 해당 값을 가져옵니다.'), (18, '딕셔너리 응용', "다음 딕셔너리에서 `phone`이 없을 때 '전화번호 없음'을 출력하는 코드를 작성하세요.\n\nuser = {'name': '민수', 'email': 'minsu@example.com'}", "if 'phone' not in user:\n    print('전화번호 없음')", 'not in은 해당 Key가 존재하지 않는지를 확인할 때 사용할 수 있습니다.'), (19, '딕셔너리 + for', "다음 딕셔너리에서 가격이 5000 이상인 상품의 Key와 Value를 출력한다고 생각하고 코드를 작성하세요.\n\nprices = {'사과': 3000, '망고': 7000, '수박': 9000}", "for key in prices:\n    if prices[key] >= 5000:\n        print(key, ':', prices[key])", 'Key를 반복하면서 dictionary[key]로 Value를 확인할 수 있습니다.'), (20, '딕셔너리 + for', "다음 딕셔너리의 모든 Value만 출력하는 코드를 작성하세요. Key는 출력하지 않습니다.\n\nperson = {'name': '철수', 'age': 20, 'city': '서울'}", 'for key in person:\n    print(person[key])', 'Key를 반복 변수로 받고 dictionary[key]를 출력하면 Value만 출력됩니다.'), (21, 'CRUD 사고력', '다음 작업들이 CRUD 중 무엇인지 각각 설명하세요.\n① 새 친구 추가 ② 친구 이름 변경 ③ 친구 정보 삭제 ④ 친구 정보 확인', '① Create(추가) ② Update(수정) ③ Delete(삭제) ④ Read(조회)', 'CRUD는 Create, Read, Update, Delete의 네 가지 기본 데이터 처리입니다.'), (22, 'CRUD 코드', "다음 딕셔너리에서 `age`를 조회하는 코드를 작성하세요.\n\nperson = {'name': '철수', 'age': 20}", "print(person['age'])", '딕셔너리에서 Key로 값을 조회하는 것은 Read에 해당합니다.'), (23, '코드 읽기', '다음 코드가 실행된 후 numbers의 값은 무엇인지 설명하세요.\n\nnumbers = [1, 2, 3]\nfor number in numbers:\n    print(number)\n\nprint(numbers)', '[1, 2, 3]\n\nfor문에서 단순히 요소를 읽어 출력했을 뿐 리스트 자체를 수정하지 않았습니다.', 'for로 값을 읽는 것과 원본 자료를 수정하는 것은 다릅니다.'), (24, '코드 읽기', '다음 두 코드의 차이를 자신의 말로 설명하세요.\n\nA.\nfor number in numbers:\n    print(number)\n\nB.\nfor i in range(len(numbers)):\n    print(numbers[i])', 'A는 리스트의 요소를 직접 하나씩 가져오고, B는 인덱스를 만들어 그 인덱스로 요소를 가져옵니다.', '둘 다 요소를 출력할 수 있지만 반복 변수에 들어오는 대상이 다릅니다.'), (25, '오류 찾기', '다음 코드의 오류를 찾아 올바르게 고치세요.\n\nnumbers = [10, 20, 30]\nfor number in range(numbers):\n    print(number)', 'for number in numbers:\n    print(number)', 'range에는 정수 범위가 필요하므로 리스트 자체를 반복하려면 range를 쓰지 않고 리스트를 직접 순회합니다.'), (26, '오류 찾기', "다음 코드가 왜 원하는 결과를 내지 못하는지 설명하고 수정하세요.\n\nperson = {'name': '철수'}\nprint(person[0])", "print(person['name'])", '딕셔너리는 리스트처럼 숫자 인덱스 0으로 접근하지 않고 Key를 사용합니다.'), (27, '오류 찾기', "다음 코드에서 딕셔너리에 `age`를 추가하려고 했는데 잘못된 부분을 찾아 수정하세요.\n\nperson = {'name': '철수'}\nperson['age'] == 20", "person['age'] = 20", '==는 비교 연산이고, 값을 저장하거나 수정할 때는 =를 사용합니다.'), (28, '통합 문제', '다음 리스트에서 10보다 큰 숫자만 역순으로 출력하는 코드를 작성하세요.\n\nnumbers = [5, 12, 7, 20, 3, 15]', 'for number in reversed(numbers):\n    if number > 10:\n        print(number)', '역순 순회와 조건을 결합한 문제입니다.'), (29, '통합 문제', '다음 중첩 리스트에서 모든 숫자의 합을 구하는 코드를 작성하세요. (힌트: 바깥 for와 안쪽 for가 필요합니다.)\n\nnumbers = [[1, 2], [3, 4], [5, 6]]', 'total = 0\nfor row in numbers:\n    for number in row:\n        total += number\nprint(total)', '중첩 리스트의 모든 요소를 순회하며 누적 변수에 더합니다.'), (30, '최종 응용', "다음 상품 정보에서 Key와 Value를 `상품명 : 노트`처럼 모두 출력하고, `stock`이 있는지도 확인하는 코드를 작성하세요.\n\nproduct = {'상품명': '노트', '가격': 3000, 'stock': 10}", "for key in product:\n    print(key, ':', product[key])\n\nif 'stock' in product:\n    print('재고 정보가 있습니다.')", 'for로 Key와 Value를 함께 출력하고, in으로 stock Key의 존재 여부를 확인합니다.')]
TOTAL = len(QUESTIONS)

st.title("🐍 Python 새 문제 응용 테스트")
st.caption("기존 문제와 겹치지 않는 새로운 응용·서술형 30문제")
st.info("한 번에 한 문제씩 풀고 → 채점 → 모범답안/해설 확인 → 다음 문제로 넘어가세요! 😊")

if "current" not in st.session_state:
    st.session_state.current = 0
if "checked" not in st.session_state:
    st.session_state.checked = False
if "answers" not in st.session_state:
    st.session_state.answers = {}

idx = st.session_state.current
num, level, question, model_answer, explanation = QUESTIONS[idx]

st.progress((idx + 1) / TOTAL)
st.write(f"### 문제 {idx + 1} / {TOTAL}")
st.caption(level)

# 문제와 코드 표시
parts = question.split("\n")
st.write(parts[0])

if len(parts) > 1:
    st.code("\n".join(parts[1:]), language="python")

st.divider()

answer_key = f"answer_{idx}"
user_answer = st.text_area(
    "✍️ 내 답안",
    value=st.session_state.answers.get(answer_key, ""),
    height=180,
    placeholder="자신의 말로 설명하거나 코드를 작성해보세요.",
    disabled=st.session_state.checked,
)

if not st.session_state.checked:
    if st.button("✅ 채점하기", type="primary", use_container_width=True):
        if not user_answer.strip():
            st.warning("먼저 답을 작성해보자! 😊")
        else:
            st.session_state.answers[answer_key] = user_answer
            st.session_state.checked = True
            st.rerun()

else:
    # 답안은 제출 후 고정
    st.write("### 📝 내 답안")
    st.info(st.session_state.answers.get(answer_key, ""))

    st.write("### 📊 자기 채점")
    st.warning("서술형은 컴퓨터가 정답 여부를 완벽하게 판단하기 어려워요. 아래 모범답안과 비교해서 스스로 채점해보세요.")

    st.write("### ✅ 모범답안")
    if any(x in model_answer for x in ["for ", "print(", "if ", "total ="]):
        st.code(model_answer, language="python")
    else:
        st.write(model_answer)

    st.write("### 💡 해설")
    st.write(explanation)

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        if idx > 0:
            if st.button("⬅️ 이전 문제", use_container_width=True):
                st.session_state.current -= 1
                st.session_state.checked = True
                st.rerun()

    with col2:
        if idx < TOTAL - 1:
            if st.button("다음 문제 ➡️", type="primary", use_container_width=True):
                st.session_state.current += 1
                st.session_state.checked = False
                st.rerun()
        else:
            if st.button("🏆 테스트 완료!", type="primary", use_container_width=True):
                st.session_state.current = 0
                st.session_state.checked = False
                st.rerun()

    # 완료 현황
    checked_count = sum(
        1 for i in range(TOTAL)
        if i == idx or f"answer_{i}" in st.session_state.answers
    )
    st.caption(f"진행 상황: {min(checked_count, TOTAL)} / {TOTAL} 문제")

# 처음/마지막 문제 이동
if not st.session_state.checked and idx > 0:
    st.write("")
    if st.button("⬅️ 이전 문제로", use_container_width=True):
        st.session_state.current -= 1
        st.session_state.checked = True
        st.rerun()
