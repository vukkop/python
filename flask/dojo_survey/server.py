from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'secret01'

@app.route('/')
def load_home_page():

  return render_template('index.html')

@app.route('/result')
def result():

  return render_template('result.html')


@app.route('/destroy_session')
def destroy_session():
  if 'num' in session:
    session.clear()
    return redirect('/')


if __name__=="__main__":
  app.run(debug=True)
