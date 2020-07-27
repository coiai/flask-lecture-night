from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/top')
def top():
    return "ここはトップだよ(๑>◡<๑)"


if __name__ == '__main__':
    app.run(debug=True)