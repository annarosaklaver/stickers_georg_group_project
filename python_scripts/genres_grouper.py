import json
from collections import Counter
import csv

#import the musicians data and make it a variable
with open("musicians_data.json", encoding="utf-8") as file:
    musicians_data = json.load(file)

#create a dictionary to keep track of genre frequency and iterate over musicians_data to compile the dictionary
    # separate loops are needed for genre entries that are lists and genre entries containing a single value
    # if the genre is not in the dictionary: add it to the dictionary and set the count to one
    #if the genre is in the dictionary: add 1 to the count
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

#sorted genres in order of frequency
counted_genre_frequency = Counter(genre_frequency)

# sort the genres by frequency and only include genres that appear over 99 times
genre_frequency_list = sorted(counted_genre_frequency)     

for genre in genre_frequency_list:
    if genre_frequency[genre] < 99:
        genre_frequency.pop(genre)

# sort the genres that appear over 99 times into groups based on wikipedia classification
grouped_genres = {"Blues" : ["Blues", "Contemporary R&B", "Chicago blues", "Blues rock", "Electric blues", "Country blues"],
                  "Country" : ["Country music", "Country rock", "Alternative country", "Bluegrass music", "Country blues"],
                  "Easy_Listening" : ["New-age music", "Easy listening", "Downtempo"],
                  "Electronic" : ["Dance music", "Electronic", "Alternative hip hop", "Drum and bass", "House music", "Trip hop", "Intelligent dance music", "Electronica", "Electro (music)", "Industrial metal", "New wave music", "Synth pop", "New-age music", "Ambient music", "Industrial rock", "Disco", "Trap music", "Post-rock", "Eurodance", "Downtempo", "Progressive house", "Alternative dance", "Dub music", "Neo soul", "Dubstep", "Deep house", "Trance music", "Grime music"],
                  "Folk" : ["Folk music", "Folk rock", "Indie folk", "Celtic music", "Singer-songwriter", "Acoustic music"],
                  "Hip_Hop" : ["Hip hop music", "Alternative hip hop", "Gangsta rap", "Underground hip hop"],
                  "Jazz" : ["Jazz", "Avant-garde jazz", "Bossa nova", "Big band", "Bebop", "Hard bop", "Swing music", "Free jazz"],
                  "Pop" : ["Pop music", "Pop-folk", "Dance pop", "Indie pop", "Pop rock", "Power pop", "Pop punk", "K-pop", "Urban contemporary", "Synth pop", "Chanson", "J-pop", "Contemporary worship music"],
                  "Soul_and_R&B" : ["Contemporary R&B", "Rhythm and blues", "Soul music", "Disco", "Neo soul", "Blue-eyed soul",  "Traditional black gospel", "Urban contemporary gospel", "Funk", "Reggae", "Rocksteady"],
                  "Rock" : ["Rock music", "Alternative rock", "Indie rock", "Heavy metal music", "Hard rock", "Pop rock", "Power pop", "Progressive rock", "Folk rock", "Rock and roll", "Country rock", "Grunge", "Experimental rock", "Glam rock", "Blues rock", "Punk rock", "Garage rock", "Psychedelic rock", "Gothic rock", "Industrial rock", "Post-rock", "Christian rock", "Roots rock", "Alternative dance", "Art rock", "Instrumental rock", "Rockabilly", "Noise rock", "Southern rock", "Dream pop", "Post-grunge", "Ska", "Pop punk", "Post punk", "Punk rock", "Hardcore punk", "Post-hardcore"],
                  "Metal" : ["Heavy metal music", "Glam metal", "Black metal", "Industrial metal", "Symphonic metal", "Death metal", "Thrash metal", "Alternative metal", "Power metal", "Progressive metal", "Doom metal", "Speed metal", "Metalcore", "Nu metal"]}

#import the clean musicians dataset
with open("cleaned_musician_data.json", encoding="utf-8") as file:
    clean_musicians_data = json.load(file)

#grouped_musicians_data is a list of dictionaries that we will use to create a csv file
grouped_musicians_data = []

#loop over entries in clean_musicians_data and only include entries that contain a birthyear
    #loop over the grouped genres, check if the entry contains a subgenre and group accordingly
    #note!! this yields a dataset with a lot of duplicates that need to be removed in R
for entry in clean_musicians_data:
    if "Birthyear" in entry:
        for grouped_genre in grouped_genres:
            if type(entry["Genre(s)"]) is list:
                for genre in entry["Genre(s)"]:
                    if genre in grouped_genres[grouped_genre]:
                        grouped_musicians_data.append({"Title" : entry["Title"],
                                        "Birthyear" : entry["Birthyear"],
                                        "Genre(s)" : grouped_genre})  
            else:
                if genre in grouped_genres[grouped_genre]:
                    grouped_musicians_data.append({"Title" : entry["Title"],
                                        "Birthyear" : entry["Birthyear"],
                                        "Genre(s)" : grouped_genre})

# write the data with grouped genres to a csv file
with open("output_data/grouped_genre_and_birthyear.csv", "w", newline="", encoding="utf-8") as file:
    fieldnames = ["Title", "Genre", "Birthyear"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for entry in grouped_musicians_data:
        if type(entry["Genre(s)"]) is list:
            for genre in entry["Genre(s)"]: 
                writer.writerow({"Title" : entry["Title"], "Genre" : genre, "Birthyear" : entry["Birthyear"]})
        else:
            writer.writerow({"Title" : entry["Title"], "Genre" : entry["Genre(s)"], "Birthyear" : entry["Birthyear"]})

#creating the exact same csv, but with starting year of a musician's career instead of birthyear (analysis pipeline is the same).
career_musicians_data = []

for entry in clean_musicians_data:
    if "Active_Years_Start" in entry:
        for grouped_genre in grouped_genres:
            if type(entry["Genre(s)"]) is list:
                for genre in entry["Genre(s)"]:
                    if genre in grouped_genres[grouped_genre]:
                        career_musicians_data.append({"Title" : entry["Title"],
                                        "Career_Start" : entry["Active_Years_Start"],
                                        "Genre(s)" : grouped_genre})  
            else:
                if genre in grouped_genres[grouped_genre]:
                    grouped_musicians_data.append({"Title" : entry["Title"],
                                        "Career_Start" : entry["Active_Years_Start"],
                                        "Genre(s)" : grouped_genre})
    else:
        if "Birthyear" in entry:
            for grouped_genre in grouped_genres:
                if type(entry["Genre(s)"]) is list:
                    for genre in entry["Genre(s)"]:
                        if genre in grouped_genres[grouped_genre]:
                            career_musicians_data.append({"Title" : entry["Title"],
                                            "Career_Start" : int(entry["Birthyear"]) + 20,
                                            "Genre(s)" : grouped_genre})  
                else:
                    if genre in grouped_genres[grouped_genre]:
                        grouped_musicians_data.append({"Title" : entry["Title"],
                                            "Career_Start" : int(entry["Birthyear"]) + 20,
                                            "Genre(s)" : grouped_genre})
                        
# write the data with grouped genres to a csv file
with open("output_data/grouped_genre_and_career_start.csv", "w", newline="", encoding="utf-8") as file:
    fieldnames = ["Title", "Genre", "Career_Start"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for entry in career_musicians_data:
        if type(entry["Genre(s)"]) is list:
            for genre in entry["Genre(s)"]: 
                writer.writerow({"Title" : entry["Title"], "Genre" : genre, "Career_Start" : entry["Career_Start"]})
        else:
            writer.writerow({"Title" : entry["Title"], "Genre" : entry["Genre(s)"], "Career_Start" : entry["Career_Start"]})
