from flask import render_template, session, redirect, request, flash, url_for
from flask_app import app
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/logout')
def logout():
    session.clear()
    return redirect("/")

@app.route('/register_user', methods=['POST'])
def register():
    data = {
    'first_name': request.form['first_name'],
    'last_name': request.form['last_name'],
    'email': request.form['email'],
    'password': bcrypt.generate_password_hash(request.form['password']),
    }
    user = User.get_one_user(request.form['email'])
    if user:
        flash('Email already in use.', 'register')
        return redirect('/')
    if not User.validate_register(request.form):
        return redirect('/')
    User.create_user(data)
    return redirect('/')

@app.route('/login_user', methods=['POST'])
def login_user():
    user = User.get_one_user(request.form['email'])
    if user:
        if bcrypt.check_password_hash(user.password, request.form['password']):
            session['id'] = user.id
            session['first_name'] = user.first_name
            session['logged_in'] = True
            return redirect(f"/recipes")
        else:
            flash('Invalid Email/Password', 'login')
            return redirect('/')
    else:
        flash('Invalid Email/Password', 'login')
        return redirect('/')