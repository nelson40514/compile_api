from flask import *

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    data = "Deploying a Flask App To Heroku"
    return data

if __name__ == '__main__':
    app.run(debug=True)
