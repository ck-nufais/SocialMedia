from main import db,Login
from sqlalchemy import String
from sqlalchemy.orm import relationship,Mapped,mapped_column,WriteOnlyMapped
from werkzeug.security import generate_password_hash ,check_password_hash
from flask_login import UserMixin





class Users(UserMixin,db.Model):
    id:Mapped[int] = mapped_column(primary_key=True)
    username:Mapped[str] = mapped_column(String(50),index=True,unique=True)
    email:Mapped[str] = mapped_column(String(60),index=True,unique=True)
    password:Mapped[str]=mapped_column(String(256))
    def generate_hash(self,password):
        self.password = generate_password_hash(password)
    def check_hash(self,password):
        return check_password_hash(self.password,password)


@Login.user_loader          
def load(id):               
    return db.session.get(Users,int(id)) 
                            
