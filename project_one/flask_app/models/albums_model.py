from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import users_model


class Album:
    def __init__(self, data):
        self.id = data['id']
        self.album_title = data['album_title']
        self.artist = data['artist']
        self.genre = data['genre']
        self.favorite_song = data['favorite_song']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def create(cls, data):
        query = "INSERT INTO albums (album_title, artist, genre, favorite_song, user_id) VALUES (%(album_title)s, %(artist)s, %(genre)s, %(favorite_song)s, %(user_id)s);"
        return connectToMySQL('spotify').query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM albums JOIN users on albums.user_id = users.id;"
        results = connectToMySQL('spotify').query_db(query)
        if len(results) > 0:
            all_albums = []
            for row in results:
                this_album = cls(row)
                user_data = {
                    **row,
                    'id': row['users.id'],
                    'created_at': row['users.created_at'],
                    'updated_at': row['users.updated_at']
                }
                this_user = users_model.User(user_data)
                this_album.poster = this_user
                all_albums.append(this_album)
            return all_albums
        return []

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM albums JOIN users on users.id = albums.user_id WHERE albums.id = %(id)s;"
        results = connectToMySQL('spotify').query_db(query, data)
        if len(results) < 1:
            return False
        row = results[0]
        this_album = cls(row)
        user_data = {
            **row,
            'id': row['users.id'],
            'created_at': row['users.created_at'],
            'updated_at': row['users.updated_at']
        }
        poster = users_model.User(user_data)
        this_album.poster = poster
        return this_album

    @classmethod
    def update(cls, data):
        query = "UPDATE albums SET album_title = %(album_title)s, artist = %(artist)s, genre = %(genre)s, favorite_song = %(favorite_song)s WHERE id = %(id)s;"
        return connectToMySQL('spotify').query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE from albums where ID = %(id)s;"
        return connectToMySQL('spotify').query_db(query, data)

    @staticmethod
    def validator(form_data):
        is_valid = True
        if len(form_data['album_title']) < 1:
            flash("title required")
            is_valid = False
        if len(form_data['artist']) < 1:
            flash("artist required")
            is_valid = False
        if len(form_data['genre']) < 1:
            flash("genre required")
            is_valid = False
        if len(form_data['favorite_song']) < 1:
            flash("favorite song required")
            is_valid = False
        return is_valid
