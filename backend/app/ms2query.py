# from ms2query.run_ms2query import default_library_file_base_names, run_complete_folder
# from ms2query.ms2library import create_library_object_from_one_dir
# import datetime
# import os

# def run_ms2query():
#     # Set the location where all your downloaded model files are stored
#     ms2query_library_files_directory = "./ms2query_library_files"
#     # define the folder in which your query spectra are stored.
#     # Accepted formats are: "mzML", "json", "mgf", "msp", "mzxml", "usi" or a pickled matchms object. 
#     ms2_spectra_directory = "./ms2_spectra"

#     # Create a MS2Library object 
#     ms2library = create_library_object_from_one_dir(ms2query_library_files_directory, default_library_file_base_names())

#     today = datetime.datetime.now()
#     folder_to_store_results = os.path.join(ms2_spectra_directory, today.strftime("%Y%m%d%H%M%S_"+"results"))

#     # Run library search and analog search on your files. 
#     # The results are stored in the specified folder_to_store_results.
#     run_complete_folder(ms2library, ms2_spectra_directory, folder_to_store_results)

#     return "ms2query DONE"