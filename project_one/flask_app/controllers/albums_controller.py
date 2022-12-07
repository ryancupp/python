from flask_app import app
from flask import render_template, redirect, request, flash, session
from flask_app.models.users_model import User
from flask_app.models.albums_model import Album


@app.route('/albums/new')
def new_album_form():
    if 'user_id' not in session:
        return redirect('/')
    user_data = {
        'id': session['user_id']
    }
    logged_user = User.get_by_id(user_data)
    return render_template("new_album.html", logged_user=logged_user)

@app.route('/albums/create', methods=['POST'])
def process_album():
    if 'user_id' not in session:
        return redirect('/')
    if not Album.validator(request.form):
        return redirect('/albums/new')
    data = {
        **request.form,
        'user_id': session['user_id']
    }
    Album.create(data)
    return redirect('/welcome')

@app.route("/albums/<int:id>")
def show_album(id):
    album = Album.get_by_id({'id':id})
    user_data = {
        'id': session['user_id']
    }
    logged_user = User.get_by_id(user_data)
    return render_template("show_album.html", album = album, logged_user = logged_user)    

@app.route("/albums/<int:id>/edit")
def edit_album_form(id):
    if 'user_id' not in session:
        return redirect('/')
    album = Album.get_by_id({'id':id})
    if not int(session['user_id']) == album.user_id:
        return redirect('/welcome')
    album = Album.get_by_id({'id':id})
    user_data = {
        'id': session['user_id']
    }
    logged_user = User.get_by_id(user_data)
    return render_template("edit_album.html", album = album, logged_user = logged_user)

@app.route("/albums/<int:id>/update", methods=['POST'])
def update_album(id):
    if 'user_id' not in session:
        return redirect('/')
    album = Album.get_by_id({'id':id})
    if not int(session['user_id']) == album.user_id:
        return redirect('/welcome')
    if not Album.validator(request.form):
        return redirect(f"/albums/{id}/edit")
    data = {
        **request.form,
        'id' : id
    }
    Album.update(data)
    return redirect('/welcome')

@app.route("/albums/<int:id>/delete")
def delete_album(id):
    if 'user_id' not in session:
        return redirect('/')
    album = Album.get_by_id({'id':id})
    if not int(session['user_id']) == album.user_id:
        return redirect ('/welcome')
    Album.delete({'id':id})
    return redirect('/welcome')
