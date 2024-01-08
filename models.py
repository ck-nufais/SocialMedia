from main import db,Login
from sqlalchemy import String,ForeignKey,select,func
from sqlalchemy.orm import relationship,Mapped,mapped_column,WriteOnlyMapped
from werkzeug.security import generate_password_hash ,check_password_hash
from flask_login import UserMixin
from datetime import datetime,timezone

class Follow(db.Model):
    # id:Mapped[int] = mapped_column(primary_key=True)
    follower_id:Mapped[int] = mapped_column(ForeignKey("users.id"),primary_key=True)
    followed_id:Mapped[int] = mapped_column(ForeignKey("users.id"),primary_key=True)



class Users(UserMixin,db.Model):
    id:Mapped[int] = mapped_column(primary_key=True)
    username:Mapped[str] = mapped_column(String(50),index=True,unique=True)
    email:Mapped[str] = mapped_column(String(60),index=True,unique=True)
    password:Mapped[str]=mapped_column(String(256))
    posts:WriteOnlyMapped['Posts'] = relationship(back_populates="user")
    followers:WriteOnlyMapped["Users"] = relationship(back_populates="follows" ,secondary='follow',secondaryjoin=( id==Follow.followed_id),primaryjoin=(Follow.follower_id==id))
    follows:WriteOnlyMapped["Users"]= relationship(back_populates="followers", secondary='follow', primaryjoin=(Follow.followed_id == id), secondaryjoin=(Follow.follower_id == id))
    def generate_hash(self,password):
        self.password = generate_password_hash(password)
    def check_hash(self,password):
        return check_password_hash(self.password,password)
    def follow(self,user):
        if not self.is_following(user):
            self.follows.add(user)
    def unfollow(self,user):
        if self.is_following(user):
            self.follows.remove(user)

    def following_count(self):
        query = select(func.count()).select_from(
            self.follows.select().subquery())
        return db.session.scalar(query)
    def is_following(self ,user):
        q = self.follows.select().where(Users.id == user.id)
        return db.session.scalar(q)
    def followers_count(self):
        query = select(func.count()).select_from(
            self.followers.select().subquery())
        return db.session.scalar(query)



class Posts(db.Model):
    id:Mapped[int] = mapped_column(primary_key=True)
    body:Mapped[str] = mapped_column(String(130))
    time_Stamp:Mapped[datetime] = mapped_column(index=True,default=lambda:datetime.now(timezone.utc))
    user_id:Mapped[int] = mapped_column(ForeignKey(Users.id),index=True)
    user:Mapped[Users] = relationship(back_populates="posts")




@Login.user_loader          
def load(id):               
    return db.session.get(Users,int(id)) 
                            
