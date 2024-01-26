from flask_app.config.my_db_connection import connecttoMySQL
from flask import flash


class Ride:
    DB = 'rideshares'

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
    def validate_ride(ride):
        is_valid = True
        # check validity
        if len(ride['name']) < 4:
            flash("Name must be longer than 2 Characters", 'ride')
            is_valid = False
        if len(ride['description']) < 4:
            flash("Description cannot be blank", 'ride')
            is_valid = False
        if len(ride['instructions']) < 4:
            flash("Instructions cannot be blank", 'ride')
            is_valid = False
        if len(ride['created_at']) < 10:
            flash("Date cannot be blank", 'ride')
        return is_valid


    @classmethod
    def get_all_rides(cls):
        query = 'SELECT * FROM rides JOIN users ON rides.user_id=users.id;'
        result = connecttoMySQL(cls.DB).query_db(query)
        rides = []
        for ride in result:
            rides.append(ride)
        return rides
    
    @classmethod
    def get_one_ride(cls, ride_id):
        data = {'ride_id': ride_id}
        query = 'SELECT * FROM rides JOIN users ON rides.user_id=users.id WHERE rides.id=%(ride_id)s;'
        results =  connecttoMySQL(cls.DB).query_db(query, data)
        return results[0]
    
    @classmethod
    def create_ride(cls, data):
        query = 'INSERT INTO rides (name, user_id, under_30, description, instructions, created_at, updated_at) VALUES (%(name)s, %(user_id)s, %(under_30)s, %(description)s, %(instructions)s, NOW(), NOW());'
        results = connecttoMySQL(cls.DB).query_db(query, data)
        return results
    
    @classmethod
    def update_ride(cls, data):
        query = 'UPDATE rides SET name=%(name)s, user_id=%(user_id)s, under_30=%(under_30)s, description=%(description)s, instructions=%(instructions)s, updated_at=NOW() WHERE id=%(ride_id)s;'
        results = connecttoMySQL(cls.DB).query_db(query, data)
        return results
    
    @classmethod
    def delete_ride(cls, id):
        query = 'DELETE from rides WHERE id = %(id)s;'
        data = {'id': id}
        return connecttoMySQL(cls.DB).query_db(query,data)

