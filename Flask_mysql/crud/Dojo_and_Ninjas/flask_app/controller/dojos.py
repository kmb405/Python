from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo, Ninja


@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all_dojos()
    return render_template('dojos.html', dojos=dojos)

@app.route('/ninja')
def ninja():
    dojos = Dojo.get_all_dojos()
    return render_template('new_ninja.html', dojos=dojos)

@app.route('/edit/<id>')
def edit(id):
    ninja = Ninja.get_one_ninja(id=id)
    return render_template('edit_ninja.html', ninja=ninja)

@app.route('/dojo/<id>')
def dojo(id):
    dojo = Dojo.get_one_dojo(id=id)
    print(dojo)
    ninjas = Ninja.get_all_ninjas(id=id)
    return render_template('dojo_show.html', ninjas=ninjas, dojo=dojo)

@app.route('/create_ninja', methods=['POST'])
def create_ninja():
    id = request.form['dojo_id']
    Ninja.create_ninja(data=request.form)
    return redirect('/dojo/'+ id)

@app.route('/update_ninja/<id>', methods=['POST'])
def update_ninja(id):
    dojo_id = Ninja.get_ninja_dojo_id(id)
    Ninja.update_ninja(data=request.form)
    return redirect('/dojo/'+ str(dojo_id[0]['dojo_id']))

@app.route('/delete_ninja/<id>')
def delete_ninja(id):
    dojo_id = Ninja.get_ninja_dojo_id(id)
    Ninja.delete_ninja(id=id)
    return redirect('/dojo/'+ str(dojo_id[0]['dojo_id']))

@app.route('/create_dojo', methods=['POST'])
def create_dojo():
    Dojo.create_dojo(data=request.form)
    return redirect('/dojos')