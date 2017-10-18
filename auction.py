from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


Auction = Flask(__name__)
Auction.config.from_pyfile('config.cfg')

# Bootstrap needs to come before SQLAlchemy
Bootstrap(Auction)
db = SQLAlchemy(Auction)

from views import *
from model import Users

login_manager = LoginManager()
login_manager.init_app(Auction)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


if __name__ == '__main__':
    Auction.run()
