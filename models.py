from main import db
from sqlalchemy import String
from sqlalchemy.orm import relationship,Mapped,mapped_column,WriteOnlyMapped


class Users(db.Model):
    id:Mapped[int] = mapped_column(primary_key=True)
    username:Mapped[str] = mapped_column(String(50),index=True,unique=True)
    email:Mapped[str] = mapped_column(String(60),index=True,unique=True)
    password:Mapped[str]=mapped_column(String(256))

