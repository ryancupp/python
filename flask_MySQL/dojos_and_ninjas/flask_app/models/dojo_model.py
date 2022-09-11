from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja_model

class Dojo:
    def __init__ (self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def new_dojo(cls,data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s)"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        return result

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []
        for u in results:
            dojos.append( cls(u) )
        return dojos

    @classmethod
    def get_dojo_with_ninjas(cls,data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = dojo_id WHERE dojos.id = %(id)s"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        print(results)
        dojo = cls(results[0])
        ninja_list =[]
        for row_from_db in results:
            ninja_data= {
                "id": row_from_db["ninjas.id"],
                "first_name" : row_from_db["first_name"],
                "last_name" : row_from_db["last_name"],
                "age" : row_from_db["age"],
                "created_at" : row_from_db["ninjas.created_at"],
                "updated_at" : row_from_db["ninjas.updated_at"],
                "dojo_id" : row_from_db["dojo_id"],
            }
            ninja_instance = ninja_model.Ninja(ninja_data)
            ninja_list.append(ninja_instance)
            dojo.ninjas = ninja_list
        return dojo