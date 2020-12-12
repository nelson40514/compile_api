from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello, World!'

@app.route('/test')
def test_page():
  return 'In test page!'

if __name__ == '__main__':
  app.run(threaded=True,host='0.0.0.0', port=80)
