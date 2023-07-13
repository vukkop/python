from flask_app.config.mysqlconnection import connectToMySQL

class User:
  def __init__( self , data ):
    self.id = data['id']
    self.first_name = data['first_name']
    self.last_name = data['last_name']
    self.email = data['email']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']

  @classmethod
  def get_all(cls):
    query = "SELECT * FROM users;"
    results = connectToMySQL('users').query_db(query)
    users = []
    for dict in results:
        users.append( cls(dict) )
    return users

  @classmethod
  def get_by_id(cls, id):
    query = "SELECT * FROM users WHERE id =  %(id)s;"
    results = connectToMySQL('users').query_db(query, {'id':id})
    user = results[0]
    return user

  @classmethod
  def save(cls, data ):
    query = "INSERT INTO users ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(email)s , NOW() , NOW() );"
    return connectToMySQL('users').query_db( query, data )

  @classmethod
  def update(cls, data):
    query = "UPDATE `users` SET `first_name` = %(fname)s, `last_name` = %(lname)s, `email` = %(email)s WHERE (`id` = %(id)s);"
    return connectToMySQL('users').query_db( query, data)

  @classmethod
  def delete(cls, id):
    query = "DELETE FROM users WHERE id = %(id)s;"
    return connectToMySQL('users').query_db(query, {'id':id})
