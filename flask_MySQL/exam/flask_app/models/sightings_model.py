from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import users_model

class Sighting:
    def __init__(self,data):
        self.id = data['id']
        self.location = data['location']
        self.what_happened = data['what_happened']
        self.date = data['date']
        self.num = data['num']
        self.created__at = data['created_at']
        self.updated__at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def create(cls,data):
        query = "INSERT INTO sightings (location, what_happened, date, num, user_id) VALUES (%(location)s, %(what_happened)s, %(date)s, %(num)s, %(user_id)s);"
        return connectToMySQL('sasquatch').query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM sightings JOIN users on sightings.user_id = users.id;" 
        results = connectToMySQL('sasquatch').query_db(query)
        if len(results) > 0:
            all_sightings = []
            for row in results:
                this_sighting = cls(row)
                user_data = {
                    **row,
                    'id' : row['users.id'],
                    'created_at': row['users.created_at'],
                    'updated_at': row['users.updated_at']
                }
                this_user = users_model.User(user_data)
                this_sighting.reporter = this_user
                all_sightings.append(this_sighting)
            return all_sightings
        return []

    @classmethod 
    def get_by_id(cls,data):
        query = "SELECT * FROM sightings JOIN users on users.id = sightings.user_id WHERE sightings.id = %(id)s;"
        results = connectToMySQL('sasquatch').query_db(query, data)
        if len(results) < 1:
            return False
        row = results[0]
        this_sighting = cls(row)
        user_data = {
            **row,
            'id' : row['users.id'],
            'created_at': row['users.created_at'],
            'updated_at': row['users.updated_at']
        }
        reporter = users_model.User(user_data)
        this_sighting.reporter = reporter
        return this_sighting

    @classmethod
    def update(cls,data):
        query = "UPDATE sightings SET location = %(location)s, what_happened = %(what_happened)s, date = %(date)s, num = %(num)s WHERE id = %(id)s;"
        return connectToMySQL('sasquatch').query_db(query,data)
    
    @classmethod
    def delete(cls,data):
        query = "DELETE from sightings where ID = %(id)s;"
        return connectToMySQL('sasquatch').query_db(query,data)

    @staticmethod
    def validator(form_data):
        is_valid = True
        if len(form_data['location']) < 1:
            flash("location required")
            is_valid = False
        if len(form_data['what_happened']) < 1:
            flash("what happened required")
            is_valid = False
        if len(form_data['date']) < 1:
            flash("date required")
            is_valid = False
        if len(form_data['num']) < 1:
            flash("# required")
            is_valid = False
        return is_valid

