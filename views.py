from auction import Auction, db
from forms import LoginUserForm, CreateUserForm
from flask import render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from model import Users


@Auction.route('/')
def index():
    return redirect(url_for('login'))


@Auction.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginUserForm()

    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('dashboard'))

    return render_template('login.html', form=form)


@Auction.route('/logout')
@login_required
def logout():
    flash(current_user.username + ' is logged out')
    logout_user()
    return redirect(url_for('login'))


@Auction.route('/register', methods=['GET', 'POST'])
def create_user():
    form = CreateUserForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = Users(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash('You may now log in as ' + new_user.usename)
        return redirect(url_for('login'))
        # return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'

    flash('Registration error, please try again')
    return render_template('register.html', form=form)


@Auction.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')


## GLOBAL
# Admin (organization)
# Manage Users and Roles
# Manage Auctions

## By Auction
## Pre
# Manage Donors (bulk copy)
# Manage Customers (bulk copy)
# Manage Donations (items)
# Manage Tables (Names, item assignments)
# Bid sheets

## Active
# Check-in Customer
# Check-out Customer
# Manage Bids
# Open/Close Tables

## Post
# Close Auction
# Bill unpaid Customers

## Reports
