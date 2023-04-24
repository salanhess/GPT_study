from datetime import datetime, timedelta
from flask import Flask, make_response
'''
在上面的示例中，当用户访问主页（'/'）时，服务器将发送一个响应，其中包含一个名为'username'的cookie，其值为'john'。
可以使用浏览器的开发者工具（例如Chrome的开发者工具）来查看cookie是否已正确设置。
请注意，如果没有设置cookie的过期时间，则cookie将在浏览器关闭时过期。要设置过期时间，请使用expires参数。
例如，以下代码将设置一个cookie，有效期为一小时：
'''

app = Flask(__name__)

@app.route('/')
def index():
    resp = make_response('Setting a cookie')
    expires = datetime.now() + timedelta(hours=1)
    resp.set_cookie('username', 'john', expires=expires)
    return resp

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(debug=True, host='0.0.0.0', port=8080)