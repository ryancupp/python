from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.dojo_model import Dojo
from flask_app.models.ninja_model import Ninja

@app.route('/new/ninja')
def new():
    return render_template("new_ninja.html", dojos=Dojo.get_all())

@app.route('/ninja/create',methods=['POST'])
def create_ninja():
    print(request.form)
    Ninja.new_ninja(request.form)
    return redirect(f'/dojos/{request.form["dojo_id"]}')