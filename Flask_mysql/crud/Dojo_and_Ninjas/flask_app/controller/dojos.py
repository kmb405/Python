from flask import render_template, redirect
from server import app
from flask_app.models.dojo import Dojo, Ninja


@app.route('/dojo')
def dojos():
    return render_template('dojos.html')

@app.route('/ninja')
def ninja():
    return render_template('new_ninja.html')

@app.route('/dojo/<int:id>')
def dojo(id):
    Ninja.get_all_ninjas(id=id)
    redirect('/')