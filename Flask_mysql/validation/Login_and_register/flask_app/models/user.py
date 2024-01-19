from flask_app.config.my_db_connection import connecttoMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    DB = 'users'

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_user(user):
        is_valid = True
        # check validity
        if len(user['first_name']) < 3:
            flash("First name must be longer than 2 Characters")
            is_valid = False
        if len(user['first_name']) < 3:
            flash("Last name must be longer than 2 Characters")
            is_valid = False
        if len(user['password']) < 3:
            flash('Password must be longer than 2 Characters')
            is_valid = False
        if not user['email'] in EMAIL_REGEX:
            flash('Please enter a valid email')
            is_valid = False
        return is_valid


    @classmethod
    def get_all_users(cls):
        query = 'SELECT * FROM users;'
        result = connecttoMySQL(cls.DB).query_db(query)
        users = []
        for user in result:
            users.append(user)
        return users
    
    @classmethod
    def get_one_user(cls, email):
        data = {'email': email}
        query = 'SELECT * FROM users WHERE email=%(email)s;'
        results =  connecttoMySQL(cls.DB).query_db(query, data)
        return cls(results[0])
    
    @classmethod
    def create_user(cls, data):
        query = 'INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());'
        results = connecttoMySQL(cls.DB).query_db(query, data)
        return results
    
    @classmethod
    def update_user(cls, data):
        query = 'UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s, password=%(password)s, updated_at=NOW() WHERE id=%(id)s;'
        return connecttoMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def delete_user(cls, id):
        query = 'DELETE from users WHERE id = %(id)s;'
        data = {'id': id}
        return connecttoMySQL(cls.DB).query_db(query,data)

