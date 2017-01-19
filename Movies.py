import requests, csv, pandas as pd, numpy as np
from bokeh.plotting import figure, output_file, save
from bokeh.charts import Bar, output_file, save
from bokeh.palettes import Accent4 as pal

title_list = []
release_list = []
runtime_list = []
rating_list = []

def search_movie():
    base_url = "http://www.omdbapi.com/?"
    title_url = "t=" + input("Movie title? ")

    url = base_url + title_url
    r = requests.get(url)
    movie = r.json()
    
    title = movie['Title']
    release = movie['Released']
    rating = movie['imdbRating']
    runtime = movie['Runtime']
    
    title_list.append(title)
    release_list.append(release)
    runtime_list.append(runtime)
    rating_list.append(rating)
    
search_movie()

def query_yes_no():
    response = input("Continue adding movies? Respond with 'y' or 'n'. ")
    if response == "y":
        search_movie()
        query_yes_no()
    elif response == "n":
        print("Creating CSV file...\nCreating graphs...")
    else:
        print("Invalid response. Try again.")
        query_yes_no()

query_yes_no()

csvfile = open("Movies.csv", "w")
csvwriter = csv.writer(csvfile, delimiter = ",")
csvwriter.writerow(["Title", "Release Date", "Runtime", "IMDb Rating"])

rows = zip(title_list,release_list,runtime_list,rating_list)
for row in rows:
    csvwriter.writerow(row)

csvfile.close()

df = pd.read_csv("Movies.csv")
graph1 = Bar(df, 'Title', values='IMDb Rating', palette=pal, legend=False, title="IMDb Ratings for Movies")

output_file("Movies.html")
save(graph1)