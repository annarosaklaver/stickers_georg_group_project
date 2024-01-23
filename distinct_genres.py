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

grouped_genres = {"Experimental" : ["Instrumental", "Industrial music"],
                  "Blues" : ["Blues", "Contemporary R&B", "Chicago blues", "Blues rock", "Electric blues", "Country blues"],
                  "Country" : ["Country music", "Country rock", "Alternative country", "Bluegrass music", "Country blues"],
                  "Easy_Listening" : ["New-age music", "Easy listening", "Downtempo"],
                  "Electronic" : ["Dance music", "Electronic", "Alternative hip hop", "Drumb and bass", "House music", "Trip hop", "Intelligent dance music", "Electronica", "Electro (music)", "Industrial metal", "New wave music", "Synth pop", "New-age music", "Ambient music", "Industrial rock", "Disco", "Trap music", "Post-rock", "Eurodance", "Downtempo", "Progressive house", "Alternative dance", "Dub music", "Neo soul", "Dubstep", "Deep house", "Trance music", "Grime music"],
                  "Folk" : ["Folk music", "Folk rock", "Indie folk", "Celtic music", "Singer-songwriter"],
                  "Hip_Hop" : ["Hip hop music", "Alternative hip hop", "Gangsta rap", "Underground hip hop"],
                  "Jazz" : ["Jazz", "Avant-garde jazz", "Bossa nova", "Big band", "Bebop", "Hard bop", "Swing music", "Free jazz"],
                  "Pop" : ["Pop music", "Pop-folk", "Dance pop", "Indie pop", "Pop rock", "Power pop", "Pop punk", "K-pop", "Urban contemporary", "Synth pop", "Chanson", "J-pop"],
                  "Soul" : ["Contemporary R&B", "Rhythm and blues", "Soul music", "Disco", "Neo soul", "Blue-eyed soul"],
                  "Rock" : ["Rock music", "Alternative rock", "Indie rock", "Heavy metal music", "Hard rock", "Pop rock", "Power pop", "Progressive rock", "Folk rock", "Rock and roll", "Country rock", "Grunge", "Experimental rock", "Glam rock", "Blues rock", "Punk rock", "Garage rock", "Psychedelic rock", "Gothic rock", "Industrial rock", "Post-rock", "Christian rock", "Roots rock", "Alternative dance", "Art rock", "Instrumental rock", "Rockabilly", "Noise rock", "Southern rock", "Dream pop", "Post-grunge"],
                  "Metal" : ["Heavy metal music", "Glam metal", "Black metal", "Industrial metal", "Symphonic metal", "Death metal", "Thrash metal", "Alternative metal", "Power metal", "Progressive metal", "Doom metal", "Speed metal", "Metalcore", "Nu metal"],
                  "Punk" : ["Pop punk", "Post punk", "Punk rock", "Hardcore punk", "Post-hardcore"],
                  "Other" : ["Hindustani classical music", "Musical theatre", "World music", "Indepedent music", "Acoustic music", "Contemporary worship music", "Film score", "Opera", "Contemporary classical music", "Ska", "Traditional black gospel", "Urban contemporary gospel", "Reggae", "Funk", "Rocksteady", "Indian classical music"]}


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
