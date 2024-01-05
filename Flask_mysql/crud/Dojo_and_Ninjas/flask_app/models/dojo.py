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
    def get_one_dojo(cls, data):
        query = 'SELECT * FROM dojos WHERE id=%(id)s;'
        results =  connecttoMySQL(cls.DB).query_db(query, data)
        return cls(results[0])
    
    @classmethod
    def add_dojo(cls, data):
        query = 'INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());'
        results = connecttoMySQL(cls.DB).query_db(query, data)
        return results

class Ninja:
    DB = 'dojos_and_ninjas_schema'

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_all_ninjas(cls):
        query = 'SELECT * FROM ninjas;'
        result = connecttoMySQL(cls.DB).query_db(query)
        ninjas = []
        for ninja in result:
            ninjas.append(ninja)
        return ninjas
    
    @classmethod
    def get_one_ninja(cls, data):
        query = 'SELECT * FROM ninjas WHERE id=%(id)s;'
        results =  connecttoMySQL(cls.DB).query_db(query, data)
        return cls(results[0])
    
    @classmethod
    def add_dojo(cls, data):
        query = 'INSERT INTO dojos (first_name, last_name, age, created_at, updated_at) VALUE (%(first_name)s,%(last_name)s,%(age)s,NOW(),NOW());'
        results = connecttoMySQL(cls.DB).query_db(query, data)
        return results