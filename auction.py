from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import views

Auction = Flask(__name__)
Auction.config.from_pyfile('config.cfg')
db = SQLAlchemy(Auction)


if __name__ == '__main__':
    Auction.run()
