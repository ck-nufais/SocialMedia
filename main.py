from flask import Flask
from config import Configurations
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Configurations)
db = SQLAlchemy(app)
migrate = Migrate(app,db)

import models,routes 

