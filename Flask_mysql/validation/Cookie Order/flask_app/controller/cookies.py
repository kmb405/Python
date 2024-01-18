from flask import render_template, session, redirect, request
from flask_app import app
from flask_app.models.cookie import Cookie


@app.route('/cookies')
def orders():
    orders = Cookie.get_all_orders()
    return render_template('cookies.html', orders=orders)

@app.route('/edit_cookie/<id>')
def edit_cookie(id):
    order = Cookie.get_one_order(id=id)
    return render_template('edit_cookie.html', order=order)

@app.route('/new_cookie')
def new_cookie():
    return render_template('new_cookie.html')

@app.route('/add_cookie', methods=['POST'])
def add_author():
    session['customer_name'] = request.form['customer_name']
    session['cookie_type'] = request.form['cookie_type']
    session['number_of_boxes'] = request.form['number_of_boxes']
    if not Cookie.validate_order(request.form):
        return redirect('/new_cookie')
    Cookie.create_order(request.form)
    return redirect('/cookies')

@app.route('/update_cookie/<id>', methods=['POST'])
def add_book(id):
    if not Cookie.validate_order(request.form):
        return redirect('/edit_cookie/' + id)
    Cookie.update_order(request.form)
    return redirect('/cookies')