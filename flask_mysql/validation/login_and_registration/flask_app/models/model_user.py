from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB, bcrypt
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:

  def __init__( self , data ):
    self.id = data['id']
    self.first_name = data['first_name']
    self.last_name = data['last_name']
    self.email = data['email']
    self.date_of_birth = data['date_of_birth']
    self.password = data['password']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']


  @classmethod
  def save(cls, data):
    query = "INSERT INTO users ( first_name, last_name, email, date_of_birth, password ) VALUES ( %(first_name)s, %(last_name)s, %(email)s, %(date_of_birth)s, %(password)s );"
    return connectToMySQL(DB).query_db( query, data )

  @classmethod
  def get_by_email(cls, data):
    query = "SELECT * FROM users WHERE users.email = %(email)s"
    results = connectToMySQL(DB).query_db( query, data )
    dict = results[0]
    return cls(dict)


  @staticmethod
  def validate_regitration(data):
    is_valid = True

    if len(data['first_name']) < 3:
      flash("Please fill in your first name", "err_first_name")
      is_valid = False

    if len(data['last_name']) < 3:
      flash("Please fill in your last name.", "err_last_name")
      is_valid = False

    if len(data['email']) < 1:
      flash("Please fill in your email.", "err_email")
      is_valid = False
    elif not EMAIL_REGEX.match(data['email']):
      flash("Invalid email address.", "err_email")
      is_valid = False

    if len(data['date_of_birth']) < 1:
      flash("Please select your date of birth.", "err_date_of_birth")
      is_valid = False

    if len(data['password']) < 9:
      flash("Please choose your password.", "err_password")
      is_valid = False

    if len(data['confirm_password']) < 9 or not data['password'] == data['confirm_password']:
      flash("Please confirm your password.", "err_confirm_password")
      is_valid = False


    return is_valid

