from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy

import datetime, json, os

app = Flask(__name__)
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SQLALCHEMY_DATABASE_URI'] = ''
#db = SQLAlchemy(app)

@app.route('/')
def index():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("3000"), debug=True)