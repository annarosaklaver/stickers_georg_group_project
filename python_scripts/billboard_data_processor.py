import csv
import json
from collections import Counter

billboard_data = []
with open("merged_billboard_data.csv", "r", encoding= "utf-8") as file:
    reader = csv.DictReader(file)
    for dictionary in reader:
        billboard_data.append(dictionary)

for entry in billboard_data:
    for character in "'[] ":
        entry["spotify_genre"] = entry["spotify_genre"].replace(character, "")
    entry["spotify_genre"] = entry["spotify_genre"].split(",")

genre_frequency = {}
for entry in billboard_data:
    if type(entry["spotify_genre"]) is list:
        for genre in entry["spotify_genre"]:
            if genre not in genre_frequency:
                genre_frequency[genre] = 1
            elif genre in genre_frequency:
                genre_frequency[genre] = genre_frequency[genre] +1
    else:
        if entry["spotify_genre"] not in genre_frequency:
            genre_frequency[entry["spotify_genre"]] = 1
        elif entry["spotify_genre"] in genre_frequency:
            genre_frequency[entry["spotify_genre"]] = genre_frequency[entry["spotify_genre"]] +1

counted_genre_frequency = Counter(genre_frequency)

# print(counted_genre_frequency)
# print(len(counted_genre_frequency))

genre_frequency_list = sorted(counted_genre_frequency)

for genre in genre_frequency_list:
    if genre_frequency[genre] < 1000:
        genre_frequency.pop(genre)

# print(len(genre_frequency))
        
# print(genre_frequency)

grouped_genres = {"Blues" : ["doo-wop", "rhythmandblues", "jazzblues", "electricblues", "soulblues", "blues", "britishblues"],
                  "Country" : ["contemporarycountry", "country", "countryroad", "arkansascountry", "countrydawn", "oklahomacountry", "nashvillesound", "outlawcountry", "redneck"],
                  "Easy_Listening" : ["deepadultstandards", "adultstandards", "hollywood", "lounge", "easylistening", "classicgirlgroup"],
                  "Electronic" : ["divahouse", "hiphouse", "edm", "electropop", "tropicalhouse"],
                  "Folk" : ["folk", "lilith", "singer-songwriter", "neomellow", "traditionalfolk", "stompandholler", "canadiansinger-songwriter"],
                  "Hip_Hop" : ["urbancontemporary", "althiphop", "hiphop", "gansterrap", "poprap", "rap", "southernhiphop", "eastcoasthiphop", "hardcorehiphop", "oldschoolhiphop", "raprock", "crunk", "dirtysouthrap", "neworleansrap", "trap", "detroithiphop", "melodicrap", "freestyle", "queenshiphop", "conscioushiphop", "gfunk", "westcoastrap", "miamihiphop", "chicagorap", "canadianhiphop", "torontorap"],
                  "Jazz" : ["vocaljazz", "jazzfunk"],
                  "Pop" : ["brillbuilding pop", "newwavepop", "synthpop", "bubblegumdance", "eurodance", "europop", "boyband", "dancepop", "hippop", "australianpop", "girlgroup", "pop", "post-teenpop", "candypop", "viralpop", "canadianpop", "bubblegumpop", "classicukpop", "baroquepop", "sunshinepop", "latinpop", "deeppopr&b", "ukpop", "classiccountrypop", "indiepop", "acousticpop", "powerpop", "country pop", "indiepoptimism", "reggaefusion", "latin", "reggaeton", "tropical"],
                  "Soul_and_R&B" : ["classicsoul", "disco", "funk", "motown", "newjackswing", "phillysoul", "post-disco", "quietstorm", "soul", "southernsoul", "classicsoul", "memphissoul", "hi-nrg", "r&b", "neosoul", "britishsoul", "northernsoul", "chicagosoul", "alternativer&b"],
                  "Rock" : ["classicrock", "folkrock", "rock-and-roll", "mellowgold", "softrock", "countryrock", "heartlandrock", "albumrock", "hardrock", "rock", "dancerock", "newromantic", "newwave", "alternativerock", "poprock", "glamrock", "pianorock", "permanentwave", "modernrock", "poppunk", "moderncountryrock", "funkrock", "rockabilly", "merseybeat", "britishinvasion", "psychedelicrock", "classicgaragerock", "bluesrock", "rootsrock", "southernrock", "yachtrock", "artrock", "minneapolissound", "australianrock", "symphonicrock", "clasiccanadianrock", "protopunk", "progressiverock", "emo", "indierock"],
                  "Metal" : ["glammetal", "metal", "alternativemetal", "post-grunge", "numetal", "funkmetal"]}

# with open("billboard_data.json", "w", encoding="utf-8") as file:
#     json.dump(billboard_data, file, indent = 4)

#grouped_musicians_data is a list of dictionaries that we will use to create a csv file
grouped_billboard_data = []

#loop over entries in billboard_data 
    #loop over the grouped genres, check if the entry contains a subgenre and group accordingly
    #note!! this yields a dataset with a lot of duplicates that need to be removed in R
for entry in billboard_data:
    for grouped_genre in grouped_genres:
        if type(entry["spotify_genre"]) is list:
            for genre in entry["spotify_genre"]:
                if genre in grouped_genres[grouped_genre]:
                    grouped_billboard_data.append({"Date" : entry["weekID"],
                                                   "Artist" : entry["Performer"],
                                    "Genre" : grouped_genre})  
        else:
            if genre in grouped_genres[grouped_genre]:
                grouped_billboard_data.append({"Date" : entry["weekID"],
                                               "Artist" : entry["Performer"],
                                    "Genre" : grouped_genre})

#make dates by year and not a string
for entry in grouped_billboard_data:
    entry["Date"] = int(entry["Date"][-4:])

# with open("grouped_billboard_data.json", "w", encoding="utf-8") as file:
#      json.dump(grouped_billboard_data, file, indent = 4)

with open("output_data/grouped_billboard_data.csv", "w", newline="", encoding="utf-8") as file:
    fieldnames = ["Artist", "Genre", "Date"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for entry in grouped_billboard_data:
        writer.writerow({"Artist" : entry["Artist"], "Genre" : entry["Genre"], "Date" : entry["Date"]})