from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.model_dojo import Dojo

@app.route("/dojos")
def get_all_dojos():
  dojos = Dojo.get_all()
  return render_template("dojos.html", dojos=dojos)

@app.route("/dojos/<int:id>")
def get_dojo_by_id(id):
  dojo = Dojo.get_by_id_with_ninjas(id)
  return render_template("single_dojo.html", dojo=dojo)

@app.route('/dojos/create', methods=["POST"])
def dojo_create():
  data = {
  "dojo_name": request.form["dojo_name"],
  }
  Dojo.save(data)
  return redirect('/dojos')
