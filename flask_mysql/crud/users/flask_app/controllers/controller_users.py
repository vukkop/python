from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/users")
def get_all_users():
  users = User.get_all()
  return render_template("users.html", users=users)

@app.route("/users/new")
def add_user():
    return render_template("create.html")

@app.route('/users/new/create_user', methods=["POST"])
def create_user():
  data = {
  "fname": request.form["fname"],
  "lname" : request.form["lname"],
  "email" : request.form["email"]
  }
  User.save(data)
  return redirect('/users')

@app.route("/users/<int:id>")
def get_user_by_id(id):
  user = User.get_by_id(id)
  return render_template("user_page.html", user=user)

@app.route("/users/<int:id>/edit")
def get_user(id):
  user = User.get_by_id(id)
  return render_template("user_edit_page.html", user=user)

@app.route('/users/<int:id>/update', methods=["POST"])
def update_user(id):
  data = {
  "id": id,
  "fname": request.form["fname"],
  "lname" : request.form["lname"],
  "email" : request.form["email"],
  }
  User.update(data)
  return redirect(f'/users/{id}')

@app.route("/users/<int:id>/delete")
def delete_(id):
  User.delete(id)
  return redirect('/users')
