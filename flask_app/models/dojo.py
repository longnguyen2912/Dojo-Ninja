from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojo_and_ninja_schema').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos(name) VALUES (%(name)s);"
        results = connectToMySQL("dojo_and_ninja_schema").query_db(query,data)
        return results
    
    @classmethod
    def get_ninja(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL("dojo_and_ninja_schema").query_db(query,data)
        dojo = cls(results[0])
        all_ninjas = []
        for row in results:
            n = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['ninjas.updated_at'],
                'dojo_id': row['dojo_id']
            }
            ninja_instance = ninja.Ninja(n)
            all_ninjas.append(ninja_instance)
        print(dojo)
        dojo.all_ninjas = all_ninjas
        return dojo