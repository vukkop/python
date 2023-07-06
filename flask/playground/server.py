from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
  return "Hello World"



@app.route('/play/')
def welcome_play():
  return render_template("index.html", times=3, color="blue")

@app.route('/play/<int:times>/')
def welcome_play_number(times):
  return render_template("index.html", times=times, color="blue")

@app.route('/play/<int:times>/<string:color>/')
def welcome(times, color):
  return render_template("index.html", times=times, color=color)


if __name__=="__main__":
  app.run(debug=True)
