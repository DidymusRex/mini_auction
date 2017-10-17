from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_pyfile('config.cfg')

# Bootstrap needs to come before SQLAlchemy
Bootstrap(app)
db = SQLAlchemy(app)

from views import *

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login_user'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


if __name__ == '__main__':
    app.run()
