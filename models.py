from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Manufacturer(db.Model):
    __tablename__ = "manufacturers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    containers = db.relationship('Container', backref='manufacturer',
                                lazy='dynamic')

class Container(db.Model):
    __tablename__ = "containers"

    id = db.Column(db.String(30), primary_key=True)
    bill_of_lading = db.Column(db.String(30), unique=True)
    location = db.Column(db.String(50))
    manufacturer_id = db.Column(db.Integer, db.ForeignKey("manufacturers.id"))
