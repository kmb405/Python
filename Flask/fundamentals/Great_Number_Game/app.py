from flask import Flask, redirect, request, render_template, session
from random import randint

app = Flask(__name__)
app.secret_key = 'secretkey'



@app.route('/')
def index():
    if 'number' in session:
        session['count'] += 1
        return render_template('index.html')
    else:
        session['number'] = randint(0,100)
        session['count'] = 0
        return render_template('index.html')

@app.route('/form', methods=['POST', 'GET'])
def guess():
    guess = int(request.form['guess'])
    if guess == session['number']:
        session['ans'] = 'You Win'
        return redirect('/')
    elif guess > session['number']:
        session['ans'] = 'Too High'
        return redirect('/')
    elif guess < session['number']:
        session['ans'] = 'Too Low'
        return redirect('/')
    else:
        return 'Error'
    
@app.route('/save', methods=['POST', 'GET'])
def save():
    session['name'] = request.form['name']
    return redirect('leaders')
    
@app.route('/newgame', methods=['POST', 'GET'])
def new():
    session.clear()
    return redirect('/')

@app.route('/leaders')
def leaders():
    return render_template('leaders.html')


if (__name__) == '__main__':
    app.run(debug=True)