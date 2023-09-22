from Employee import app,api
from flask import render_template, redirect, url_for, flash,session,request,abort,make_response
from Employee.models import User
from Employee.forms import RegisterForm, LoginForm,SearchForm
from Employee import db
from flask_login import login_user,logout_user,login_required,current_user,LoginManager
from flask_restful import Api, Resource, reqparse, marshal_with, fields
from flask_principal import Principal, Permission, RoleNeed
from functools import wraps
from sqlalchemy.orm import Query


# route for home page
@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


#route for market page
@app.route('/market')
#@access_required(role="Admin")
@login_required
def market_page():
    form=SearchForm()
    users= User.query.all()
    return render_template('market.html', users=users, form=form)


#route for registration page
@app.route('/register', methods=['GET', 'POST'])
def register_page():
    users = User.query.all()
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,FirstName=form.FirstName.data,LastName=form.LastName.data,
                              email_address=form.email_address.data,Address =form.Address.data,
                              password=form.password1.data,role=form.role.data,PhoneNumber=form.PhoneNumber.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f"Account created successfully! You are now logged in as {user_to_create.username}", category='success')
        return redirect(url_for('employee_page'))
        
    if form.errors != {}: #If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')

    return render_template('register.html', form=form,users=users)


#routes for the login page
@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
                attempted_password=form.password.data
        ):
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
            return redirect(url_for('employee_page'))
        else:
            flash('Username and password are not match! Please try again', category='danger')
    return render_template('login.html', form=form)


#route to logout page
@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for("home_page"))


#route for employee page
@app.route('/employee')
@login_required
def employee_page():
    return render_template('details.html')


#restful microservice operation like get,postand delete
First_post_args=reqparse.RequestParser()
First_post_args.add_argument("FirstName",type=str,help='firstname is required',required=True)
First_post_args.add_argument("Address",type=str,help='Address is required',required=True)

First_put_args=reqparse.RequestParser()
First_put_args.add_argument("FirstName",type=str)
First_put_args.add_argument("Address",type=str)

resource_feilds={
    'id':fields.Integer,
    'FirstName':fields.String,
    'Address':fields.String,
}
class ToDoList(Resource):
    def get(self):
        tasks=User.query.all()
        todos={}
        for FirstName in tasks:
            todos[FirstName.id]={"FirstName":FirstName.FirstName,"Address":FirstName.Address}
        return todos

class ToDo(Resource):
    @marshal_with(resource_feilds)
    def get(self,todo_id):
        FirstName=User.query.filter_by(id=todo_id).first()
        #results = User.query.filter(User.FirstName.like('%' + search_term + '%')).all()
        return todo_id

    @marshal_with(resource_feilds)
    def post(self,todo_id):
        args=First_post_args.parse_args()
        FirstName=User.query.filter_by(id=todo_id).first()

        if FirstName:
            abort(409,'firstname already exists')
        todo=User(id=todo_id,FirstName=args['FirstName'],Address=args['Address'])
        db.session.add(todo)
        db.session.commit()
        return todo,201

    @marshal_with(resource_feilds)
    def put(self,todo_id):
        args=First_put_args.parse_args()
        FirstName=User.query.filter_by(id=todo_id).first()
        if not FirstName:
            abort(404,message="task doesnot exist,cannot update")
        if args['FirstName']:
            FirstName.Firstname=args['FirstName']
        if args['Address']:
            FirstName.Address=args['Address']
        return FirstName

    def delete(self,todo_id):
        FirstName=User.query.filter_by(id=todo_id).first()
        db.session.delete(FirstName)
        return 'deleted',204



api.add_resource(ToDo,'/todos/<int:todo_id>')
#api.add_resource(ToDo,'/todos/<string:search_term>')
api.add_resource(ToDoList,'/todos')
#api.add_resource((ToDo,'/market.html/search/<search_term>'))



@app.context_processor
def base():
    form=SearchForm
    return dict(form=form)

#route for search form
@app.route('/search',methods=['GET','POST'])
def search_page():
    global post
    form = SearchForm()
    posts=User.query
    if form.validate_on_submit():
        posts=posts.filter(User.FirstName.like('%'+form.searched.data+'%' ))
        post = posts.filter(User.Address.like('%' + form.searching.data + '%'))
        posts = posts.order_by(User.username).all()
        return render_template("Search.html", form=form,posts=posts,post=post)
    else:
        abort(404,"FirstName doesnot exist")

    return render_template("Search.html",form=form,posts=posts,post=post)










