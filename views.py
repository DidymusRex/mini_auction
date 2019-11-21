from auction import Auction, db
from flask import redirect, render_template, url_for
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_bootstrap import Bootstrap
from flask_user import UserManager, login_required
from model import User

Bootstrap(Auction)
admin = Admin(Auction, template_mode='bootstrap3')
user_manager = UserManager(Auction, db, User)
admin.add_view(ModelView(User, db.session))


@Auction.route('/dashboard')
@login_required
def dashboard():
    """
    Entry point to the application
    """
    return render_template('dashboard.html')
