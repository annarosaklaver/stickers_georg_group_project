import json
from data_compiler import compile_data

#run data compiler
all_files = compile_data()

#create an empty list for all "musical artist" entries
musician_data = []
 
#loop over all entries to create a list of all "musical artist" entries and create a set of all unique labels.
for entry in all_files:
    if "musical artist" in entry["http://www.w3.org/1999/02/22-rdf-syntax-ns#type_label"]:
        musician_data.append(entry)
   
print(len(musician_data))