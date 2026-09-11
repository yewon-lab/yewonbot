import streamlit as st

st.set_page_config(page_title='파이썬 기초 코드 완성 퀴즈 1~14', page_icon='🐍')

questions = []
questions.append({'number': 1, 'question': '리스트의 합계를 구하려면 □에 무엇이 들어갈까요?', 'code': 'numbers = [12, 25, 7, 33, 18]\ntotal = 0\n\nfor number in numbers:\n    □\n\nprint(total)', 'options': ['total = number', 'total += number', 'number += total', 'total -= number'], 'answer': 'total += number', 'explanation': 'total += number는 total = total + number와 같습니다. 반복할 때마다 number를 total에 계속 더합니다.'})
questions.append({'number': 2, 'question': '리스트의 평균을 구하려면 □에 무엇이 들어갈까요?', 'code': 'numbers = [10, 20, 30, 40]\ntotal = 0\n\nfor number in numbers:\n    total += number\n\naverage = □\nprint(average)', 'options': ['total * len(numbers)', 'len(numbers) / total', 'total / len(numbers)', 'total - len(numbers)'], 'answer': 'total / len(numbers)', 'explanation': '평균은 전체 합계 ÷ 데이터 개수입니다. len(numbers)는 리스트의 개수를 자동으로 계산하므로 리스트 길이가 바뀌어도 맞춰집니다.'})
questions.append({'number': 3, 'question': '3단을 1부터 9까지 출력하려면 □에 무엇이 들어갈까요?', 'code': 'for i in range(□):\n    print("3 x", i, "=", 3 * i)', 'options': ['0, 9', '1, 9', '1, 10', '3, 10'], 'answer': '1, 10', 'explanation': 'range(1, 10)은 1부터 10 바로 전인 9까지 만듭니다. range의 끝 숫자는 포함되지 않습니다.'})
questions.append({'number': 4, 'question': 'max() 없이 최댓값을 찾을 때 □에 무엇이 들어갈까요?', 'code': 'numbers = [12, 45, 7, 83, 29]\nbig = numbers[0]\n\nfor number in numbers:\n    if number > big:\n        □\n\nprint(big)', 'options': ['number = big', 'big += number', 'number += big', 'big = number'], 'answer': 'big = number', 'explanation': '현재 number가 big보다 크면 새로운 최댓값입니다. 따라서 big에 number를 저장합니다.'})
questions.append({'number': 5, 'question': '딕셔너리의 key를 순회하려면 □에 무엇이 들어갈까요?', 'code': 'character = {"name": "기사", "hp": 200, "level": 5}\n\nfor □ in character:\n    print(key)', 'options': ['key', 'value', 'item', 'character'], 'answer': 'key', 'explanation': '딕셔너리를 for문으로 직접 순회하면 key가 하나씩 나옵니다. 그래서 for key in character가 됩니다.'})
questions.append({'number': 6, 'question': '1부터 5까지 출력하는 while문의 조건은 무엇일까요?', 'code': 'i = 1\n\nwhile □:\n    print(i)\n    i += 1', 'options': ['i < 5', 'i >= 5', 'i == 5', 'i <= 5'], 'answer': 'i <= 5', 'explanation': '5도 출력해야 하므로 i <= 5입니다. 5를 출력한 뒤 i가 6이 되면 조건이 거짓이 됩니다.'})
questions.append({'number': 7, 'question': '리스트에서 짝수만 세려면 □에 무엇이 들어갈까요?', 'code': 'numbers = [3, 8, 15, 22, 7, 40, 11]\ncount = 0\n\nfor number in numbers:\n    if □:\n        count += 1\n\nprint(count)', 'options': ['number / 2 == 0', 'number % 2 == 1', 'number * 2 == 0', 'number % 2 == 0'], 'answer': 'number % 2 == 0', 'explanation': '짝수는 2로 나눈 나머지가 0입니다. %는 나머지를 구하는 연산자입니다.'})
questions.append({'number': 8, 'question': '문자열을 거꾸로 순회하려면 □에 무엇이 들어갈까요?', 'code': 'word = "Python"\n\nfor letter in □:\n    print(letter, end="")', 'options': ['word.reverse()', 'reversed(word)', 'reverse(word)', 'word.reversed()'], 'answer': 'reversed(word)', 'explanation': 'reversed(word)는 문자열을 뒤에서부터 순회하게 합니다. Python은 n, o, h, t, y, P 순서로 읽힙니다.'})
questions.append({'number': 9, 'question': '57을 찾으면 반복문을 완전히 끝내려면 □에 무엇이 들어갈까요?', 'code': 'array = [273, 32, 103, 57, 52]\n\nfor i in range(len(array)):\n    if array[i] == 57:\n        print(i)\n        □', 'options': ['break', 'continue', 'pass', 'print'], 'answer': 'break', 'explanation': 'break는 반복문 전체를 즉시 종료합니다. continue는 현재 반복만 건너뛰고 다음 반복으로 갑니다.'})
questions.append({'number': 10, 'question': 'while문에서 i를 다음 숫자로 증가시키려면 □에 무엇이 들어갈까요?', 'code': 'i = 1\ntotal = 0\n\nwhile i <= 100:\n    total += i\n    □\n\nprint(total)', 'options': ['total += 1', 'i = 1', 'i += 1', 'i -= 1'], 'answer': 'i += 1', 'explanation': 'i += 1은 i = i + 1입니다. i가 1, 2, 3처럼 증가해야 반복이 진행됩니다. 없으면 무한 반복이 됩니다.'})
questions.append({'number': 11, 'question': '2단부터 9단까지 만들려면 바깥쪽 range에 무엇을 넣을까요?', 'code': 'for dan in range(□):\n    for i in range(1, 10):\n        print(dan, "x", i)', 'options': ['1, 9', '2, 9', '3, 10', '2, 10'], 'answer': '2, 10', 'explanation': 'range(2, 10)은 2부터 9까지 만듭니다. 10은 포함되지 않기 때문에 9단까지 정확합니다.'})
questions.append({'number': 12, 'question': '3의 배수인지 확인하려면 □에 무엇이 들어갈까요?', 'code': 'for number in range(1, 31):\n    if □:\n        print("Fizz")', 'options': ['number / 3 == 0', 'number % 3 == 0', 'number % 3 == 1', 'number * 3 == 0'], 'answer': 'number % 3 == 0', 'explanation': '3의 배수는 3으로 나눈 나머지가 0입니다. 그래서 number % 3 == 0을 사용합니다.'})
questions.append({'number': 13, 'question': '짝수만 새로운 리스트에 추가하려면 □에 무엇이 들어갈까요?', 'code': 'numbers = [3, 8, 15, 22, 7, 40, 11, 6]\neven_numbers = []\n\nfor number in numbers:\n    if number % 2 == 0:\n        □\n\nprint(even_numbers)', 'options': ['even_numbers = number', 'number.append(even_numbers)', 'even_numbers.append(number)', 'even_numbers.append(2)'], 'answer': 'even_numbers.append(number)', 'explanation': 'append()는 리스트에 값을 하나 추가합니다. 조건을 만족한 현재 숫자 number를 새 리스트에 넣습니다.'})
questions.append({'number': 14, 'question': '두 리스트의 같은 인덱스 값을 연결하려면 range 안에 무엇을 넣을까요?', 'code': 'key_list = ["name", "hp", "mp", "level"]\nvalue_list = ["기사", 200, 30, 5]\n\ncharacter = {}\n\nfor i in range(□):\n    character[key_list[i]] = value_list[i]\n\nprint(character)', 'options': ['len(key_list) - 1', '4 - 1', 'len(key_list)', 'key_list'], 'answer': 'len(key_list)', 'explanation': 'len(key_list)는 리스트의 현재 개수를 자동으로 알려줍니다. 4개이면 range(4)가 되어 인덱스 0, 1, 2, 3을 모두 사용합니다. 리스트 개수가 바뀌어도 자동으로 맞춰집니다.'})

