import os
import datetime
import utils
import csv
import json
from bson.objectid import ObjectId
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from ms2query.run_ms2query import default_library_file_base_names, run_complete_folder
from ms2query.ms2library import create_library_object_from_one_dir

# init flask app
app = Flask(__name__)

# init mongodb <-> flask connection
mongodb_client = PyMongo(app, uri=os.environ['MONGODB_URI_STRING'])
db = mongodb_client.db

# api endpoints
@app.route('/ping')
def pong():
    return "pong"

@app.route('/get_ms2query_results', methods=['GET'])
def getMs2QueryResults():
    _ms2query_results = db.ms2query_results.find()

    item = {}
    data = []
    for result in _ms2query_results:
        item = {
            '_id': str(result['_id']),
            'timestamp': result['timestamp'],
            'results': result['results'],
            'filename': result['filename']
        }
        data.append(item)

    return jsonify(
        status=True,
        data=data
    )

@app.route('/run_ms2query', methods=['GET', 'POST'])
def runMs2Query():
    run_ms2query()
    return jsonify(
        status=True,
        message='Ms2query result saved successfully!'
    ), 201
    
@app.route('/ms2query_to_database', methods=['GET', 'POST'])
def ms2queryToDatabase():
    ms2query_to_database()
    return jsonify(
        status=True,
        message='Results folder successfully removed!'
    ), 201

@app.route('/delete_ms2query_result/<id>', methods=['GET', 'POST'])
def deleteMs2QueryResult(id):
    db.ms2query_results.delete_one({"_id": ObjectId(id)})
    return jsonify(
        status=True,
        message='Ms2query result deleted!'
    ), 201

@app.route('/find_ms2query_result/<id>', methods=['GET', 'POST'])
def findMs2QueryResult(id):
    _ms2query_results = db.ms2query_results.find({"_id": ObjectId(id)})

    item = {}
    data = []
    for result in _ms2query_results:
        item = {
            'id': str(result['_id']),
            'timestamp': result['timestamp'],
            'results': result['results'],
            'filename': result['filename']
        }
        data.append(item)

    return jsonify(
        status=True,
        data=data
    )

# if __name__ == '__main__':
#     app.run(host="0.0.0.0", port=5000)

def run_ms2query():
    # Set the location where all your downloaded model files are stored
    ms2query_library_files_directory = "./ms2query_library_files"
    # define the folder in which your query spectra are stored.
    # Accepted formats are: "mzML", "json", "mgf", "msp", "mzxml", "usi" or a pickled matchms object. 
    ms2_spectra_directory = "./ms2_spectra"

    # Create a MS2Library object 
    ms2library = create_library_object_from_one_dir(ms2query_library_files_directory, default_library_file_base_names())

    folder_to_store_results = os.path.join(ms2_spectra_directory, "results")

    # Run library search and analog search on your files. 
    # The results are stored in the specified folder_to_store_results.
    run_complete_folder(ms2library, ms2_spectra_directory, folder_to_store_results)

    return "ms2query DONE"

def ms2query_to_database():
    filename = os.listdir('./ms2_spectra/results/analog_search')[0]

    json_array_analog_search = []
    with open(r'./ms2_spectra/results/analog_search/'+filename, encoding='utf-8') as csvf: 
        csv_reader = csv.DictReader(csvf) 

        for row in csv_reader: 
            json_array_analog_search.append(row)

    json_array_library_search = []
    with open(r'./ms2_spectra/results/library_search/'+filename, encoding='utf-8') as csvf: 
        csv_reader = csv.DictReader(csvf) 

        for row in csv_reader: 
            json_array_library_search.append(row)
    
    db.ms2query_results.insert_one({
        "timestamp": datetime.datetime.now(),
        "filename": filename,
        "results": {
            "analog_search": json_array_analog_search,
            "library_search": json_array_library_search,
        }
    })

    os.remove(r'./ms2_spectra/results/analog_search/'+filename)
    os.remove(r'./ms2_spectra/results/library_search/'+filename)
    os.rmdir(r'./ms2_spectra/results/analog_search')
    os.rmdir(r'./ms2_spectra/results/library_search')
    os.rmdir(r'./ms2_spectra/results')