from app.app import create_app
from app.extensions.database import db
from app.orders.models import Works

if __name__ == '__main__':
  app = create_app()
  app.app_context().push()

works_data = {
    'screaming' : {'name': 'Screaming Face', 'price': 1.50},
    'sadness' : {'name': 'Russian sadness', 'price': 1.00},
    'mind' : {'name': 'Trapped inside my mind', 'price': 0.75},
    'loving' : {'name': 'Loving', 'price': 0.50},
  }

for slug, works in works_data.items():
    new_work = Works(slug=slug, name=works['name'], price=works['price'])
    db.session.add(new_work)

db.session.commit()

class CRUDMixin():
    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return self

