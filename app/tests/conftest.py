from flask_migrate import upgrade
from os import environ
import pytest
from app.app import create_app
environ['DATABASE_URL'] = 'sqlite://'

@pytest.fixture
def client():
    app = create_app()
    with app.app_context():
        upgrade()
        yield app.test_client()
