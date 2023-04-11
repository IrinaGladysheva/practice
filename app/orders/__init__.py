from flask import Blueprint

orders_blueprint = Blueprint('orders', __name__)

from . import routes

def register_blueprints(app):
    app.register_blueprint(orders_blueprint)
