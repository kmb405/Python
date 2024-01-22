from flask import render_template, session, redirect, request, flash
from flask_app import app
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/main/<int:id>')
def main(id):
    if session['id'] == id and session['logged_in'] == True:
        return render_template('main.html')
    else:
        return redirect('/')

@app.route('/recipe/<int:id>')
def recipe(id):
    if session['id'] == id and session['logged_in'] == True:
        return render_template('recipe.html')
    else:
        return redirect('/main')

@app.route('/logout')
def logout():
    session.clear()
    return redirect("/")

