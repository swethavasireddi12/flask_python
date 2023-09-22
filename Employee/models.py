from Employee import db, login_manager
from Employee import bcrypt
from flask_login import UserMixin
from flask_security import RoleMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#class to store the values to database 

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    FirstName = db.Column(db.String(length=30), nullable=False)
    LastName = db.Column(db.String(length=30), nullable=False)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    Address = db.Column(db.String(length=50), nullable=False)
    password_hash = db.Column(db.String(length=60), nullable=False)
    role = db.Column(db.String(80),nullable=False)
    PhoneNumber = db.Column(db.Integer(),nullable=False,unique=True)
    roles = db.relationship('Role', secondary='user_roles')

    def __repr__(self):
        return '<name %r>' %self.id


    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)





class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)

class UserRoles(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('roles.id', ondelete='CASCADE'))















