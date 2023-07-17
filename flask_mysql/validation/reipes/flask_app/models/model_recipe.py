from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB, bcrypt
from flask import flash, session
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9]).{8,}$')
''' (?=.*?[A-Z]) : At least one upper case English letter
    (?=.*?[a-z]) : At least one lower case English letter
    (?=.*?[0-9]) : At least one digit
    (?=.*?[#?!@$ %^&*-]) : At least one special character or space (not used in this case)
    .{8,} : Minimum eight in length
'''
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

class Recipe:

  def __init__( self , data ):
    self.id = data['id']
    self.name = data['name']
    self.description = data['description']
    self.instructions = data['instructions']
    self.date_made = data['date_made']
    self.under_30 = data['under_30']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']

  @classmethod
  def save(cls, data):
    query = "INSERT INTO recipes ( name, description, instructions, date_made, under_30, user_id) VALUES ( %(name)s, %(description)s, %(instructions)s, %(date_made)s, %(under_30)s, %(user_id)s);"
    return connectToMySQL(DB).query_db( query, data )

  @classmethod
  def get_all(cls):
    query = "SELECT * FROM recipes JOIN users ON recipes.user_id = users.id;"
    return connectToMySQL(DB).query_db( query )

  @classmethod
  def delete(cls, id):
    query = "DELETE FROM recipes WHERE id = %(id)s;"
    return connectToMySQL(DB).query_db(query, {'id':id})

  @classmethod
  def get_by_id(cls, id):
    query = "SELECT * FROM recipes WHERE id = %(id)s"
    results = connectToMySQL(DB).query_db(query, {'id': id})
    print(results)
    if results:
      dict = results[0]
      return cls(dict)
