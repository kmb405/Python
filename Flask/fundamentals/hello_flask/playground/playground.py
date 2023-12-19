from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Go to url /play"

# @app.route('/play')
# def play(block=3, color="blue"):
#     return render_template('play.html', block=block, color=color )

# @app.route('/play/<int:block>')
# def play(block=3, color="blue"):
#     return render_template('play.html', block=block, color=color )


@app.route('/play')
@app.route('/play/<int:block>')
@app.route('/play/<int:block>/<string:color>')
def play(block=3, color="blue"):
    return render_template('play.html', block=block, color=color)

if __name__ == "__main__":
    app.run(debug=True)