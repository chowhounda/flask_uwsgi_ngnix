from flask import Flask, request
from flask import jsonify
from concurrent import futures

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/index')
def index():
    return 'Hello Index'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
