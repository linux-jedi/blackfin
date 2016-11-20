from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy

import datetime, json, os

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DB']
db = SQLAlchemy(app)

@app.route('/')
def index():
    return str(os.environ['DB'])

if __name__ == "__main__":
    app.run(debug=True)