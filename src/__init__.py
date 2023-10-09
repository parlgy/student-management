from flask import Flask, jsonify
from src.config.config import config_dict
from src.models.database import db, migrate, User
from os import path
from src.auth.auth import auth
from flask_login import LoginManager

login_manager = LoginManager()

""" A module for creating an application """
def create_app(config = config_dict["dev"]):
     
     app = Flask(__name__)
     app.config.from_object(config)
     db.init_app(app=app)
     migrate.init_app(app=app)
     login_manager.init_app(app=app)
     login_manager.login_view = "auth.login_user"

     create_database(app=app)

     @app.errorhandler(404)
     def handle_not_found(e):
         return jsonify({"error": str(e)})
     

     @app.errorhandler(500)
     def handle_not_found(e):
         return jsonify({"error": str(e)})
     
     app.register_blueprint(auth)

     @login_manager.user_loader
     def load_user(user_id):
         return User.query.get(int(user_id))
     
     return app


def create_database(app):
    if not path.exists("src/database.db"):
        with app.app_context():
            db.create_all()
            print("database created")