from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB

class Book:

  def __init__( self , data ):
    self.id = data['id']
    self.title = data['title']
    self.num_of_pages = data['num_of_pages']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']

  @classmethod
  def get_all(cls):
    query = "SELECT * FROM books;"
    results = connectToMySQL(DB).query_db(query)
    books = []
    for dict in results:
        books.append( cls(dict) )
    return books

  @classmethod
  def get_unfavorited_authors_books(cls, id):
    query = "SELECT * FROM books WHERE books.id NOT IN ( SELECT book_id FROM favorites WHERE author_id = %(id)s );"
    books = []
    results = connectToMySQL(DB).query_db(query, {'id':id})
    for row in results:
      books.append(cls(row))
    return books

  @classmethod
  def save(cls, data ):
    query = "INSERT INTO books ( title , num_of_pages ) VALUES ( %(title)s , %(num_of_pages)s);"
    return connectToMySQL(DB).query_db( query, data )

  # @classmethod
  # def get_by_id(cls, id):
  #   query = "SELECT * FROM users WHERE id =  %(id)s;"
  #   results = connectToMySQL(cls.DB).query_db(query, {'id':id})
  #   user = results[0]
  #   return user

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
