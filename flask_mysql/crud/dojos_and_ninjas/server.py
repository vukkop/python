from flask_app import app

from flask_app.controllers import controller_routes, controller_dojo, controller_ninja

if __name__ == "__main__":
    app.run(debug=True)

