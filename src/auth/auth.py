from flask import Blueprint, request, jsonify
from src.models.database import User, db
from werkzeug.security import generate_password_hash, check_password_hash
import re

auth = Blueprint("auth", __name__, url_prefix="/api/auth")

""" A module to get user registration data """
@auth.post("/register")
def register_user():
          error_message = {"Registration failed": "make sure to double check your credentials"}

          if not request.content_type == "application/json":
              return jsonify({"Registration failed": "content_type must be appliaction/json"}), 401
          
          else:
              request_data = request.get_json()
              if not verify_user_registration_details(request_data):
                  return jsonify(error_message), 400
              
              elif not verify_user_email(request_data["email"]):
                 return jsonify({"Registration failed": "Email is badly formated"}), 400
        
              elif not verify_password(request_data["password"]):
                  return jsonify({"Registration failed": "password must not be less tha 6 characters"}), 400

              
              hashed_password = handle_password_hashing(request_data["email"], request_data["password"])
              if hashed_password:
                    new_user = User(first_name=request_data["first_name"],
                              last_name=request_data["last_name"],
                              email=request_data["email"],
                              password=hashed_password)
                    
                    db.session.add(new_user)
                    db.session.commit()
                    return jsonify({"first_name": request_data["first_name"],
                              "last_name": request_data["last_name"],
                              "email": request_data["email"],
                              "password": request_data["password"], 
                              }), 201

          return jsonify({"failed": "email already taken"}), 409



def verify_user_registration_details(new_user):
    if "first_name" in new_user and "last_name" in new_user and "email" in new_user \
    and "password" in new_user:
        return True
    
    return False

def verify_user_email(email):
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return True
    
    return False
        

def verify_password(password):
    return len(password) > 6


def handle_password_hashing(email, password):
    existing_email = User.query.filter_by(email=email).first()
    if not existing_email:
        hashed_password = generate_password_hash(password)
        return hashed_password
    
    return False

def verify_user_login_credentials(request_body):
    if "email" in request_body and "password" in request_body:
        return True
    
    return False

def check_login_password(email, password):
    existing_email = User.query.filter_by(email=email).first()
    if existing_email:
        if check_password_hash(existing_email.password, password):
            return existing_email
        
        return False
    return False