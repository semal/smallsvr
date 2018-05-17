from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'HELLO, WORLD! THIS IS FROM SEMAL\'S ANDROID TABLET.'
