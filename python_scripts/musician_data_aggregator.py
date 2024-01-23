import json
from python_scripts.data_compiler import compile_data

#run data compiler
all_files = compile_data()
all_genres = set()

#create a dataset containing all musicians that have a genre listed (and create a list of all genres)
genre_data = []
for entry in all_files:
    if "musical artist" in entry["http://www.w3.org/1999/02/22-rdf-syntax-ns#type_label"]: 
        if "ontology/genre_label" in entry:
            genre_data.append(entry)
            for genre in entry["ontology/genre_label"]:
                all_genres.add(genre)

with open("musicians_data.json", "w", encoding="utf-8") as file:
    json.dump(genre_data, file, indent = 4)
