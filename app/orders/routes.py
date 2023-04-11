from flask import Blueprint, render_template
from app.extensions.database import db
from app.orders.models import Order, Address, Works

orders_blueprint = Blueprint('orders', __name__)

from app.orders import models

@orders_blueprint.route('/')
def homework():
  return render_template('homework.html')

@orders_blueprint.route('/about')
def about():
#  works = ["Screaming Face", "Russian sadness", "Trapped inside my mind", "Loving"]
  works = Works.query.all()
  return render_template('About.html', works=works)

@orders_blueprint.route('/all_works')
def all_works():
  all_works = Works.query.all()
  return render_template('Works.html', works=all_works)

@orders_blueprint.route('/works/<slug>')
def works(slug):
  works = Works.query.filter_by(slug=slug).first()
  return render_template('show.html', works=works)

