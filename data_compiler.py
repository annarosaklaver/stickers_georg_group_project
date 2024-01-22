import json
#import os

all_files = []
for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    with open (f"./People/{letter}_people.json", encoding = 'utf-8') as file:
        unfiltered_file = json.load(file)
        all_files.append(unfiltered_file)
    


# directory = "C:/Users/sarak/group_project/People"
# for files in os.listdir(directory):
#     with open (files, encoding = 'utf-8') as file:
#         unfiltered_file = json.load(file)
#     all_files.append(unfiltered_file)

    



# for file in os.People:
#     with open ('People/A_people.json', encoding = 'utf-8') as file:
#         A_people = json.load(file)




