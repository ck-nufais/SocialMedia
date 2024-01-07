from flask import Flask
from config import Configurations
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sqlalchemy as sa
import sqlalchemy.orm as so
from flask_login import LoginManager
app = Flask(__name__)
Login = LoginManager(app)
Login.login_view='login'
app.config.from_object(Configurations)
db = SQLAlchemy(app)
migrate = Migrate(app,db)

import models,routes 

from models import Users
@app.shell_context_processor
def make_shell_context():
    return {'sql': sa, 'orm': so, 'db': db, 'User': Users}


