from flask import Flask, render_template, redirect, session, request, url_for
app = Flask(__name__)
from users import User

@app.route('/users')
def users():
    users = User.get_all()
    return render_template('users.html', users=users)

@app.route('/user/<int:id>')
def user(id):
    data ={ 
        "id":id
    }
    user = User.get_one(data)
    return render_template('user.html', user=user)

@app.route('/edit/<int:id>')
def edit(id):
    data ={ 
        "id":id
    }
    user = User.get_one(data)
    return render_template('edit.html', user=user)

@app.route('/new')
def new():
    return render_template('new.html')

@app.route('/add', methods=['POST'])
def add_user():
    id = User.add_one(request.form)
    return redirect(url_for('user', id=id))

@app.route('/update/<int:id>',methods=['POST'])
def update(id):
    User.update(request.form)
    return redirect(url_for('user', id=id))

@app.route('/delete/<user_id>')
def delete(user_id):
    User.delete(user_id)
    return redirect("/users")

if (__name__) == '__main__':
    app.run(debug=True)