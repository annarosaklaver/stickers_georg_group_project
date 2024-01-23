import json
#import os
def compile_data():
    all_files = []
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        with open (f"./People/{letter}_people.json", encoding = 'utf-8') as file:
            unfiltered_file = json.load(file)
            all_files.extend(unfiltered_file)
    return all_files




