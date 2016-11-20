from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy

import datetime, json, os

from models import db
from models import Container, Manufacturer

app = Flask(__name__)
db.init_app(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DB']

@app.route('/')
def index():
    return "Blackfin API"

@app.route('/manufacturers', methods=['GET'])
def manufacturers():
    manufacturers = Manufacturer.query.order_by(Manufacturer.id)
    
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
    containers = Container.query.filter_by(manufacturer_id=man_id).all()
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

@app.route('/manufacturers/<int:man_id>/billofladings', methods=['GET'])
def getBillsByManufacturer(man_id):
    containers = Container.query.filter_by(manufacturer_id=man_id).distinct(Container.bill_of_lading).all()
    
    if containers is None:
        abort(403)
    
    json_data = []
    for container in containers:
        if container.est_arrival is not None:
            json_data.append({
                'bill_of_lading': container.bill_of_lading,
                'est_arrival': str(container.est_arrival)
            })
    resp = json.dumps(json_data)
    return resp

# Get containers recieved per port per date
@app.route('/containers', methods=['GET'])
def containersPerDay():
    # Get estimated arrival dates
    arr_dates = ['2016-07-01', '2016-07-29', '2016-07-15', '2016-07-22',
            '2016-08-05', '2016-08-12', '2016-07-08']
    
    # Get counts
    counts = {}
    for date in arr_dates:
        counts[date] = Container.query.filter_by(est_arrival=date).count()
    
    resp = jsonify(**counts)
    resp.status_code = 200
    return resp

# Get containers recieved per port per date
@app.route('/port/<port>/containers', methods=['GET'])
def containersPerDayByPort(port):
    # Get estimated arrival dates
    arr_dates = ['2016-07-01', '2016-07-29', '2016-07-15', '2016-07-22',
            '2016-08-05', '2016-08-12', '2016-07-08']
    
    # Get counts
    counts = {}
    for date in arr_dates:
        counts[date] = Container.query.filter_by(est_arrival=date).filter_by(unload_port=port).count()
    
    resp = jsonify(**counts)
    resp.status_code = 200
    return resp

@app.route('/shippingline/<shippingline>/containers', methods=['GET'])
def containersPerDayByLine(shippingline):
    # Get all distinct arrival dates
    arr_dates = ['2016-07-01', '2016-07-29', '2016-07-15', '2016-07-22',
            '2016-08-05', '2016-08-12', '2016-07-08']
    # Count number of containers on each arrival datetime
    counts = {}
    for date in arr_dates:
        counts[date] = Container.query.filter_by(est_arrival=date).filter_by(shipping_line=shippingline).count()

    resp = jsonify(**counts)
    resp.status_code = 200
    return resp


'''
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
'''

if __name__ == "__main__":
    app.run(debug=True)