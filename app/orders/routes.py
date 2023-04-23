from flask import Blueprint, render_template, request, flash, redirect, url_for, session, abort
from app.extensions.database import db
from app.orders.models import Order, Address, Works, User
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from flask_login import login_required, current_user

orders_blueprint = Blueprint('orders', __name__)

def register_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated:
            return f(*args, **kwargs)
        else:
            flash('You need to be registered to access this page.', category='error')
            return redirect(url_for('orders.register'))
    return decorated_function

@orders_blueprint.route('/')
def homework():
    return render_template('homework.html')

@orders_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 3:
            flash('Email must be greater than 3 characters', category='error')
        elif len(username) < 1:
            flash('First name must be greater than 1 character', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password much be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, user_name=username, password=generate_password_hash(password1, method='sha256'))
            flash('Account created!', category='success')
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('about'))

    return render_template('register.html')

@orders_blueprint.route('/about', methods=['GET', 'POST'])
@register_required
def about():
    if request.method == 'POST':
        name = request.form['title']
        description = request.form['description']
        price = request.form['price']
        from time import time
        slug = f"{name}-{int(time())}"
        new_work = Works(slug=slug, name=name, description=description, price=price)
        new_work.save()
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