from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/<int:y>/')
@app.route('/<int:x>/<int:y>/')
@app.route('/<int:x>/<int:y>/<string:light>/')
@app.route('/<int:x>/<int:y>/<string:light>/<string:dark>/')
def colors(x=8, y=8, light="blue", dark="black"):
  return render_template("index.html", x=x, y=y, light=light, dark=dark)

if __name__=="__main__":
  app.run(debug=True)
