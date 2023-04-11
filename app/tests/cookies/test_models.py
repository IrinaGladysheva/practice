from app.extensions.database import db
from app.orders.models import Works

def test_work_update(client):
  # updates works properties
  work = Works(slug='screaming', name='Screaming Face', price=1.50)
  db.session.add(work)
  db.session.commit()

  work.name = 'Screaming'
  work.save()

  updated_work = Works.query.filter_by(slug='screaming').first()
  assert updated_work.name == 'Screaming'


def test_work_delete(client):
  # deletes cookie
  work = Works(slug='sadness', name='Russian sadness', price=1.50)
  db.session.add(work)
  db.session.commit()

  work.delete()

  deleted_work = Works.query.filter_by(slug='sadness').first()
  assert deleted_work is None

