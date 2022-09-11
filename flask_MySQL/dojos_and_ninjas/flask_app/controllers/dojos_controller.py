from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.dojo_model import Dojo
from flask_app.models.ninja_model import Ninja

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def users():
    return render_template("all_dojo_page.html",dojos=Dojo.get_all())

@app.route('/dojo/create',methods=['POST'])
def create():
    print(request.form)
    Dojo.new_dojo(request.form)
    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def one_dojo(id):
    one_dojo = Dojo.get_dojo_with_ninjas({'id':id})
    return render_template("show_one_dojo.html", one_dojo = one_dojo)