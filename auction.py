from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_login import LoginManager


Auction = Flask(__name__)
Auction.config.from_pyfile('config.cfg')

"""
Bootstrap needs to be instantiated before SQLAlchemy
"""
Bootstrap(Auction)
db = SQLAlchemy(Auction)
admin = Admin(Auction, template_mode='bootstrap3')

"""
Semi-circular imports needed because of internal dependencies, Users has to be imported after db is instantiated
"""
from views import *
from model import Users

login_manager = LoginManager(Auction)


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


if __name__ == '__main__':
    Auction.run()
