from auction import app
from forms import LoginUserForm, RegisterUserForm
from flask import render_template, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from model import Users

@app.route('/')
def index():
    return '<h1>index</h1>'


@app.route('/login_user', methods=['GET', 'POST'])
def login():
    form = LoginUserForm()

    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('index'))

        return '<h1>Invalid username or password</h1>'
        # return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'

    return render_template('login.html', form=form)


@app.route('/logout_user')
@login_required
def logout():
    logout_user()
    redirect(url_for('login_user'))


@app.route('/register_user', methods=['GET', 'POST'])
def register_user():
    form = RegisterUserForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = Users(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return '<h1>New user has been created!</h1>'
        # return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'

    return render_template('register_user.html', form=form)


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
