from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField

class LoginForm(FlaskForm):
  username = StringField('username')
  password = PasswordField('password')

