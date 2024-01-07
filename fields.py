from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,EmailField,SubmitField
from wtforms.validators import DataRequired

class Login(FlaskForm):
    username = StringField("Username",validators=[DataRequired()])
    password = PasswordField("PasswordField",validators=[DataRequired()])
    email = EmailField("Email :<")
    state = BooleanField("remember Me")
    submit = SubmitField("Log in")
    
