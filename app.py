from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World from Google App Engine!"

@app.route('/about')
def about():
    return "This is a simple GAE web application"

if __name__ == '__main__':
    app.run()
