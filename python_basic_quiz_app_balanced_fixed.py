import streamlit as st

st.set_page_config(
    page_title="Python 기초 퀴즈",
    page_icon="📝",
    layout="centered"
)

# 8월 31일 학습 자료를 바탕으로 구성한 퀴즈
QUESTIONS = [{'q': '프로그램이 처리할 수 있는 모든 것을 무엇이라고 하는가?', 'options': ['데이터', '알고리즘', '자료구조', '프로그램'], 'answer': 0, 'explanation': '데이터(Data)는 프로그램이 처리할 수 있는 모든 것을 의미한다. 이름, 숫자, 사진, 메시지, 온도, 습도 등도 데이터가 될 수 있다.'}, {'q': '컴퓨터의 기본적인 데이터 처리 흐름으로 가장 적절한 것은?', 'options': ['처리 → 입력 → 출력 → 저장', '입력 → 저장 → 처리 → 출력', '저장 → 출력 → 입력 → 처리', '출력 → 처리 → 저장 → 입력'], 'answer': 1, 'explanation': "학습 자료에서는 컴퓨터의 기본 처리를 '입력 → 저장 → 처리 → 출력'으로 정리한다."}, {'q': '자료구조(Data Structure)의 가장 적절한 설명은?', 'options': ['문제를 해결하기 위한 방법과 순서', '코드를 해석하면서 실행하는 프로그램', '데이터를 효율적으로 저장하고 관리하는 방법', '코드에 직접 작성한 값'], 'answer': 2, 'explanation': '자료구조는 많은 데이터를 효율적으로 저장하고 관리하기 위한 방법이다.'}, {'q': '알고리즘(Algorithm)이란 무엇인가?', 'options': ['데이터의 종류를 구분하는 것', '프로젝트별 독립 실행 환경', '코드에 설명을 작성하는 부분', '문제를 해결하기 위한 방법과 순서'], 'answer': 3, 'explanation': '알고리즘은 데이터를 처리해서 문제를 해결하기 위한 방법과 순서이다.'}, {'q': '다음 중 Python이 활용되는 분야로 자료에서 언급되지 않은 것은?', 'options': ['위성 궤도 제어만을 위한 전용 언어', '데이터 처리', '인공지능', '자동화'], 'answer': 0, 'explanation': '자료에서는 Python이 데이터 처리, 인공지능, 자동화, 웹, AI 에이전트 등 다양한 분야에서 활용된다고 설명한다.'}, {'q': 'Python의 실행 방식은 자료에서 어떻게 설명되는가?', 'options': ['오직 컴파일 방식', '인터프리터 방식 중심', '오직 기계어 직접 실행', '문서 편집 방식'], 'answer': 1, 'explanation': 'Python은 일반적으로 인터프리터 방식의 언어로 이해하며, 인터프리터가 코드를 해석하면서 실행한다.'}, {'q': 'Python 파일의 확장자는 무엇인가?', 'options': ['.python', '.pt', '.py', '.exe'], 'answer': 2, 'explanation': 'Python 파일은 test.py, main.py, app.py처럼 .py 확장자를 사용한다.'}, {'q': 'VS Code에 대한 설명으로 가장 적절한 것은?', 'options': ['Python만 설치하는 프로그램', '컴퓨터의 저장장치', 'Python의 자료형', 'Python 코드를 작성하고 실행할 수 있는 개발 도구'], 'answer': 3, 'explanation': 'VS Code는 코드 작성과 실행뿐 아니라 파일 관리, 디버깅, 확장 기능, 터미널 사용 등 다양한 개발 작업에 활용된다.'}, {'q': 'IDE의 뜻은 무엇인가?', 'options': ['통합 개발 환경', '인터프리터 데이터 엔진', '독립 데이터 실행기', '입력 장치 관리자'], 'answer': 0, 'explanation': 'IDE는 Integrated Development Environment의 약자로, 코드 작성·실행·디버깅·프로젝트 관리 등의 기능을 하나의 환경에서 제공한다.'}, {'q': 'Python에서 다른 사람이 만들어 놓은 라이브러리를 설치할 때 사용하는 도구는?', 'options': ['dir', 'pip', 'cls', 'cd'], 'answer': 1, 'explanation': 'pip는 Python 라이브러리를 설치할 때 사용하는 도구이다. 예: pip install matplotlib.'}, {'q': 'Python 코드에서 라이브러리나 모듈을 사용할 때 주로 사용하는 키워드는?', 'options': ['install', 'open', 'import', 'use'], 'answer': 2, 'explanation': '라이브러리나 모듈을 코드에서 사용할 때 import를 사용한다.'}, {'q': 'time.sleep(5)의 의미로 자료에 맞는 것은?', 'options': ['5개의 시간을 출력한다', '5초 전으로 되돌린다', '프로그램을 삭제한다', '5초 동안 실행을 멈춘다'], 'answer': 3, 'explanation': 'time.sleep(5)는 5초 동안 실행을 멈추고, 그 후 다음 코드가 실행된다.'}, {'q': '가상환경(Virtual Environment)을 사용하는 주된 이유는?', 'options': ['프로젝트별로 독립적인 Python 실행 환경을 만들기 위해', '모니터 화면을 정리하기 위해', 'Python 파일의 확장자를 바꾸기 위해', '인터넷 속도를 높이기 위해'], 'answer': 0, 'explanation': '프로젝트마다 필요한 Python 버전이나 라이브러리가 다를 수 있으므로 충돌을 줄이기 위해 프로젝트별 독립 환경을 만든다.'}, {'q': '터미널에 (.venv)가 표시된다면 무엇을 의미하는가?', 'options': ['가상환경이 삭제된 상태', '가상환경이 활성화된 상태', '현재 폴더가 비어 있는 상태', 'Python이 설치되지 않은 상태'], 'answer': 1, 'explanation': '터미널에 (.venv)처럼 표시되면 가상환경이 활성화된 상태이다.'}, {'q': '가상환경을 종료할 때 사용하는 명령어는?', 'options': ['activate', 'closeenv', 'deactivate', 'exitenv'], 'answer': 2, 'explanation': '자료에서 가상환경 종료 명령어는 deactivate로 제시되어 있다.'}, {'q': 'Windows Command Prompt에서 현재 폴더의 파일과 폴더를 확인하는 명령어는?', 'options': ['cd', 'cls', 'pip', 'dir'], 'answer': 3, 'explanation': 'dir은 현재 폴더에 있는 파일과 폴더 목록을 확인하는 명령어이다.'}, {'q': 'cd test 명령어의 의미는?', 'options': ['test 폴더로 이동', 'test 폴더 삭제', 'test 폴더 생성', '화면 정리'], 'answer': 0, 'explanation': 'cd는 Change Directory의 약자로 폴더를 이동할 때 사용한다. cd test는 test 폴더로 이동한다.'}, {'q': '현재 폴더의 한 단계 위로 이동하려면 무엇을 사용하는가?', 'options': ['cd .', 'cd ..', 'cd /', 'dir ..'], 'answer': 1, 'explanation': '..은 현재 폴더의 한 단계 위를 뜻한다. 따라서 cd ..은 상위 디렉터리로 이동한다.'}, {'q': 'cd .의 .이 의미하는 것은?', 'options': ['상위 위치', 'C드라이브 최상위 위치', '현재 위치', '사용자 폴더'], 'answer': 2, 'explanation': '.은 현재 위치를 의미한다.'}, {'q': 'Command Prompt에서 cls 명령어를 실행하면 어떻게 되는가?', 'options': ['파일이 삭제된다', '현재 폴더가 삭제된다', '가상환경이 종료된다', '화면 내용이 정리된다'], 'answer': 3, 'explanation': 'cls는 Command Prompt 화면을 깨끗하게 정리한다. 파일이나 폴더를 삭제하는 명령어가 아니다.'}, {'q': 'Python에서 if, else, for, while, import, class, def의 공통점은?', 'options': ['키워드(예약어)', '리터럴', '자료구조', '객체'], 'answer': 0, 'explanation': '이 단어들은 Python에서 특별한 의미가 정해져 있는 키워드이다.'}, {'q': '다음 중 식별자로 사용할 수 있는 것은?', 'options': ['1name', 'student_age', 'user name', 'break'], 'answer': 1, 'explanation': 'student_age는 숫자로 시작하지 않고 공백이 없으며 키워드도 아니므로 식별자로 사용할 수 있다.'}, {'q': 'age = 20에서 20은 무엇인가?', 'options': ['식별자', '키워드', '정수 리터럴', '연산자'], 'answer': 2, 'explanation': '20은 코드에 직접 작성한 값이며 정수이므로 정수 리터럴이다. age는 식별자이다.'}, {'q': '10 + 20에서 +는 무엇인가?', 'options': ['표현식', '리터럴', '문장', '연산자'], 'answer': 3, 'explanation': '+는 계산이나 비교 등에 사용하는 기호이므로 연산자이다.'}, {'q': '10 + 20 전체를 값의 관점에서 설명하면 무엇인가?', 'options': ['표현식', '키워드', '식별자', '주석'], 'answer': 0, 'explanation': '표현식(Expression)은 값을 만들어내는 코드이다. 10 + 20의 결과는 30이다.'}, {'q': '여러 개의 Statement가 모이면 무엇을 구성하는가?', 'options': ['리터럴', '프로그램', '자료형', '인덱스'], 'answer': 1, 'explanation': '자료에서는 여러 개의 Statement가 모여 하나의 Program을 구성한다고 설명한다.'}, {'q': '다음 중 자료형이 올바르게 연결된 것은?', 'options': ['3.14 → int', 'True → str', '10 → int', '"Python" → float'], 'answer': 2, 'explanation': '10은 소수점이 없는 정수이므로 int이다. 3.14는 float, True는 bool, "Python"은 str이다.'}, {'q': '10과 10.0의 자료형 구분으로 맞는 것은?', 'options': ['10은 float, 10.0은 int', '둘 다 str', '둘 다 bool', '10은 int, 10.0은 float'], 'answer': 3, 'explanation': '소수점이 없는 10은 int이고, 소수점이 있는 10.0은 float이다.'}, {'q': 'Python에서 True와 False는 어떤 자료형인가?', 'options': ['bool', 'str', 'int', 'float'], 'answer': 0, 'explanation': 'True와 False는 참과 거짓을 나타내는 불리언(Boolean) 자료형이며 Python에서는 bool로 표현한다.'}, {'q': '문자열 "Python"에서 text[0]의 결과는?', 'options': ['y', 'P', 'o', 'n'], 'answer': 1, 'explanation': 'Python은 Zero Index 방식이므로 첫 번째 문자의 인덱스가 0이다. 따라서 text[0]은 P이다.'}, {'q': '문자열 "Python"에서 text[-1]의 결과는?', 'options': ['P', 'o', 'n', 'y'], 'answer': 2, 'explanation': '뒤에서 첫 번째 위치는 -1이다. 따라서 Python의 마지막 문자 n을 가져온다.'}, {'q': '문자열 "Python"에서 text[0:3]의 결과는?', 'options': ['Pyth', 'yth', 'Python', 'Pyt'], 'answer': 3, 'explanation': '슬라이싱은 시작 위치는 포함하고 끝 위치는 포함하지 않는다. 0, 1, 2번 인덱스만 가져오므로 Pyt가 된다.'}, {'q': '문자열 "Python"에서 text[2:]의 결과는?', 'options': ['thon', 'yth', 'Python', 'Pyt'], 'answer': 0, 'explanation': '2번 인덱스부터 끝까지 가져오므로 t부터 시작하는 thon이 된다.'}, {'q': '문자열 안에서 줄바꿈을 나타내는 이스케이프 문자는?', 'options': ['\\t', '\\n', '\\s', '\\b'], 'answer': 1, 'explanation': '\\n은 줄바꿈을 나타낸다. \\t는 탭 간격을 나타낸다.'}, {'q': '문자열 안에서 탭 간격을 나타내는 이스케이프 문자는?', 'options': ['\\n', '\\r', '\\t', '\\p'], 'answer': 2, 'explanation': '\\t는 탭 기능을 수행한다.'}, {'q': '객체지향 프로그래밍에서 클래스와 객체의 관계로 가장 적절한 것은?', 'options': ['객체는 설계도이고 클래스는 실제 대상이다', '클래스와 객체는 항상 같은 의미이다', '객체는 함수이고 클래스는 변수이다', '클래스는 설계도이고 객체는 클래스를 이용해 만들어진 실제 대상이다'], 'answer': 3, 'explanation': '클래스는 객체의 설계도이고, 객체는 클래스를 기반으로 만들어진 실제 대상이다. 하나의 클래스로 여러 객체를 만들 수 있다.'}, {'q': '클래스 안에 정의된 함수는 무엇이라고 하는가?', 'options': ['메서드', '리터럴', '키워드', '인덱스'], 'answer': 0, 'explanation': '메서드(Method)는 클래스 안에 정의된 함수이다.'}, {'q': '클래스의 데이터와 행위에서 데이터에 해당하는 것은?', 'options': ['메서드(Method)', '속성(Attribute)', '알고리즘(Algorithm)', '연산자(Operator)'], 'answer': 1, 'explanation': '클래스에서 데이터는 속성(Attribute), 행위는 메서드(Method)로 표현한다.'}, {'q': '추상화(Abstraction)의 설명으로 가장 적절한 것은?', 'options': ['모든 현실 정보를 빠짐없이 코드로 옮기는 것', '파일을 삭제하는 것', '현실의 복잡한 대상에서 필요한 특징만 선택해 단순하게 표현하는 것', '코드를 한 줄씩 실행하는 것'], 'answer': 2, 'explanation': '추상화는 현실의 복잡한 내용을 모두 표현하지 않고 프로그램에 필요한 특징만 선택해 단순하게 표현하는 과정이다.'}, {'q': '객체지향적인 사고의 시작으로 자료에서 설명한 것은?', 'options': ['모든 데이터를 문자열로 만드는 것', '모든 코드를 한 파일에 작성하는 것', '화면을 먼저 꾸미는 것', '현실의 대상을 데이터와 행위로 나누어 생각하는 것'], 'answer': 3, 'explanation': '현실의 대상을 필요한 데이터와 행위로 나누어 생각하는 것이 객체지향적인 사고의 시작이다.'}, {'q': '함수(Function)의 설명으로 가장 적절한 것은?', 'options': ['특정 작업을 수행하도록 만든 코드의 묶음', '클래스를 이용해 만든 실제 대상', '데이터의 위치를 나타내는 번호', 'Python의 예약된 단어'], 'answer': 0, 'explanation': '함수는 특정 작업을 수행하도록 만든 코드의 묶음이다.'}, {'q': '코딩 컨벤션(Coding Convention)은 무엇인가?', 'options': ['데이터를 저장하는 장치', '코드를 작성할 때 지키는 약속과 규칙', 'Python 파일의 확장자', '프로그램의 실행 결과'], 'answer': 1, 'explanation': '코딩 컨벤션은 코드를 작성할 때 지키는 약속과 규칙이다.'}]

