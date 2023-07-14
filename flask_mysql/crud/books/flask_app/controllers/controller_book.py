from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.model_book import Book
from flask_app.models.model_author import Author


@app.route("/books")
def book_get_all():
  books = Book.get_all()
  return render_template("books.html", books=books)

@app.route('/books/create', methods=["POST"])
def book_create():
  data = {
  "title": request.form["title"],
  "num_of_pages": request.form["num_of_pages"],
  }
  Book.save(data)
  return redirect(f'/books')
