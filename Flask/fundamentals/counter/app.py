from flask import Flask, render_template, request, redirect, session

app=Flask(__name__)
app.secret_key = "secretkey"

@app.route('/')
def root():
    if 'count' in session:
        session['count'] += 1
        return render_template('index.html')
    else:
        print("key not is session")
        session['count'] = 1
        return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    session['count'] += int(request.form['count']) - 1
    return redirect('/')

@app.route('/two')
def two():
    session['count'] += 1
    return redirect('/')


@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if (__name__) == '__main__':
    app.run(debug=True)