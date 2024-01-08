from main import app,db
from models import Users
from flask import render_template,redirect, url_for
from fields import Login,Register
from flask_login import current_user,login_user,logout_user,login_required
import sqlalchemy as sql
from sqlalchemy import or_
from models import Users
from flask import request
from urllib.parse import urlsplit


@app.route("/")
def index():
     return render_template("test.html")


@app.route("/login",methods=["post","get"])
def login():
    form = Login()
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if form.validate_on_submit(): 
        print("Post")
        user = db.session.scalar(
            sql.select(Users).where(
                or_(
                    Users.username == form.username.data,
                    Users.email == form.username.data)))
        print(user)
        if user is None or not user.check_hash(form.password.data):
            return redirect(url_for('login'))
        login_user(user, remember=form.state.data)
        next_page = request.args.get('next')
        print(next_page)
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('user',user_name=current_user.username)
        return redirect(next_page)    
    return render_template('login.html', login=form)
          
#    print(Users)
#     return render_template("index.html",login=form)
@app.route("/register",methods=['get','post'])
def register():
    form = Register()
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if form.validate_on_submit():
        user = Users(username=form.username.data,email=form.email.data)
        user.generate_hash(form.pass1.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("register.html",form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))

@app.route('/user/<user_name>', methods=['GET'])
@login_required
def user(user_name):
    return str(current_user.username)

