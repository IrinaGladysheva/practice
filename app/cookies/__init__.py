from flask import Blueprint

cookies_blueprint = Blueprint('cookies', __name__)

def register_blueprints(app):
    app.register_blueprint(cookies_blueprint)
