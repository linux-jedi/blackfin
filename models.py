from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Manufacturer(db.Models):
    __tablename__ = "manufacturers"
    id = db.Column(db.Integer, primary_key=True)
    name = Column(db.String(50), unique=True)
    containers = db.relationship('Container', backref='manufacturer',
                                lazy='dynamic')


class Container(db.Models):
    __tablename__ = "containers"

    id = db.Column(db.String(30), primary_key=True)
    bill_of_lading = db.Column(db.String(30), unique=True)
    location = db.Columb(db.String(50))
    manufacturer = db.Column(db.Integer, db.ForeignKey("manufacturer.id"))
