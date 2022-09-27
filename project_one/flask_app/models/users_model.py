from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import albums_model
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls, data):
        query = "INSERT into users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL('spotify').query_db(query,data)

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users where email = %(email)s;"
        results = connectToMySQL('spotify').query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM users LEFT JOIN albums on users.id = albums.user_id WHERE users.id = %(id)s;"
        results = connectToMySQL('spotify').query_db(query,data)
        if len(results) < 1:
            return False
        user = cls(results[0])
        list_of_albums = []
        for row in results:
            if row['albums.id'] == None:
                break
            album_data= {
                **row,
                'id' : row['albums.id'],
                'created_at' : row['albums.created_at'],
                'updated_at' : row['albums.updated_at']
            }
            this_album = albums_model.Album(album_data)
            list_of_albums.append(this_album)
        user.albums = list_of_albums
        return user

    @staticmethod
    def validate(user_data):
        is_valid = True
        if len(user_data['first_name']) < 2:
            flash("First Name Required", "reg")
            is_valid = False
        if len(user_data['last_name']) < 2:
            flash("Last Name Required", "reg")
            is_valid = False
        if len(user_data['email']) < 2:
            flash("Email Required", "reg")
            is_valid = False
        elif not EMAIL_REGEX.match(user_data['email']):
            flash("Invalid Email Format", "reg")
            is_valid = False
        else:
            data = {
                'email' : user_data['email']
            }
            potential_user = User.get_by_email(data)
            if potential_user:
                flash("Email Already Registered")
                is_valid = False
        if len(user_data['password']) < 8:
            flash("Password not long enough", "reg")
            is_valid = False
        elif not user_data['password'] == user_data['password2']:
            flash("Passes don't match", "reg")
            is_valid = False
        return is_valid
