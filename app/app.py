from flask import Flask
from flask_login import LoginManager
from app.orders.models import User
from app.extensions.database import migrate
from app.extensions.database import db
from app.orders.routes import orders_blueprint

login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')

    app.secret_key = app.config['SECRET_KEY']

    # Initialize LoginManager
    login_manager.init_app(app)
    login_manager.login_view = 'orders.register'

    register_extensions(app)
    register_blueprints(app)

    return app

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def register_blueprints(app: Flask):
    app.register_blueprint(orders_blueprint)

def register_extensions(app: Flask):
    from app.extensions.database import db
    from flask_migrate import Migrate

    db.init_app(app)
    migrate = Migrate(app, db, compare_type=True)
    migrate.init_app(app, db, compare_type=True)
