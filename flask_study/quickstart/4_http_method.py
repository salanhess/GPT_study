from markupsafe import escape
from flask import Flask, session, request, redirect, url_for
from flask import url_for
'''
todo: 
    username = request.args.get('username')
    password = request.args.get('password')
    无法获取到用户名和密码 
'''

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # 设置应用程序的安全密钥

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

def do_the_login():
    username = request.args.get('username')
    password = request.args.get('password')
    print('Logged in user: {}, password: {}'.format(username, password))
    if username == 'admin' and password == 'admin':
        session['logged_in'] = True
        return redirect(url_for('login'))
    else:
        return 'Invalid username or password'

def show_the_login_form():
    return '''
    <form action="/login" method="post">
        <input type="text" name="username" placeholder="Username">
        <input type="password" name="password" placeholder="Password">
        <input type="submit" value="Login">
    </form>
    '''    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)    