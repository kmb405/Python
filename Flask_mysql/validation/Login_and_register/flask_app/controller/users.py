from flask import render_template, session, redirect, request
from flask_app import app
from flask_app.models.user import User


@app.route('/')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/register_user', methods=['POST'])
def register():
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['email'] = request.form['email']
    session['password'] = request.form['password']
    # if not User.validate_user(request.form):
    #     return redirect('/')
    User.create_user(request.form)
    return redirect('/')

@app.route('/login_user', methods=['POST'])
def login_user():
    # if not User.validate_user(request.form):
    #     return redirect('/')
    user = User.get_one_user(request.form['email'])
    session['first_name'] == user.first_name
    if user.email == request.form['email'] and user.password == request.form['password']:
        return redirect('/dashboard')
    else:
        return redirect('/')