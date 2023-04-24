from markupsafe import escape
from flask import Flask, session, request, redirect, url_for
from flask import url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

def test_urlfor():
    with app.test_request_context():
        print(url_for('index'))
        print(url_for('login'))
        print(url_for('login', next='/'))
        print(url_for('profile', username='John Doe'))


if __name__ == '__main__':
    test_urlfor()
    app.run(debug=True, host='0.0.0.0', port=8080)
