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

@app.route("/recipes/<int:id>/delete")
def delete_recipie(id):
  if 'user_id' not in session:
    return redirect("/")
  Recipe.delete(id)
  return redirect("/recipes")

@app.route("/recipes/<int:id>")
def display_recipie(id):
  print(id)
  if 'user_id' not in session:
    return redirect("/")
  user = User.get_by_id(session['user_id'])
  recipe = Recipe.get_by_id(id)
  return render_template("display_recipe.html", recipe=recipe, user=user)

