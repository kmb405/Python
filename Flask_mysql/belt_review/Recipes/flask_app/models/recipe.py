from flask_app.config.my_db_connection import connecttoMySQL
from flask import flash


class Recipe:
    DB = 'recipes'

    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.name = data['name']
        self.under_30 = data['under_30']
        self.description = data['description']
        self.instructions = data['instructions']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
        # check validity
        if len(recipe['name']) < 3:
            flash("Name must be longer than 2 Characters", 'recipe')
            is_valid = False
        if len(recipe['description']) < 10:
            flash("Description cannot be blank", 'recipe')
            is_valid = False
        if len(recipe['instructions']) < 10:
            flash("Instructions cannot be blank", 'recipe')
            is_valid = False
        return is_valid


    @classmethod
    def get_all_recipes(cls):
        query = 'SELECT * FROM recipes;'
        result = connecttoMySQL(cls.DB).query_db(query)
        recipes = []
        for recipe in result:
            recipes.append(recipe)
        return recipes
    
    @classmethod
    def get_one_user(cls, id):
        data = {'id': id}
        query = 'SELECT * FROM recipes WHERE id=%(id)s;'
        results =  connecttoMySQL(cls.DB).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])
    
    @classmethod
    def create_user(cls, data):
        query = 'INSERT INTO recipes (name, user_id, under_30, description, instructions, created_at, updated_at) VALUES (%(name)s, %(user_id)s, %(under_30)s, %(description)s, %(instructions)s, NOW(), NOW());'
        results = connecttoMySQL(cls.DB).query_db(query, data)
        return results
    
    @classmethod
    def update_user(cls, data):
        query = 'UPDATE recipes SET name=%(name)s, user_id=%(user_id)s, under_30=%(under_30)s, description=%(description)s, instructions=%(instructions)s, updated_at=NOW() WHERE id=%(id)s;'
        return connecttoMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def delete_user(cls, id):
        query = 'DELETE from recipes WHERE id = %(id)s;'
        data = {'id': id}
        return connecttoMySQL(cls.DB).query_db(query,data)

