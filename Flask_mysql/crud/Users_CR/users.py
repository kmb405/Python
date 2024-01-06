from my_db_connection import connecttoMySQL

class User:
    DB = 'user_schema'

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM users;'
        results = connecttoMySQL(cls.DB).query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users
    
    @classmethod
    def get_one(cls, data):
        query = 'SELECT * FROM users WHERE id = %(id)s;'
        results = connecttoMySQL(cls.DB).query_db(query, data)
        return cls(results[0])
    
    @classmethod
    def add_one(cls, data):
        query = 'INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUE (%(first_name)s,%(last_name)s,%(email)s,NOW(),NOW());'
        results = connecttoMySQL(cls.DB).query_db(query, data)
        return results
    
    @classmethod
    def update(cls, data):
        query = 'UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s, updated_at=NOW() WHERE id=%(id)s;'
        return connecttoMySQL(cls.DB).query_db(query,data)
    
    @classmethod
    def delete(cls, id):
        query = 'DELETE from users WHERE id = %(id)s;'
        data = {'id': id}
        return connecttoMySQL(cls.DB).query_db(query,data)