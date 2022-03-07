from flask import Flask, jsonify, request
import json
import os
from flask_pymongo import PyMongo
# from ms2query import run_ms2query
# from utils import csv2json

app = Flask(__name__)

mongodb_client = PyMongo(app, uri=os.environ['MONGODB_URI_STRING'])
db = mongodb_client.db

@app.route('/ping')
def pong():
    return "pong"

@app.route('/create_ms2query_result', methods=['GET', 'POST'])
def createMs2QueryResult():
    data = request.get_json(force=True)
    db.ms2query_results.insert_one(data)

    return jsonify(
        status=True,
        message='Ms2query result saved successfully!'
    ), 201

@app.route('/get_ms2query_results', methods=['GET'])
def getMs2QueryResults():
    _ms2query_results = db.ms2query_results.find()

    item = {}
    data = []
    for result in _ms2query_results:
        item = {
            'id': str(result['_id']),
            'timestamp': result['timestamp'],
            'results': result['results']
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