from flask import Flask, render_template, request, redirect, session
# import the class from friend.py
from friend import Friend
app = Flask(__name__)
app.secret_key = 'secretkey'
@app.route("/")
def index():
    # call the get all classmethod to get all friends
    friends = Friend.get_all()
    print(friends)
    return render_template("index.html", all_friends = friends)

@app.route('/create_friend', methods=['POST'])
def create_friend():
    Friend.save(request.form)
    return redirect('/')

@app.route('/show_friend/<int:friend_id>')
def get_one(friend_id):
    friend = Friend.get_one(friend_id)
    return render_template('show_friend.html', friend=friend)
            
if __name__ == "__main__":
    app.run(debug=True)