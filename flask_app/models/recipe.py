from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.user import User
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
db_name = 'recipes'

class Recipe:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.under = data['under']
        self.description = data['description']
        self.instructions = data['instructions']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO recipes (name, under, description, instructions, created_at, updated_at) VALUES(%(name)s,%(under)s,%(description)s,%(instructions)s)"
        return connectToMySQL(db_name).query_db(query,data)

    @classmethod
    def get_all(cls) -> list:
        query = "SELECT * FROM recipes"
        results = connectToMySQL(db_name).query_db(query)
        recipes = []
        for recipe in results:
            recipes.append(cls(recipe))
        return recipes

    @classmethod
    def get_one(cls,data:dict) -> list:
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        results = connectToMySQL(db_name).query_db(query,data)
        if results:
            return cls(results[0])
        return False

    @staticmethod
    def validator(data:dict) -> bool:
        is_valid = True
        if len(data['name']) < 3:
            is_valid = False
            flash("Recipe name must be at least 3 characters.","new")
        if len(data['description']) < 3:
            is_valid = False
            flash("Description must be at least 3 characters.","new")
        if len(data['instructions']) < 3:
            is_valid = False
            flash("Instructions must be at least 3 characters.","new")
        return is_valid


    
        

