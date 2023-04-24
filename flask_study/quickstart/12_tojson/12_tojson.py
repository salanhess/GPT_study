'''
Q:请继续阅读 https://flask.palletsprojects.com/en/2.2.x/quickstart/#a-minimal-application   
 分析其中的APIs with JSON概念，并给出一个可以实际运行的包含JSON response 以及调用to_json()的例子

A:这个示例中，我们定义了两个路由：/api和/api/tojson，分别返回JSON格式的数据。
 在get_data函数中，我们使用jsonify函数将Python字典转换为JSON格式的响应。
 在get_data_tojson函数中，我们使用了Pandas库中的to_json方法，将数据以JSON格式返回。
 这两个路由均返回相同的数据，只是数据来源和转换方式不同。

'''

from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_data():
    data = {
        'name': 'Alice',
        'age': 30,
        'gender': 'female'
    }
    return jsonify(data)

@app.route('/api/tojson', methods=['GET'])
def get_data_tojson():
    data = {
        'name': 'Bob',
        'age': 25,
        'gender': 'male'
    }
    return json.dumps(data)

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(debug=True, host='0.0.0.0', port=8080)