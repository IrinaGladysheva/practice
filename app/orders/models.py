from app.extensions.database import db, CRUDMixin
from datetime import datetime
from flask_login import UserMixin


class Works(db.Model, CRUDMixin):
  __tablename__ = 'works'
  id = db.Column(db.Integer, primary_key=True, unique=True)
  slug = db.Column(db.String(80))
  name = db.Column(db.String(80))
  description = db.Column(db.String(200))
  price = db.Column(db.Numeric(10, 2))
  user_id = db.Column(db.Integer, db.ForeignKey('user.id', name='fk_user_id'))


class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True, unique=True)
  email = db.Column(db.String(150), unique=True)
  username = db.Column(db.String(150))
  password = db.Column(db.String(150))
  works = db.relationship('Works', backref=db.backref('user', lazy=True))


class Order(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  address = db.relationship('Address', backref='order', uselist=False, lazy=True)

class Address(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80))
  street = db.Column(db.String(80))
  city = db.Column(db.String(80))
  state = db.Column(db.String(80))
  zip = db.Column(db.String(80))
  country = db.Column(db.String(80))
  order_id = db.Column(db.Integer, db.ForeignKey('order.id'))