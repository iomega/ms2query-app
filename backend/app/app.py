from flask import Flask, jsonify
from ms2query.run_ms2query import download_default_models, default_library_file_base_names, run_complete_folder
from ms2query.ms2library import create_library_object_from_one_dir
import os
import csv
import json

app = Flask(__name__)

###########
### API ###
###########

@app.route('/ping')
def pong():
    return {"message": "pong"}

@app.route('/run_ms2query')
def ms2query():
    response = run_ms2query()
    return response

@app.route('/get_results/<filename>')
def results(filename):
    file = csv2json(r'./ms2_spectra/results/library_search/'+filename+'.csv', r'./ms2_spectra/results/library_search/'+filename+'.json')
    return file


#################
### FUNCTIONS ###
#################

def run_ms2query():
    # Set the location where all your downloaded model files are stored
    ms2query_library_files_directory = "./ms2query_library_files"
    # define the folder in which your query spectra are stored.
    # Accepted formats are: "mzML", "json", "mgf", "msp", "mzxml", "usi" or a pickled matchms object. 
    ms2_spectra_directory = "./ms2_spectra"

    # Downloads pretrained models and files for MS2Query (>10GB download)
    # download_default_models(ms2query_library_files_directory, default_library_file_base_names())

    # Create a MS2Library object 
    ms2library = create_library_object_from_one_dir(ms2query_library_files_directory, default_library_file_base_names())

    folder_to_store_results = os.path.join(ms2_spectra_directory, "results")

    # Run library search and analog search on your files. 
    # The results are stored in the specified folder_to_store_results.
    run_complete_folder(ms2library, ms2_spectra_directory, folder_to_store_results)

    return "ms2query DONE"


def csv2json(csvFilePath, jsonFilePath):
    
    jsonArray = []
    
    with open(csvFilePath, encoding='utf-8') as csvf: 
        csvReader = csv.DictReader(csvf) 

        for row in csvReader: 
            jsonArray.append(row)

    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)

    return jsonString
        
#################
#################
#################

# if __name__ == '__main__':
#     app.run(host="0.0.0.0", port=5000)