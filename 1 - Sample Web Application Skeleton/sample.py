from flask import Flask

# WSGI Application
app = Flask(__name__)

@app.route('/')
def welcome():
    return "Hello SLY"

if __name__ == '__main__':
    app.run(debug=True)