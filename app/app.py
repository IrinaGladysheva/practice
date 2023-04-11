from flask import Flask
from app.extensions.database import migrate
from app.extensions.database import db
from app.orders.routes import orders_blueprint
#from app.cookies.routes import cookies_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')

    register_extensions(app)
    register_blueprints(app)

    return app


def register_blueprints(app: Flask):
    app.register_blueprint(orders_blueprint)
 #   app.register_blueprint(cookies_blueprint)

def register_extensions(app: Flask):
    from app.extensions.database import db
    from flask_migrate import Migrate

    db.init_app(app)
    migrate = Migrate(app, db, compare_type=True)
    migrate.init_app(app, db, compare_type=True)
