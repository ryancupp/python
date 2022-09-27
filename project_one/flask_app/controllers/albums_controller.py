from flask_app import app
from flask import render_template, redirect, request, flash, session
from flask_app.models.users_model import User
from flask_app.models.albums_model import Album

@app.route('/albums/new')
def new_album_form():
    if 'user_id' not in session:
        return redirect ('/')
    return render_template("new_album.html")

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