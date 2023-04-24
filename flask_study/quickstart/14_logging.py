import logging
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    app.logger.debug('Debug message')
    app.logger.error('Error message')
    return 'Hello, World!'

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(debug=True, host='0.0.0.0', port=8080)