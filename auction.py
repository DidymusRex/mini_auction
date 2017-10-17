from flask import Flask
from flask_sqlalchemy import SQLAlchemy

auction = Flask(__name__)

db = SQLAlchemy(auction)

auction.config.from_pyfile('config.cfg')

if __name__ == '__main__':
    auction.run()
