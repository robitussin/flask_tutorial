from flask import Flask, redirect, url_for

# WSGI Application
app = Flask(__name__)

@app.route('/')
def welcome():
    return "Hello SLY"

@app.route('/cats')
def cats():
    return "Zesto, Butter, Livi"

@app.route('/success/<int:score>')
def success(score):
    return "The person has passed and the score is: " + str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "The person has failed and the score is: " + str(score)

@app.route('/results/<int:score>')
def results(score):
    
    if score < 50:
        result='fail'
    else:
        result='pass'
    
    return result
    
@app.route('/resultredirect/<int:marks>')
def resultredirect(marks):
    
    if marks < 50:
        result='fail'
    else:
        result='success'
    
    # return result
    return redirect(url_for(result, score=marks))

if __name__ == '__main__':
    app.run(debug=True)