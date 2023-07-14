from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.model_author import Author
from flask_app.models.model_book import Book

@app.route("/authors")
def get_all_authors():
  authors = Author.get_all()
  return render_template("authors.html", authors=authors)

@app.route("/authors/<int:id>")
def get_author_by_id(id):
  author = Author.get_by_id_with_books(id)
  unfavorite_books = Book.get_unfavorited_authors_books(id)
  return render_template("single_author.html", author=author, unfavorite_books=unfavorite_books)

@app.route('/authors/create', methods=["POST"])
def author_create():
  data = {
  "name": request.form["name"],
  }
  Author.save(data)
  return redirect('/authors')

@app.route('/authors/add/<int:id>', methods=["POST"])
def author_add_favorite(id):
  data = {
  "author_id": id,
  "book_id": request.form["book_id"],
  }
  Author.add_favorite(data)
  return redirect(f'/authors/{id}')
