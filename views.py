from auction import Auction, db
from flask import redirect, render_template, url_for
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_bootstrap import Bootstrap
from flask_user import UserManager, SQLAlchemyAdapter, login_required
from model import User

Bootstrap(Auction)
admin = Admin(Auction, template_mode='bootstrap3')
db_adapter = SQLAlchemyAdapter(db, User)
user_manager = UserManager(db_adapter, Auction)
admin.add_view(ModelView(User, db.session))


@Auction.route('/dashboard')
@login_required
def dashboard():
    """
    Entry point to the application
    """
    return render_template('dashboard.html')
