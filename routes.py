from wtforms.validators import url
from main import app,db
from models import Users
from flask import render_template,redirect, url_for
from fields import Login
from flask_login import current_user,login_user,logout_user
import sqlalchemy as sql

@app.route("/",methods=["post","get"])
def login():
     form = Login()
     if current_user.is_authenticated:
          print("authed bro")
          return redirect(url_for("where"))
     if form.validate_on_submit():
          user = db.session.scalar(sql.select(Users).where(Users.username==form.username.data))
          if user is None or not user.check_hash(form.password.data):
               print("error")
               return redirect(url_for("login"))
          login_user(user,remember=form.state.data)
          print("sucess")
          return redirect(url_for("where"))
     print("main")
     return render_template("index.html",login=form)

@app.route("/where")
def where():
     return render_template("test.html")

@app.route("/ou")
def logout():
     logout_user()
     return redirect(url_for("login"))

