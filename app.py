from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy

import datetime, json, os

from models import db
from models import Container, Manufacturer

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DB']
db.init_app(app)

@app.route('/')
def index():
    return "Hello World!"

@app.route('/manufacturers', methods=['GET'])
def manufacturers():
    manufacturers = Manufacturer.query.order_by(Org.id)
    
    json_data = []
    for man in manufacturers:
        json_data.append({
            'id': man.id,
            'name': man.name
        })
    resp = json.dumps(json_data)
    return resp

@app.route('/manufacturers/<int:man_id>/containers', methods=['GET'])
def getManContainers(man_id):
    containers = Container.query.filter_by(manufacturer=man_id).all()
    if containers is None:
        abort(404)
    
    json_data = []
    for container in containers:
        json_data.append({
            'id':container.id,
            'bill_of_lading':container.bill_of_lading,
            'manufacturer':man_id,
            'location':container.location
        })
    resp = json.dumps(json_data)
    return resp


@app.route('/containers/',defaults={'container_id': None})
@app.route('/containers/<int:container_id>', methods=['GET'])
def containers(man_id):
    if man_id is None:
        man = Container.query.filter_by(id = container_id).first()

        if org is None:
            abort(404)

        json_data = {
            'id':org.id,
            'name':man.name
        }
        
        resp = jsonify(**json_data)
        resp.status_code = 200
        return resp
    else:


if __name__ == "__main__":
    app.run(debug=True)