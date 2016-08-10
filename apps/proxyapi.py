#!/usr/bin/python
# -*- coding: UTF-8 -*-

import dboperation
from flask import Flask, jsonify

app = Flask(__name__)

tasks = dboperation.select()

@app.route('/api/http', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


def run():
    print("Get infomation from http://localhost:5000/api/http")
    app.run(debug=False)

