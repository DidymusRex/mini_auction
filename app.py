from flask import Flask, render_template, redirect, url_for
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_bootstrap import Bootstrap
from flask_user import UserManager, UserMixin, SQLAlchemyAdapter, login_required
from flask_sqlalchemy import SQLAlchemy

"""
Build the app
"""
app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/auction/mini_auction/db/Auction.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'Wee1nYiVbRa6gHNevSex0cOeLaiR7bOg'
app.config['CSRF_ENABLED'] = True
app.config['USER_ENABLE_EMAIL'] = True

"""
define the database model
"""
db = SQLAlchemy(app)


class Organization(db.Model):
    """
    Organization information - single row
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    address1 = db.Column(db.String(255))
    address2 = db.Column(db.String(255))
    city = db.Column(db.String(255))
    state = db.Column(db.String(255))
    postal_code = db.Column(db.String(255))
    telephone = db.Column(db.String(255))
    email_address = db.Column(db.String(255))
    logo_image = db.column(db.Integer)


class Event(db.Model):
    """
    A record for each auction event (day)
    """
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255))
    date = db.Column(db.Integer)
    status = db.Column(db.Integer)
    auctions = db.relationship('Auction', backref='event', lazy=True)


class Auction(db.Model):
    """
    Smaller units of auction (i.e. individual silent auctions and live auctions)
    """
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))
    status = db.Column(db.Integer)
    type = db.Column(db.Integer)
    name = db.Column(db.String(255))
    picture_id = db.Column(db.Integer)


class Item(db.Model):
    """
    List of items for auction
    """
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer)
    auction_id = db.Column(db.Integer)
    donor_id = db.Column(db.Integer)
    last_bid_id = db.Column(db.Integer)
    description = db.Column(db.String(255))
    value = db.column(db.Float)
    price = db.column(db.Float)
    reserve = db.Column(db.Float)
    is_sold = db.Column(db.Boolean)


class Picture(db.Model):
    """
    Images should be in the static directory
    """
    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(255))
    thumb_name = db.Column(db.String(255))


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    title = db.Column(db.String(255))
    address1 = db.Column(db.String(255))
    address2 = db.Column(db.String(255))
    city = db.Column(db.String(255))
    state = db.Column(db.String(255))
    postal_code = db.Column(db.String(255))
    telephone = db.Column(db.String(255))
    telephone_ext = db.Column(db.String(255))
    email_address = db.Column(db.String(255))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    title = db.Column(db.String(255))
    address1 = db.Column(db.String(255))
    address2 = db.Column(db.String(255))
    city = db.Column(db.String(255))
    state = db.Column(db.String(255))
    postal_code = db.Column(db.String(255))
    telephone = db.Column(db.String(255))
    telephone_ext = db.Column(db.String(255))
    email_address = db.Column(db.String(255))
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean(), nullable=False, server_default='0')


class Donor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    title = db.Column(db.String(255))
    address1 = db.Column(db.String(255))
    address2 = db.Column(db.String(255))
    city = db.Column(db.String(255))
    state = db.Column(db.String(255))
    postal_code = db.Column(db.String(255))
    telephone = db.Column(db.String(255))
    telephone_ext = db.Column(db.String(255))
    email_address = db.Column(db.String(255))
    is_business = db.Column(db.Boolean)
    is_prospect = db.Column(db.Boolean)
    is_donor = db.Column(db.Boolean)
    business_name = db.Column(db.String(255))


class Bidder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    title = db.Column(db.String(255))
    address1 = db.Column(db.String(255))
    address2 = db.Column(db.String(255))
    city = db.Column(db.String(255))
    state = db.Column(db.String(255))
    postal_code = db.Column(db.String(255))
    telephone = db.Column(db.String(255))
    telephone_ext = db.Column(db.String(255))
    email_address = db.Column(db.String(255))
    balance_due = db.Column(db.Float)


class Volunteer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    title = db.Column(db.String(255))
    address1 = db.Column(db.String(255))
    address2 = db.Column(db.String(255))
    city = db.Column(db.String(255))
    state = db.Column(db.String(255))
    postal_code = db.Column(db.String(255))
    telephone = db.Column(db.String(255))
    telephone_ext = db.Column(db.String(255))
    email_address = db.Column(db.String(255))
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))


"""
build the rest of the app infrastructure
"""
Bootstrap(app)
"""
User management
"""
db_adapter = SQLAlchemyAdapter(db, User)
user_manager = UserManager(db_adapter, app)
"""
Admin pages
"""
admin = Admin(app, template_mode='bootstrap3')


class UserView(ModelView):
    create_modal = True


class OrgView(ModelView):
    create_modal = True


class AuctionView(ModelView):
    create_modal = True


admin.add_view(UserView(User, db.session))
admin.add_view(OrgView(Organization, db.session))
admin.add_view(AuctionView(Auction, db.session))

"""
build the routes
"""


@app.route('/')
def index():
    return redirect(url_for('user.login'))


@app.route('/dashboard')
@login_required
def dashboard():
    """
    Entry point to the application
    """
    return render_template('dashboard.html')


if __name__ == '__main__':
    app.run()
