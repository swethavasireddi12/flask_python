from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, IntegerField, SelectField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from Employee.models import User

# class to define registeration form

class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! Please try a different username')

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email Address already exists! Please try a different email address')

    username = StringField(label='UserName', validators=[Length(min=2, max=30), DataRequired()])
    FirstName = StringField(label='FirstName', validators=[Length(min=2, max=30), DataRequired()])
    LastName = StringField(label='LastName', validators=[Length(min=2, max=30), DataRequired()])
    Address = StringField(label='Address', validators=[Length(min=2, max=50), DataRequired()])
    DOB=DateField(label='DOB',validators=[DataRequired()])
    PhoneNumber=IntegerField(label='PhoneNumber',validators=[DataRequired()])
    email_address = StringField(label='Email Address', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password', validators=[EqualTo('password1'), DataRequired()])
    #role = StringField(label='Role', validators=[Length(min=2, max=30), DataRequired()])
    role = SelectField(label="Role", choices=[('', 'Select Role'), ('admin', 'Admin'), ('employee', 'Employee')])
    submit = SubmitField(label='Create Account')


#class to define login form

class LoginForm(FlaskForm):
    username = StringField(label='User Name', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    #role = StringField(label='Role', validators=[Length(min=2, max=30), DataRequired()])
    submit = SubmitField(label='Sign in')


#class to  define  search bar

class SearchForm(FlaskForm):
  searched = StringField(label='searched', validators=[Length(min=2,max=30),DataRequired()])
  searching = StringField(label='searching', validators=[Length(min=2, max=30), DataRequired()])
  submit = SubmitField(label='Search')

