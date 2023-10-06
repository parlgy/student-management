from flask import Blueprint

auth = Blueprint("auth", __name__, url_prefix="/api/auth")

@auth.get("/home")
def home():
          return {"welcome": "Welcome my friend"}