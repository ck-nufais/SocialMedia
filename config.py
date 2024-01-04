import os

base = os.path.abspath(os.path.dirname(__file__))

class Configurations:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "its secret"
    SQLALCHEMY_DATABASE_URI  = os.environ.get("DATABASE_URL") or "sqlite:///"+os.path.join(base,"app.db") 
