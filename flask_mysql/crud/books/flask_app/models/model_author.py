from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB
from flask_app.models import model_book

class Author:

  def __init__( self , data ):
    self.id = data['id']
    self.name = data['name']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']

  @classmethod
  def get_all(cls):
    query = "SELECT * FROM authors;"
    results = connectToMySQL(DB).query_db(query)
    authors = []
    for dict in results:
        authors.append( cls(dict) )
    return authors

  @classmethod
  def get_by_id_with_books(cls, id):
    query = '''
                SELECT * FROM authors
                LEFT JOIN favorites
                ON authors.id = favorites.author_id
                LEFT JOIN books
                ON favorites.book_id = books.id
                WHERE authors.id = %(id)s;
            '''
    results = connectToMySQL(DB).query_db(query, {'id':id})
    dict = results[0]
    author_instance = cls(dict)
    author_instance.favorite_books = []

    if (dict['books.id'] != None):
      for book in results:
        book_data = {
          "id" : book["books.id"],
          "title" : book["title"],
          "num_of_pages" : book["num_of_pages"],
          "created_at" : book["books.created_at"],
          "updated_at" : book["books.updated_at"]
        }
        book_instance = model_book.Book(book_data)
        author_instance.favorite_books.append(book_instance)

    return author_instance

  @classmethod
  def save(cls, data ):
    query = "INSERT INTO authors ( name ) VALUES ( %(name)s );"
    return connectToMySQL(DB).query_db( query, data )

  @classmethod
  def add_favorite(cls, data):
    query = "INSERT INTO favorites ( author_id, book_id ) VALUES ( %(author_id)s, %(book_id)s );"
    return connectToMySQL(DB).query_db( query, data )

  # @classmethod
  # def get_by_id_with_ninjas(cls, id):
  #   query = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
  #   results = connectToMySQL(DB).query_db(query, {'id':id})
  #   dict = results[0]
  #   dojo_instance = cls(dict)
  #   dojo_instance.all_ninjas = []

  #   if dict['ninjas.id'] != None :
  #     for ninja in results:
  #       ninja_data = {
  #         #conflicting columns
  #         'id': ninja['ninjas.id'],
  #         'created_at': ninja['ninjas.created_at'],
  #         'updated_at': ninja['ninjas.updated_at'],
  #         #rest of the columns
  #         'first_name': ninja['first_name'],
  #         'last_name': ninja['last_name'],
  #         'age': ninja['age'],
  #       }
  #       ninja_instance = model_book.Ninja(ninja_data)
  #       dojo_instance.all_ninjas.append(ninja_instance)

  #   return dojo_instance
