from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager


Auction = Flask('auction')
Auction.config.from_pyfile('config.cfg')

db = SQLAlchemy(Auction)

from views import *

Bootstrap(Auction)
login_manager = LoginManager()
login_manager.init_app(Auction)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


if __name__ == '__main__':
    Auction.run()
