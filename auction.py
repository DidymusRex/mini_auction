from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

Auction = Flask(__name__)

Auction.config.from_pyfile('config.cfg')

db = SQLAlchemy(Auction)

import views

if __name__ == '__main__':
    Auction.run()
