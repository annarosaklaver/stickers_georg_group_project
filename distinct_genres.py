import json
from collections import Counter

with open("musicians_data.json", encoding="utf-8") as file:
    musicians_data = json.load(file)

genre_frequency = {}


for entry in musicians_data:
    if type(entry["ontology/genre_label"]) is list:
        for genre in entry["ontology/genre_label"]:
            if genre not in genre_frequency:
                genre_frequency[genre] = 1
            elif genre in genre_frequency:
                genre_frequency[genre] = genre_frequency[genre] +1
    else:
        if entry["ontology/genre_label"] not in genre_frequency:
            genre_frequency[genre] = 1
        elif entry["ontology/genre_label"] in genre_frequency:
            genre_frequency[genre] = genre_frequency[genre] +1


counted_genre_frequency = Counter(genre_frequency)


genre_frequency_list = sorted(counted_genre_frequency)     

for genre in genre_frequency_list:
    if genre_frequency[genre] < 99:
        genre_frequency.pop(genre)

print(genre_frequency)

#         for word in hamlet_text_split:
#     if word not in hamlet_dictionary:
#         hamlet_dictionary[word]=1
#     elif word in hamlet_dictionary:
#         hamlet_dictionary[word]=hamlet_dictionary[word]+1
       
#         if genre in entry['ontology/genre_label'] == []:
#             for genre in entry['ontology/genre_label']:
#                 if genre not in list_of_genres:
#                     list_of_genres.append(genre)
#         if genre in entry['ontology/genre_label'] == "":
#                 if genre not in list_of_genres:
#                     list_of_genres.append(genre)

# print(list_of_genres)
