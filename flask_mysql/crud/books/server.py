from flask_app import app

from flask_app.controllers import controller_book, controller_routes, controller_author

if __name__ == "__main__":
    app.run(debug=True)

