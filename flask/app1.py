# app1.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    # 작업
    return '<h1>아무개 페이지</h1><p>Flask에 오신 걸 환영합니다!</p>'

@app.route('/about')
def about():
    return '<h1>아무개 소개 페이지</h1><p>Flask 학습 중입니다.</p>'

@app.route('/contact')
def contact():
    return '<h1>아무개 연락처</h1><p>email: example@flask.com</p>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')