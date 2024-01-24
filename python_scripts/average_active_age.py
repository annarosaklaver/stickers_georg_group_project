#calculate average age at start of active years for musicians that have both start of active years and birthyear listed
import json

with open("cleaned_musician_data.json", encoding="utf-8") as file:
    data = json.load(file)


active_age_start = []
for entry in data:
    if ("Birthyear" in entry) and ("Active_Years_Start" in entry):
        if (type(entry["Birthyear"]) is not list) and (type(entry["Active_Years_Start"]) is not list):
            if (entry["Birthyear"].startswith("19")) or (entry["Birthyear"].startswith("20")):
                if int(entry["Active_Years_Start"]) > int(entry["Birthyear"]):
                    active_age_start.append(int(entry["Active_Years_Start"]) - int(entry["Birthyear"]))

print(active_age_start)

average_start_age = sum(active_age_start)/len(active_age_start)

print(average_start_age)