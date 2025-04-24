from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Home Page!'

@app.route('/cat')
def cat():
    return 'This is the Cat Page!'

@app.route('/dog')
def dog():
    return 'This is the Dog Page!'

@app.route('/elephant')
def dog():
    return 'This is the elephant Page!'

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000, debug=True)
