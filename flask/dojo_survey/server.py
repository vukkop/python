from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'secret01'

@app.route('/')
def load_home_page():
  return render_template('index.html')

@app.route('/process', methods=['POST'])
def submit():
  session['data']={**request.form}
  return redirect('/result',)

@app.route('/result')
def result():
  if 'data' not in session:
    return redirect('/')
  else:
    subscribed = "Yes" if 'subscribe' in session['data'] else "No"
    return render_template('result.html', subscribed=subscribed)


@app.route('/destroy_session')
def destroy_session():
  session.clear()
  return redirect('/')


if __name__=="__main__":
  app.run(debug=True)
