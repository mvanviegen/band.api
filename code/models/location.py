import psycopg2
from db import db
class LocationModel(db.Model):
    __tablename__ = 'locations'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80))

    def __init__(self,name):
        self.name = name
    @classmethod
    def find_by_name(cls,name):
        return LocationModel.query.filter_by(name=name).first()
    def find_by_id(_id):
        return LocationModel.query.filter_by(id=_id).first()
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
