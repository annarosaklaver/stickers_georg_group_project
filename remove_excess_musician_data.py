import json
import csv

with open("musicians_data.json", encoding="utf-8") as file:
    musicians_data = json.load(file)

#cleaning all the musicians data:

# cleaned_musicians_data = []
# for entry in musicians_data:
#     entry_dict = {}
#     entry_dict["Title"] = entry["title"]
#     if "ontology/activeYearsStartYear" in entry:
#         entry_dict["Active_Years_Start"] = entry["ontology/activeYearsStartYear"]
#     entry_dict["Genre(s)"] = entry["ontology/genre_label"]
#     if "ontology/activeYearsEndYear" in entry:
#         entry_dict["Active_Years_End"] = entry["ontology/activeYearsEndYear"]
#     if "ontology/birthDate" in entry:
#         entry_dict["Birthdate"] = entry["ontology/birthDate"]
#     if "ontology/birthYear" in entry:
#         entry_dict["Birthyear"] = entry["ontology/birthYear"]
#     if "ontology/deathDate" in entry:
#         entry_dict["Deathdate"] = entry["ontology/deathDate"]
#     if "ontology/deathYear" in entry:
#         entry_dict["Deathyear"] = entry["ontology/deathYear"]
#     cleaned_musicians_data.append(entry_dict)

# with open("cleaned_musician_data.json", "w", encoding="utf-8") as file:
#     json.dump(cleaned_musicians_data, file, indent = 4)



# create a list of birthyears for Jazz artists
jazz_birthyears = []
for entry in musicians_data:
    if "Jazz" in entry["ontology/genre_label"]:
        if "ontology/birthYear" in entry:
            jazz_birthyears.append(entry["ontology/birthYear"])

print(jazz_birthyears)

jazz_birthyears_dict = {}
jazz_birthyears_dict["birthyears"] = jazz_birthyears

with open("jazz_birthyears.csv", "w", newline = "") as file:
    writer = csv.writer(file)
    writer.writerow(jazz_birthyears_dict)
