from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length


class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=8, max=80)])
    password = PasswordField('password',  validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField()


class RegisterForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=8, max=80)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    email = StringField('email', validators=[InputRequired(), Email()])
