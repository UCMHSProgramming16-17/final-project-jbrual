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
csvfile = open("Stats.csv", "w")
csvwriter = csv.writer(csvfile, delimiter = ",")

# Establish header row.
csvwriter.writerow(["Pokemon", "HP", "Atk", "Def", "SAtk", "SDef", "Spd"])

# Create an empty dictionary to sort by values later on.
name_pokemon = []
hp_pokemon = []
atk_pokemon = []
def_pokemon = []
satk_pokemon = []
sdef_pokemon = []
speed_pokemon = []

# For each Pokemon, determine its name and base speed stat.
# Export them into a dictionary as a list.
for pokemon in type_list:
    name = pokemon["pokemon"]["name"]
    url = pokemon["pokemon"]["url"]
    rspeed = requests.get(url)
    results = rspeed.json()
    hp = results["stats"][5]["base_stat"]
    atk = results["stats"][4]["base_stat"]
    defense = results["stats"][3]["base_stat"]
    satk = results["stats"][2]["base_stat"]
    sdef = results["stats"][1]["base_stat"]
    speed = results["stats"][0]["base_stat"]
    
    name_pokemon.append(name)
    atk_pokemon.append(atk)
    def_pokemon.append(defense)
    satk_pokemon.append(satk)
    sdef_pokemon.append(sdef)
    speed_pokemon.append(speed)

rows = zip(name_pokemon,atk_pokemon,def_pokemon,satk_pokemon,sdef_pokemon,speed_pokemon)
for row in rows:
    csvwriter.writerow(row)

# Close the .csv file.
csvfile.close()