from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'secret01'

@app.route('/')
def load_home_page():
  if not 'num' in session:
    session['num'] = 1
    session['counter'] = 1
  else:
    session['num'] += 1
  return render_template('index.html', num = session['num'],counter = session['counter'])

@app.route('/add')
def add():
  if not 'counter' in session:
    session['counter'] = 1
  else:
    session['counter'] += 1
  return redirect('/')

@app.route('/add_two')
def add_two():
  if not 'counter' in session:
    session['counter'] = 1
  else:
    session['counter'] += 2
  return redirect('/')

@app.route('/add_from_input', methods=['POST'])
def add_from_input():
  session['counter'] += int(request.form['number'])
  return redirect('/')

@app.route('/destroy_session')
def destroy_session():
  if 'num' in session:
    session.clear()
    return redirect('/')


if __name__=="__main__":
  app.run(debug=True)
