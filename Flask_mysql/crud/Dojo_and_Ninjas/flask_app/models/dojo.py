from flask_app.config.my_db_connection import connecttoMySQL

class Dojo:
    DB = 'dojos_and_ninjas_schema'

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_dojos(cls):
        query = 'SELECT * FROM dojos;'
        result = connecttoMySQL(cls.DB).query_db(query)
        dojos = []
        for dojo in result:
            dojos.append(dojo)
        return dojos
    
    @classmethod
    def get_one_dojo(cls, id):
        print(id)
        data = {'id': id}
        query = 'SELECT * FROM dojos WHERE id=%(id)s;'
        results =  connecttoMySQL(cls.DB).query_db(query, data)
        return cls(results[0])
    
    @classmethod
    def create_dojo(cls, data):
        query = 'INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());'
        results = connecttoMySQL(cls.DB).query_db(query, data)
        return results
    
    @classmethod
    def update_dojo(cls, data):
        query = 'UPDATE dojos SET name=%(name)s, updated_at=NOW() WHERE id=%(id)s;'
        return connecttoMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def delete_dojo(cls, id):
        query = 'DELETE from dojos WHERE id = %(id)s;'
        data = {'id': id}
        return connecttoMySQL(cls.DB).query_db(query,data)


class Ninja:
    DB = 'dojos_and_ninjas_schema'

    def __init__(self, data):
        self.id = data['id']
        self.dojo_id = data['dojo_id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_all_ninjas(cls, id):
        data = {'id': int(id)}
        query = 'SELECT * FROM ninjas WHERE dojo_id=%(id)s;'
        result = connecttoMySQL(cls.DB).query_db(query, data)
        ninjas = []
        for ninja in result:
            ninjas.append(ninja)
        return ninjas
    
    @classmethod
    def get_one_ninja(cls, id):
        data = {'id': id}
        query = 'SELECT * FROM ninjas WHERE id=%(id)s;'
        results =  connecttoMySQL(cls.DB).query_db(query, data)
        return cls(results[0])
    
    @classmethod
    def get_ninja_dojo_id(cls, id):
        data = {'id': id}
        query = 'SELECT dojo_id FROM ninjas WHERE id=%(id)s;'
        results =  connecttoMySQL(cls.DB).query_db(query, data)
        return results
    
    @classmethod
    def create_ninja(cls, data):
        query = 'INSERT INTO ninjas (dojo_id, first_name, last_name, age, created_at, updated_at) VALUE (%(dojo_id)s,%(first_name)s,%(last_name)s,%(age)s,NOW(),NOW());'
        results = connecttoMySQL(cls.DB).query_db(query, data)
        return results
    
    @classmethod
    def update_ninja(cls, data):
        print(data)
        query = 'UPDATE ninjas SET first_name=%(first_name)s, last_name=%(last_name)s, age=%(age)s, updated_at=NOW() WHERE id=%(id)s;'
        return connecttoMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def delete_ninja(cls, id):
        query = 'DELETE from ninjas WHERE id = %(id)s;'
        data = {'id': id}
        return connecttoMySQL(cls.DB).query_db(query,data)