
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy




from flask_bcrypt import Bcrypt
from flask_login import LoginManager
app = Flask(__name__)

api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employee.db'
app.config['SECRET_KEY']='b9ee72255e3efa49ff127170'
db = SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager =LoginManager(app)
login_manager.login_view="login_page"
login_manager.login_message_category="info"
from Employee import routes