def init_state():
    if "current" not in st.session_state:
        st.session_state.current = 0
    if "selected" not in st.session_state:
        st.session_state.selected = {}
    if "finished" not in st.session_state:
        st.session_state.finished = False

def restart():
    st.session_state.current = 0
    st.session_state.selected = {}
    st.session_state.finished = False

init_state()

st.title("Python 기초 퀴즈")
st.caption("8월 31일 학습 정리 내용을 바탕으로 만든 복습용 퀴즈")

total = len(QUESTIONS)

if st.session_state.finished:
    score = sum(
        st.session_state.selected.get(i) == q["answer"]
        for i, q in enumerate(QUESTIONS)
    )
    st.success(f"퀴즈 완료! {total}문제 중 {score}문제를 맞혔습니다.")
    st.metric("점수", f"{score} / {total}", f"{score/total*100:.0f}%")

    if score == total:
        st.balloons()
        st.write("완벽합니다! 핵심 개념을 잘 이해하고 있어요.")
    elif score >= total * 0.8:
        st.write("아주 잘했어요! 틀린 문제만 다시 확인해 보세요.")
    elif score >= total * 0.6:
        st.write("좋은 출발이에요. 자료형·인덱싱·객체지향 개념을 한 번 더 복습해 보세요.")
    else:
        st.write("괜찮아요. 개념 설명을 다시 읽고 한 번 더 도전해 보세요.")

    st.divider()
    st.subheader("문제별 결과")

    for i, q in enumerate(QUESTIONS):
        user_answer = st.session_state.selected.get(i)
        is_correct = user_answer == q["answer"]
        icon = "✅" if is_correct else "❌"
        answer_text = q["options"][q["answer"]]
        chosen_text = q["options"][user_answer] if user_answer is not None else "응답 없음"

        with st.expander(f"{icon} {i+1}. {q['q']}"):
            st.write(f"내 답: **{chosen_text}**")
            st.write(f"정답: **{answer_text}**")
            st.info(q["explanation"])

    st.button("처음부터 다시 풀기", on_click=restart)
    st.stop()

q_index = st.session_state.current
q = QUESTIONS[q_index]

st.progress((q_index) / total)
st.write(f"### {q_index + 1} / {total}")
st.write(f"## {q['q']}")

previous = st.session_state.selected.get(q_index)
choice = st.radio(
    "정답을 하나 선택하세요.",
    q["options"],
    index=previous if previous is not None else None,
    key=f"q_{q_index}"
)

col1, col2 = st.columns(2)

with col1:
    if q_index > 0:
        if st.button("← 이전 문제", use_container_width=True):
            st.session_state.current -= 1
            st.rerun()

with col2:
    button_text = "결과 보기" if q_index == total - 1 else "다음 문제 →"
    if st.button(button_text, type="primary", use_container_width=True):
        if choice is None:
            st.warning("정답을 선택해주세요.")
        else:
            st.session_state.selected[q_index] = q["options"].index(choice)
            if q_index == total - 1:
                st.session_state.finished = True
            else:
                st.session_state.current += 1
            st.rerun()

st.divider()
st.caption("정답과 해설은 모든 문제를 푼 뒤 결과 화면에서 확인할 수 있습니다.")
