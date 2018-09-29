from flask import Flask
from flask import request


app = Flask(__name__)


#index
@app.route('/')
def index():
    return open("Happy_Birthday.html", 'rb').read()

@app.route('/img.jpeg')
def pic():
    return open("img.jpeg", 'rb').read()


if __name__ == '__main__':
    app.run(port=5001, host='0.0.0.0')
