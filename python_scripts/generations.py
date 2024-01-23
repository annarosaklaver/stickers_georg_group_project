import csv

generation_dict = {'Lost Generation': 1883, 'Greatest Generation': 1901, 'Silent Generation': 1928, 'Baby Boomers': 1946, 'Generation X': 1965, 'Millennilials': 1981, 'Generation Z': 1997, 'Generation Alpha': 2010}

with open("generations.csv", "w", newline = "") as file:
    fieldnames = ['generation', 'start_date']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for key in generation_dict: 
        writer.writerow({'generation': key, 'start_date' : generation_dict[key]})


