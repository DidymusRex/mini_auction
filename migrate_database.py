from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from auction import Auction, db
"""
run init once
python model.py db init

after each DDL change do ...
python model.py db migrate
python model.py db upgrade
"""

migrate = Migrate(Auction, db)
manager = Manager(Auction)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
