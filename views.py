from auction import Auction, db, admin
from forms import LoginUserForm, CreateUserForm
from flask import render_template, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from flask_admin.contrib.sqla import ModelView
from model import Users
from sqlalchemy import or_
from werkzeug.security import generate_password_hash, check_password_hash


admin.add_view(ModelView(Users, db.session))


@Auction.route('/')
def index():
    """
    Root redirects to login
    """
    return redirect(url_for('user/sign-in'))


@Auction.route('/register', methods=['GET', 'POST'])
def create_user():
    """
    Create a new user and send them to the login page
    """
    form = CreateUserForm()

    if form.validate_on_submit():
        user = Users.query.filter(or_(Users.username == form.username.data, Users.email == form.email.data)).first()
        if user:
            flash('Username or Email already exists')
        else:
            hashed_password = generate_password_hash(form.password.data, method='sha256')
            new_user = Users(username=form.username.data, email=form.email.data, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()

            flash('You may now log in as ' + new_user.username)
            return redirect(url_for('login'))

    return render_template('register.html', form=form)


@Auction.route('/dashboard')
@login_required
def dashboard():
    """
    Entry point to the application
    """
    return render_template('dashboard.html')


"""
To Do List:

Global
----------
Admin (organization)
Manage Users and Roles
Manage Auctions

By Auction
----------
Pre-auction
Manage Donors (bulk copy)
Manage Customers (bulk copy)
Manage Donations (items)
Manage Tables (Names, item assignments)
Bid sheets

Active auction
Check-in Customer
Check-out Customer
Manage Bids
Open/Close Tables

Post auction
Close Auction
Bill unpaid Customers

Reports
Bid sheets
Invoices
Closing reports
Letters
"""