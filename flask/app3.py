from flask import Flask, request

app = Flask(__name__)

# GET과 POST 모두 허용
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        return f'바이브넘치노{username}님 로그인 성공!'
    return '''
        짝꿍님 실업급여 축하합니다
        <form method="POST">
            <input type="text" name="username" placeholder="아이디">
            <button type="submit">로그인</button>
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    