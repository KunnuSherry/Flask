from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)

@app.route('/')
def start():
     return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    return render_template('success.html', score=score)

@app.route('/fail/<int:score>')
def fail(score):
    return render_template('fail.html', score=score)

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    total = 0
    res = "";
    if request.method == 'POST':
            math = int(request.form['math'])
            physics = int(request.form['physics'])
            chemistry = int(request.form['chemistry'])
            biology = int(request.form['biology'])
            english = int(request.form['english'])
            total = (math+physics+chemistry+biology+english)/5
    if total>50:
         res = "success"
    else:
         res = "fail"
    return redirect(url_for(res, score=total))

    

if(__name__=='__main__'):
    app.run(debug=True)