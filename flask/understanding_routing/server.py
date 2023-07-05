from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello World!'

@app.route('/dojo')
def hello_dojo():
  return 'Dojo!'

@app.route('/say/<string:name>')
def hello_person(name):
  return "Hi " + name + "!"

@app.route('/repeat/<int:num>/<string:word>')
def repeat(num, word):
  return f"{word * num}"

@app.errorhandler(404)
def not_found(error):
  """Page not found."""
  return "Sorry! No response. Try again."


if __name__=="__main__":
  app.run(debug=True)
