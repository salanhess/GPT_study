from flask import Flask, request
'''
非常感谢，请继续阅读 https://flask.palletsprojects.com/en/2.2.x/quickstart/#a-minimal-application    
分析其中的The Request Object 概念，并给出一个可以实际运行的例子
'''

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 获取POST请求中的表单数据
        name = request.form['name']
        age = request.form['age']
        return f'Hello {name}, your age is {age}!'
    else:
        return '''
            <form method="post">
                <label>Name:</label><input type="text" name="name"><br>
                <label>Age:</label><input type="text" name="age"><br>
                <button type="submit">Submit</button>
            </form>
        '''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
