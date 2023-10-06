from flask import Flask, jsonify
from src.config.config import config_dict
from src.models.database import db, migrate
from os import path
from src.auth.auth import auth

def create_app(config = config_dict["dev"]):
     
     app = Flask(__name__)
     app.config.from_object(config)
     db.init_app(app=app)
     migrate.init_app(app=app)

     create_database(app=app)

     @app.errorhandler(404)
     def handle_not_found(e):
         return jsonify({"error": str(e)})
     

     @app.errorhandler(500)
     def handle_not_found(e):
         return jsonify({"error": str(e)})
     
     app.register_blueprint(auth)
     
     return app


def create_database(app):
    if not path.exists("src/database.db"):
        with app.app_context():
            db.create_all()
            print("database created")