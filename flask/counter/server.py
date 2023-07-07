from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'secret01'

@app.route('/')
def load_home_page():
  if not 'num' in session:
    session['num'] = 1
  else:
    session['num'] += 1
  return render_template('index.html', num = session['num'])

@app.route('/add_two')
def add_two():
  if not 'num' in session:
    session['num'] = 1
  else:
    session['num'] += 2
  return render_template('index.html', num = session['num'])

@app.route('/add_from_input', methods=['POST'])
def add_from_input():
  session['num'] += int(request.form['number'])-1
  return redirect('/')

@app.route('/destroy_session')
def destroy_session():
  if 'num' in session:
    session.clear()
    return redirect('/')


if __name__=="__main__":
  app.run(debug=True)
