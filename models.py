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
    container_size = db.Column(db.Integer)
    location = db.Column(db.String(50))
    manufacturer_id = db.Column(db.Integer, db.ForeignKey("manufacturers.id"))
    vessel_name = db.Column(db.String(50))
    operation_type = db.Column(db.String(50))
    cargo_type = db.Column(db.String(50))
    shipping_line = db.Column(db.String(50))
    load_port = db.Column(db.String(50))
    unload_port = db.Column(db.String(50))
    is_local = db.Column(db.String(50))
    inland_point = db.Column(db.String(50))
    agent_voyage_num = db.Column(db.String(50))
    arriving_term = db.Column(db.String(50))
    est_arrival = db.Column(db.DateTime)
    cargo_cutoff = db.Column(db.DateTime)
    est_departure = db.Column(db.DateTime)
    exp_availability = db.Column(db.DateTime)
    mode_of_entry = db.Column(db.String(20))
    mode_of_exit = db.Column(db.String(20))
    
