import json
import csv

with open("musicians_data.json", encoding="utf-8") as file:
    musicians_data = json.load(file)

#cleaning all the musicians data:

cleaned_musicians_data = []
for entry in musicians_data:
    entry_dict = {}
    entry_dict["Title"] = entry["title"]
    if "ontology/activeYearsStartYear" in entry:
        entry_dict["Active_Years_Start"] = entry["ontology/activeYearsStartYear"]
    entry_dict["Genre(s)"] = entry["ontology/genre_label"]
    if "ontology/activeYearsEndYear" in entry:
        entry_dict["Active_Years_End"] = entry["ontology/activeYearsEndYear"]
    if "ontology/birthDate" in entry:
        entry_dict["Birthdate"] = entry["ontology/birthDate"]
    if "ontology/birthYear" in entry:
        entry_dict["Birthyear"] = entry["ontology/birthYear"]
    if "ontology/deathDate" in entry:
        entry_dict["Deathdate"] = entry["ontology/deathDate"]
    if "ontology/deathYear" in entry:
        entry_dict["Deathyear"] = entry["ontology/deathYear"]
    cleaned_musicians_data.append(entry_dict)

#make a json file with the cleaned data
with open("cleaned_musician_data.json", "w", encoding="utf-8") as file:
    json.dump(cleaned_musicians_data, file, indent = 4)

#make a csv file containing an entry for each genre an artist has listed, with their birthyear
with open("genre_and_birthyear.csv", "w", newline="", encoding="utf-8") as file:
    fieldnames = ["Title", "Genre", "Birthyear"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for entry in cleaned_musicians_data:
        if "Birthyear" in entry:
            if type(entry["Genre(s)"]) is list:
                for genre in entry["Genre(s)"]: 
                    writer.writerow({"Title" : entry["Title"], "Genre" : genre, "Birthyear" : entry["Birthyear"]})
            else:
                writer.writerow({"Title" : entry["Title"], "Genre" : entry["Genre(s)"], "Birthyear" : entry["Birthyear"]})

# # create a list of birthyears for Jazz artists
# jazz_birthyears = []
# for entry in musicians_data:
#     if "Jazz" in entry["ontology/genre_label"]:
#         if "ontology/birthYear" in entry:
#             jazz_birthyears.append(entry["ontology/birthYear"])

# print(jazz_birthyears)

# # tried to create a ditionary containing one key with a list as value, didn't work to write the csv
# # jazz_birthyears_dict = {}
# # jazz_birthyears_dict["birthyears"] = jazz_birthyears

# with open("jazz_birthyears.csv", "w", newline = "") as file:
#     fieldnames = ['birthyear']
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
#     writer.writeheader()
#     for birthyear in jazz_birthyears:
#         writer.writerow({'birthyear' : birthyear})
