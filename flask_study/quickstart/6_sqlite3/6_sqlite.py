import os
import sqlite3
from flask import Flask, g, jsonify, request

'''
学习链接 https://flask.palletsprojects.com/en/2.2.x/patterns/sqlite3/
author: baihao
date: 2023年4月23日19:52
'''

# 设置 Flask 应用
app = Flask(__name__)

# 配置数据库路径
DATABASE = os.path.join(os.getcwd(), 'database.db')
# DATABASE = 'D:\\Python\\study\\flask_study\\quickstart\\6_sqlite3\\database.db'

# 初始化数据库表结构
def init_database():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

# 数据库连接处理
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

# 关闭数据库连接
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# 添加数据到 sqlite3 中的 sqlitemydata 表
@app.route('/api/v1/insert', methods=['POST'])
def insert_data():
    data = request.get_json()
    name = data['name']
    email = data['email']
    db = get_db()
    try:
        db.execute('INSERT INTO sqlitemydata (name, email) VALUES (?, ?)',
                   [name, email])
        db.commit()
        response_obj = {'status': 'success', 'message': 'Data successfully inserted'}
    except Exception as e:
        response_obj = {'status': 'error', 'message': str(e)}
        db.rollback()  # 回滚事务
    
    return jsonify(response_obj)

# 在API中调用SQLite3进行Query查询
@app.route('/api/v1/query', methods=['GET'])
def query_data():
    db = get_db()
    cur = db.execute('SELECT * FROM sqlitemydata')
    data = cur.fetchall()
    return jsonify(data)

# 从sqlite3中的sqlitemydata表中删除数据
@app.route('/api/v1/delete/<int:id>', methods=['DELETE'])
def delete_data(id):
    db = get_db()
    try:
        db.execute('DELETE FROM sqlitemydata WHERE id=?', [id])
        db.commit()
        response_obj = {'status': 'success', 'message': 'Data successfully deleted'}
    except Exception as e:
        response_obj = {'status': 'error', 'message': str(e)}
        db.rollback()  # 回滚事务
    
    return jsonify(response_obj)

# 更新sqlite3中的sqlitemydata表中的数据
@app.route('/api/v1/update/<int:id>', methods=['PUT'])
def update_data(id):
    data = request.get_json()
    db = get_db()
    try:
        # 通过 ID 获取原来的值
        cur = db.execute('SELECT name, email FROM sqlitemydata WHERE id=?', [id])
        row = cur.fetchone()
        if not row:
            response_obj = {'status': 'error', 'message': 'Data with specified ID does not exist'}
        else:
            # 将未修改的属性保持为原值
            name = data.get('name') or row['name']
            email = data.get('email') or row['email']
            db.execute('UPDATE sqlitemydata SET name=?, email=? WHERE id=?',
                       [name, email, id])
            db.commit()
            response_obj = {'status': 'success', 'message': 'Data successfully updated'}
    except Exception as e:
        response_obj = {'status': 'error', 'message': str(e)}
        db.rollback()  # 回滚事务
    
    return jsonify(response_obj)

if __name__ == '__main__':
    init_database()
    app.run(debug=True, host='0.0.0.0', port=8080)
