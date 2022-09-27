from flask_app import app
from flask import render_template, redirect, request, flash, session
from flask_app.models.users_model import User
from flask_app.models.sightings_model import Sighting

@app.route('/sightings/new')
def new_sighting_form():
    if 'user_id' not in session:
        return redirect ('/')
    user_data = {
        'id': session['user_id']
    }
    logged_user = User.get_by_id(user_data)
    return render_template("sightings_new.html", logged_user=logged_user)

@app.route('/sightings/create', methods=['POST'])
def process_sighting():
    if 'user_id' not in session:
        return redirect('/')
    if not Sighting.validator(request.form):
        return redirect('/sightings/new')
    data = {
        **request.form,
        'user_id': session['user_id']
    }
    Sighting.create(data)
    return redirect('/welcome')

@app.route("/sightings/<int:id>/edit")
def edit_sighting_form(id):
    if 'user_id' not in session:
        return redirect('/')
    sighting = Sighting.get_by_id({'id':id})
    if not int(session['user_id']) == sighting.user_id:
        return redirect('/welcome')
    sighting = Sighting.get_by_id({'id':id})
    user_data = {
        'id': session['user_id']
    }
    logged_user = User.get_by_id(user_data)
    return render_template("sightings_edit.html", sighting = sighting, logged_user = logged_user)

@app.route("/sightings/<int:id>/update", methods=['POST'])
def update_sighting(id):
    if 'user_id' not in session:
        return redirect('/')
    sighting = Sighting.get_by_id({'id':id})
    if not int(session['user_id']) == sighting.user_id:
        return redirect('/welcome')
    if not Sighting.validator(request.form):
        return redirect(f"/sightings/{id}/edit")
    data = {
        **request.form,
        'id' : id
    }
    Sighting.update(data)
    return redirect('/welcome')

@app.route("/sightings/<int:id>")
def show_sighting(id):
    sighting = Sighting.get_by_id({'id':id})
    user_data = {
        'id': session['user_id']
    }
    logged_user = User.get_by_id(user_data)
    return render_template("show_sighting.html", sighting = sighting, logged_user = logged_user)

@app.route("/sightings/<int:id>/delete")
def delete_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    sighting = Sighting.get_by_id({'id':id})
    if not int(session['user_id']) == sighting.user_id:
        return redirect ('/welcome')
    Sighting.delete({'id':id})
    return redirect('/welcome')
