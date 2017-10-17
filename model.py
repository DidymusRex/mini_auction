from auction import db

class Organization(db.Model):
    id = db.Column(db.Integer, primarykey = True)
    name = db.Column(db.String(255))
    address1 = db.Column(db.String(255))
    address2 = db.Column(db.String(255))
    city = db.Column(db.String(255))
    state = db.Column(db.String(255))
    postal_code = db.Column(db.String(255))
    telephone = db.Column(db.String(255))
    email_address = db.Column(db.String(255))
    slogan =db.Column(db.String(255))
    auction_date = db.Column(db.DateTime)
    next_auction_date = db.Column(db.DateTime)
    logo_image = dn.column(db.Integer)


class Items(db.Model):
    id = db.Column(db.Integer, primarykey = True)
    donor_id = db.Column(db.Integer)
    product = db.Column(db.String(255))
    value = db.column(db.Float)
    theme = db.Column(db.String(255))
    auction_id = db.Column(db.Integer)
    theme_id = db.Column(db.Integer)


class Customer(db.Model)
    id = db.Column(db.Integer, primarykey = True)
    paddle = db.Column(db.Integer)
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


class Donors(db.Model)
    id = db.Column(db.Integer, primarykey = True)
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


class Theme(db.Model):
    id = db.Column(db.Integer, primarykey = True)
    name = db.Column(db.String(255))
    picture_id = db.Column(db.Integer)


class Pictures(db.Model):
    id = db.Column(db.Integer, primarykey = True)
    file_name = db.Column(db.String(255))
    thumbnail_name = db.Column(db.String(255))