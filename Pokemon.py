# Q: What are the stats of a given type of Pokemon?
# Import the appropriate modules.
import csv, requests, operator, pandas as pd, numpy as np
from bokeh.plotting import figure, output_file, save
from bokeh.charts import Bar, output_file, save

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

# Create empty lists to sort by values later on.
name_pokemon = []
hp_pokemon = []
atk_pokemon = []
def_pokemon = []
satk_pokemon = []
sdef_pokemon = []
speed_pokemon = []

# For each Pokemon, determine its name and stats.
# Append them to their respective lists.
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
    hp_pokemon.append(hp)
    atk_pokemon.append(atk)
    def_pokemon.append(defense)
    satk_pokemon.append(satk)
    sdef_pokemon.append(sdef)
    speed_pokemon.append(speed)

rows = zip(name_pokemon,hp_pokemon,atk_pokemon,def_pokemon,satk_pokemon,sdef_pokemon,speed_pokemon)
for row in rows:
    csvwriter.writerow(row)

# Close the .csv file.
csvfile.close()

df = pd.read_csv("Stats.csv")
graph1 = Bar(df, 'Pokemon', values='Spd', legend=False, title= type_poke + "-type Pokemon Stats")

output_file("Stats.html")
save(graph1)