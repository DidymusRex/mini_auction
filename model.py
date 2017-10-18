from auction import db
from flask_login import UserMixin


class Users(UserMixin, db.Model):
    """
    Administrative users
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))


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


class Auctions(db.Model):
    """
    A record for each auction event (day)
    """
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255))
    date = db.Column(db.Integer)
    status = db.Column(db.Integer)


class Items(db.Model):
    """
    List of items for auction
    """
    id = db.Column(db.Integer, primary_key=True)
    auction_id = db.Column(db.Integer)
    donor_id = db.Column(db.Integer)
    description = db.Column(db.String(255))
    value = db.column(db.Float)
    price = db.column(db.Float)
    reserve = db.Column(db.Float)
    table_id = db.Column(db.Integer)
    is_sold = db.Column(db.Boolean)
    sold_for = db.Column(db.Float)


class Customers(db.Model):
    """
    AKA bidders
    """
    id = db.Column(db.Integer, primary_key=True)
    auction_id = db.Column(db.Integer)
    last_name = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    title = db.Column(db.String(255))
    address1 = db.Column(db.String(255))
    address2 = db.Column(db.String(255))
    city = db.Column(db.String(255))
    state = db.Column(db.String(255))
    postal_code = db.Column(db.String(255))
    telephone = db.Column(db.String(255))
    email_address = db.Column(db.String(255))
    hidden = db.Column(db.Boolean)
    paid_amount = db.column(db.Float)
    balance = db.column(db.Float)


class Donors(db.Model):
    """
    Donor and donor prospect list
    """
    id = db.Column(db.Integer, primary_key=True)
    auction_id = db.Column(db.Integer)
    business = db.Column(db.Boolean)
    company_name = db.Column(db.String(255))
    contact_last_name = db.Column(db.String(255))
    contact_first_name = db.Column(db.String(255))
    contact_title = db.Column(db.String(255))
    address1 = db.Column(db.String(255))
    address2 = db.Column(db.String(255))
    city = db.Column(db.String(255))
    state = db.Column(db.String(255))
    postal_code = db.Column(db.String(255))
    telephone = db.Column(db.String(255))
    telephone_ext = db.Column(db.String(255))
    email_address = db.Column(db.String(255))
    contacted_date = db.Column(db.DateTime)
    donated = db.Column(db.Boolean)
    donated_date = db.Column(db.DateTime)
    no_call_reason = db.Column(db.String(255))
    # donated_item = many-to-one relation


class Tables(db.Model):
    """
    Smaller units of auction (i.e. individual silent auctions and live auctions)
    """
    id = db.Column(db.Integer, primary_key=True)
    auction_id = db.Column(db.Integer)
    status = db.Column(db.Integer)
    type = db.Column(db.Integer)
    name = db.Column(db.String(255))
    picture_id = db.Column(db.Integer)


class Pictures(db.Model):
    """
    Images should be in the static directory
    """
    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(255))
    thumb_name = db.Column(db.String(255))
