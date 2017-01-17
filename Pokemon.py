# Q: What are the ascending speeds of a given type of Pokemon?
# Import the appropriate modules.
import csv, requests, operator

# Reach the API by building its URL.
# Use user input to ask for a certain type.
base_url = "http://pokeapi.co/api/v2/type/"
type_poke = input("Select a type. ")
url = base_url + type_poke
r = requests.get(url)

# Use .json format and use the appropriate dict. key.
results = r.json()
type_list = results["pokemon"]

# Create a .csv file for export data.
csvfile = open("Speeds.csv", "w")
csvwriter = csv.writer(csvfile, delimiter = ",")

# Establish header row.
csvwriter.writerow(["Pokemon", "Speed"])

# Create an empty dictionary to sort by values later on.
type_pokemon = {}

# For each Pokemon, determine its name and base speed stat.
# Export them into a dictionary as a list.
for pokemon in type_list:
    name = pokemon["pokemon"]["name"]
    url = pokemon["pokemon"]["url"]
    rspeed = requests.get(url)
    speed_results = rspeed.json()
    speed_list = speed_results
    speed = speed_list["stats"][0]["base_stat"]
    type_pokemon[name] = speed

# Sort by dictionary values.
sortedlist = sorted(type_pokemon.items(), key = operator.itemgetter(1))

# For each pokemon in the sorted list, write a row in the .csv file.
for pokemon in sortedlist:
    csvwriter.writerow(pokemon)

# Close the .csv file.
csvfile.close()