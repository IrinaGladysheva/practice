from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

#from app.extensions.database import db

db = SQLAlchemy()
migrate = Migrate()

class CRUDMixin():
  def save(self):
    db.session.add(self)
    db.session.commit()
    return self

  def delete(self):
    db.session.delete(self)
    db.session.commit()
    return
