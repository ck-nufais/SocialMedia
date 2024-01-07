from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,EmailField,SubmitField, validators
from wtforms.validators import DataRequired,ValidationError,EqualTo,Email
from main import db
import sqlalchemy as sa
from models import Users as User
class Login(FlaskForm):
    username = StringField("Username or Email",validators=[DataRequired()])
    password = PasswordField("PasswordField",validators=[DataRequired()])
    state = BooleanField("remember Me")
    submit = SubmitField("Log in")

class Register(FlaskForm):
    username = StringField("Username",validators=[DataRequired()])
    email = EmailField("Email",validators=[DataRequired(),Email()])
    pass1 = PasswordField("Password",validators=[DataRequired()])
    pass2 = PasswordField("Repeat Password",validators=[DataRequired(),EqualTo("pass1")])
    submit = SubmitField("Register")

    def validate_username(self,username):
        user = db.session.scalar(sa.select(User).where(User.username == username.data))
        if user is not None:
            raise ValidationError("please use different username")

    def validate_email(self,email):
        user = db.session.scalar(sa.select(User).where(User.email == email.data))
        if user is not None:
            raise ValidationError("please use different Email")




    
