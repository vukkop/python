from flask_app import app, bcrypt
from flask import render_template,redirect,request,session
from flask_app.models.model_user import User
from flask_app.models.model_recipe import Recipe

@app.route("/recipes/new")
def new_recipie():
  if 'user_id' not in session:
    return redirect("/")
  return render_template("new_recipe.html")

@app.route("/recipes/create", methods = ["POST"])
def create_recipe():
  data = {
    **request.form,
    'user_id' : session['user_id']
  }
  Recipe.save(data)
  return redirect('/recipes')

