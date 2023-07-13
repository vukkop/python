from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB
from flask_app.models import model_ninja

class Dojo:

  def __init__( self , data ):
    self.id = data['id']
    self.name = data['name']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']

  @classmethod
  def get_all(cls):
    query = "SELECT * FROM dojos;"
    results = connectToMySQL(DB).query_db(query)
    dojos = []
    for dict in results:
        dojos.append( cls(dict) )
    return dojos

  @classmethod
  def get_by_id(cls, id):
    query = "SELECT * FROM dojos WHERE id = %(id)s;"
    results = connectToMySQL(DB).query_db(query, {'id':id})
    dict = results[0]
    return cls(dict)

  @classmethod
  def save(cls, data ):
    query = "INSERT INTO dojos ( name ) VALUES ( %(dojo_name)s );"
    return connectToMySQL(DB).query_db( query, data )

  @classmethod
  def get_by_id_with_ninjas(cls, id):
    query = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
    results = connectToMySQL(DB).query_db(query, {'id':id})
    dict = results[0]
    dojo_instance = cls(dict)
    dojo_instance.all_ninjas = []

    if dict['ninjas.id'] != None :
      for ninja in results:
        ninja_data = {
          #conflicting columns
          'id': ninja['ninjas.id'],
          'created_at': ninja['ninjas.created_at'],
          'updated_at': ninja['ninjas.updated_at'],
          #rest of the columns
          'first_name': ninja['first_name'],
          'last_name': ninja['last_name'],
          'age': ninja['age'],
        }
        ninja_instance = model_ninja.Ninja(ninja_data)
        dojo_instance.all_ninjas.append(ninja_instance)

    return dojo_instance
