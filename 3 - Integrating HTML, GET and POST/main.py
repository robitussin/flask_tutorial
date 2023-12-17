from flask import Flask, redirect, url_for, render_template, request

# WSGI Application
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/cats')
def cats():
    return "Zesto, Butter, Livi"

@app.route('/success/<int:score>')
def success(score):
    res = ""
    if score >= 50:
        res="PASS"
    else:
        res="FAIL"
        
    return render_template('result.html', result=res)

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

# Result checker HTML page
@app.route('/submit', methods=['POST', 'GET'])
def submit():
    
    totalscore = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        math = float(request.form['maths'])
        c = float(request.form['c'])
        datascience = float(request.form['datascience'])
        totalscore = science + math + c + datascience
        
    res = ""
    if totalscore >= 50:
        res = "success"
    else:
        res = "fail"
        
    return redirect(url_for(res, score=totalscore))

if __name__ == '__main__':
    app.run(debug=True)