if 'current' not in st.session_state:
    st.session_state.current = 0
if 'submitted' not in st.session_state:
    st.session_state.submitted = False
if 'score' not in st.session_state:
    st.session_state.score = 0

q = questions[st.session_state.current]
st.title('🐍 파이썬 코드 완성 퀴즈')
st.caption('*** 방식 · 1~14번 · 한 문제씩 풀고 바로 채점')
st.progress((st.session_state.current + 1) / len(questions))
st.markdown(f"## 문제 {q['number']} / {len(questions)}")
st.write(q['question'])
st.code(q['code'], language='python')

target_positions = [0, 2, 1, 3, 0, 3, 1, 2, 0, 2, 3, 1, 2, 0]
correct = q['answer']
wrong = [x for x in q['options'] if x != correct]
pos = target_positions[q['number'] - 1]
display_options = [None] * 4
display_options[pos] = correct
wi = 0
for oi in range(4):
    if display_options[oi] is None:
        display_options[oi] = wrong[wi]
        wi += 1

selected = st.radio('정답을 선택하세요.', display_options, key=f"choice_{q['number']}")

if not st.session_state.submitted:
    if st.button('정답 확인', type='primary', use_container_width=True):
        if selected == q['answer']:
            st.session_state.score += 1
        st.session_state.submitted = True
        st.rerun()
else:
    if selected == q['answer']:
        st.success('🎉 정답입니다!')
    else:
        st.error('❌ 오답입니다!')
    st.info(f"정답: {q['answer']}")
    st.markdown('### 📖 자세한 풀이')
    st.write(q['explanation'])
    if st.session_state.current < len(questions) - 1:
        if st.button('다음 문제 →', type='primary', use_container_width=True):
            st.session_state.current += 1
            st.session_state.submitted = False
            st.rerun()
    else:
        st.success(f"🎊 14문제 완료! 최종 점수: {st.session_state.score} / 14")
        if st.button('처음부터 다시 풀기', use_container_width=True):
            st.session_state.current = 0
            st.session_state.submitted = False
            st.session_state.score = 0
            st.rerun()