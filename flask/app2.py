from flask import Flask

app = Flask(__name__)

# 문자열 변수 (기본값)
@app.route('/user/<username>')
def user_profile(username):
    return f'<h1>{username}님의 프로필</h1>'

# 정수형 변수
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'<h1>게시글 #{post_id}</h1>'

# 실수형 변수
@app.route('/pi/<float:value>')
def show_pi(value):
    return f'입력값: {value}'

# 멀티플 변수
@app.route('/multiply/<int:a>/<int:b>')
def multiply(a, b):
    return f'<h1>{a} × {b} = {a * b}</h1>'

# greet

@app.route('/greet/<name>/<int:age>')
def greet(name, age):
    return f'<h1>{name}는 {age}살이구나.</h1>'

# 라우터
@app.route('/square/<int:n>')
def square(n):
    return f'<h1>{n}의 제곱은 {n**2}입니다.</h1>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')