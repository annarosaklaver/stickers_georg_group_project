import json
from data_compiler import compile_data

#run data compiler
all_files = compile_data()

# create a list of entries that include a cause of death
dead_people = []
for entry in all_files:
    if "ontology/deathCause_label" in entry:
        dead_people.append(entry)


# create a list of entries that include both cause of death and occupation
dead_people_with_jobs = []
for entry in dead_people:
    if "ontology/occupation_label" in entry:
        dead_people_with_jobs.append(entry)

#create a json file from dead_people_with_jobs
with open("dead_people_with_jobs.json", "w", encoding="utf-8") as file:
    json.dump(dead_people_with_jobs, file)