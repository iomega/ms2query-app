from flask import Flask, jsonify, request
import json
import os
from flask_pymongo import PyMongo
# from pymongo import MongoClient
# from ms2query import run_ms2query
# from utils import csv2json

app = Flask(__name__)

# app.config["MONGO_URI"] = 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + os.environ['MONGODB_PASSWORD'] + '@' + os.environ['MONGODB_HOSTNAME'] + ':27017/' + os.environ['MONGODB_DATABASE']
# app.config["MONGO_URI"] = os.environ['MONGODB_URI_STRING']
# client = MongoClient('mongodb://mongodb:27017/')
mongodb_client = PyMongo(app, uri=os.environ['MONGODB_URI_STRING'])
db = mongodb_client.db

@app.route('/ping')
def pong():
    return "pong"

@app.route('/create_todo', methods=['GET', 'POST'])
def createTodo():
    # data = request.get_json(force=True)
    db.todos.insert_one({'title': "todo title"})

    return jsonify(
        status=True,
        message='To-do saved successfully!'
    ), 201

@app.route('/get_todos', methods=['GET', 'POST'])
def getTodos():
    # data = request.get_json(force=True)
    _todos = db.todos.find()

    item = {}
    data = []
    for todo in _todos:
        item = {
            'id': str(todo['_id']),
            'title': todo['title']
        }
        data.append(item)

    return jsonify(
        status=True,
        data=data
    )

# @app.route('/run_ms2query')
# def ms2query():
#     response = run_ms2query()
#     return response

# @app.route('/get_results/<filename>')
# def results(filename):
#     file = csv2json(r'./ms2_spectra/results/library_search/'+filename+'.csv', r'./ms2_spectra/results/library_search/'+filename+'.json')
#     return file

# if __name__ == '__main__':
#     app.run(host="0.0.0.0", port=5000)