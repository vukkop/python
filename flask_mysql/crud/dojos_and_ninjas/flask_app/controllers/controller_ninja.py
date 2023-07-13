from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.model_ninja import Ninja
from flask_app.models.model_dojo import Dojo


@app.route("/ninjas")
def ninja_new():
  dojos = Dojo.get_all()
  return render_template("new_ninja.html", dojos=dojos)

@app.route('/ninjas/create', methods=["POST"])
def ninja_create():
  id = request.form["dojo_id"]
  data = {
  "dojo_id": request.form["dojo_id"],
  "first_name": request.form["first_name"],
  "last_name": request.form["last_name"],
  "age": request.form["age"]
  }
  Ninja.save(data)
  return redirect(f'/dojos/{id}')
