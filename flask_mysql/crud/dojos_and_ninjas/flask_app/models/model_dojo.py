from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
  DB = "dojos_and_ninjas"
  def __init__( self , data ):
    self.id = data['id']
    self.name = data['name']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']

  @classmethod
  def get_all(cls):
    query = "SELECT * FROM dojos;"
    results = connectToMySQL(cls.DB).query_db(query)
    dojos = []
    for dict in results:
        dojos.append( cls(dict) )
    return dojos

  @classmethod
  def get_by_id(cls, id):
    query = "SELECT * FROM dojos WHERE id =  %(id)s;"
    results = connectToMySQL(cls.DB).query_db(query, {'id':id})
    user = results[0]
    return user

  # @classmethod
  # def save(cls, data ):
  #   query = "INSERT INTO users ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(email)s , NOW() , NOW() );"
  #   return connectToMySQL(cls.DB).query_db( query, data )

  # @classmethod
  # def update(cls, data):
  #   query = "UPDATE `users` SET `first_name` = %(fname)s, `last_name` = %(lname)s, `email` = %(email)s WHERE (`id` = %(id)s);"
  #   return connectToMySQL(cls.DB).query_db( query, data)

  # @classmethod
  # def delete(cls, id):
  #   query = "DELETE FROM users WHERE id = %(id)s;"
  #   return connectToMySQL(cls.DB).query_db(query, {'id':id})
