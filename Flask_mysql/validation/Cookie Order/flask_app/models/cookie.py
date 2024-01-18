from flask_app.config.my_db_connection import connecttoMySQL
from flask import flash

class Cookie:
    DB = 'cookie_orders'

    def __init__(self, data):
        self.id = data['id']
        self.customer_name = data['customer_name']
        self.cookie_type = data['cookie_type']
        self.number_of_boxes = data['number_of_boxes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_order(order):
        is_valid = True
        # check validity
        if len(order['customer_name']) < 3 or len(order['cookie_type']) < 3 or order['number_of_boxes'] == '':
            flash('All fields required')
            is_valid = False
        if len(order['customer_name']) < 3:
            flash("Name must be longer than 2 Characters")
            is_valid = False
        if len(order['cookie_type']) < 3:
            flash('Cookie type must be longer than 2 Characters')
            is_valid = False
        if order['number_of_boxes'] == '':
            flash('Please enter a valid number of boxes')
            is_valid = False
        return is_valid


    @classmethod
    def get_all_orders(cls):
        query = 'SELECT * FROM orders;'
        result = connecttoMySQL(cls.DB).query_db(query)
        orders = []
        for order in result:
            orders.append(order)
        return orders
    
    @classmethod
    def get_one_order(cls, id):
        data = {'id': id}
        query = 'SELECT * FROM orders WHERE id=%(id)s;'
        results =  connecttoMySQL(cls.DB).query_db(query, data)
        return cls(results[0])
    
    @classmethod
    def create_order(cls, data):
        query = 'INSERT INTO orders (customer_name, cookie_type, number_of_boxes, created_at, updated_at) VALUES (%(customer_name)s, %(cookie_type)s, %(number_of_boxes)s, NOW(), NOW());'
        results = connecttoMySQL(cls.DB).query_db(query, data)
        return results
    
    @classmethod
    def update_order(cls, data):
        query = 'UPDATE orders SET customer_name=%(customer_name)s, cookie_type=%(cookie_type)s, number_of_boxes=%(number_of_boxes)s, updated_at=NOW() WHERE id=%(id)s;'
        return connecttoMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def delete_order(cls, id):
        query = 'DELETE from orders WHERE id = %(id)s;'
        data = {'id': id}
        return connecttoMySQL(cls.DB).query_db(query,data)

