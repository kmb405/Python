from flask import render_template, session, redirect, request, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.ride import Ride
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/rides')
def rides():
    if session['id'] and session['logged_in'] == True:
        rides = Ride.get_all_rides()
        return render_template('dashboard.html', rides=rides)
    else:
        return redirect('/')

@app.route('/ride/<int:ride_id>')
def view_ride(ride_id):
    if session['id'] and session['logged_in'] == True:
        ride = Ride.get_one_ride(ride_id=ride_id)
        return render_template('view_ride.html', ride=ride)
    else:
        return redirect('/')

@app.route('/ride/edit/<int:ride_id>/<int:user_id>')
def edit_ride(ride_id, user_id):
    if session['id'] and session['logged_in'] == True:
        ride = Ride.get_one_ride(ride_id=ride_id)
        return render_template('edit_ride.html', ride=ride, user_id=user_id)
    else:
        return redirect('/')
    
@app.route('/ride/new/<int:user_id>')
def new_ride(user_id):
    if session['id'] and session['logged_in'] == True:
        return render_template('new_ride.html', user_id=user_id)
    else:
        return redirect('/')

@app.route('/new_ride', methods=['POST'])
def create_ride():
    if not Ride.validate_ride(request.form):
        return redirect(f'/ride/new/{request.form["user_id"]}')
    else:
        Ride.create_ride(request.form)
        return redirect(f'/rides')

@app.route('/update_ride', methods=['POST'])
def update_ride():
    if not Ride.validate_ride(request.form):
        return redirect(f'/ride/edit/{request.form["ride_id"]}/{request.form["user_id"]}')
    else:
        Ride.update_ride(request.form)
        return redirect(f'/rides')
    

@app.route('/delete_ride/<int:ride_id>')
def delete_ride(ride_id):
    Ride.delete_ride(ride_id)
    return redirect('/rides')