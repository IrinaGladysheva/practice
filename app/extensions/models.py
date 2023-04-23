from app.extensions.database import db

#class User(db.Model):
 #   id = db.Column(db.Integer, primary_key=True)
 #  name = db.Column(db.String(128))

class CRUDMixin():
    def save(self):
        db.session.add(self)
        db.session.commit()
        return self
