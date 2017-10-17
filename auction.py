from flask import Flask
from flask_sqlalchemy import SQLAlchemy

Auction = Flask(__name__)
Auction.config.from_pyfile('config.cfg')

db = SQLAlchemy(Auction)


from views import *

if __name__ == '__main__':
    Auction.run()
