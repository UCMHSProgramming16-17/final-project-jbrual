# Import all of the appropriate modules.
import requests, csv, pandas as pd
from bokeh.charts import Bar, output_file, save
from bokeh.palettes import Accent4 as pal

# Create empty list to store movie data.
title_list = []
release_list = []
runtime_list = []
rating_list = []

# Define a movie search based on user input to repeat this action.
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
    
    # Append movie metadata to respective lists.
    title_list.append(title)
    release_list.append(release)
    runtime_list.append(runtime)
    rating_list.append(rating)
    
search_movie()

# Ask the user if they would like to add more movies to their search.
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

# Create .csv file to export data from the lists.
csvfile = open("Movies.csv", "w")
csvwriter = csv.writer(csvfile, delimiter = ",")

# Establish header row.
csvwriter.writerow(["Title", "Release Date", "Runtime", "IMDb Rating"])

# Zip the rows to write each movie's data.
rows = zip(title_list,release_list,runtime_list,rating_list)
for row in rows:
    csvwriter.writerow(row)

# Close the .csv file.
csvfile.close()

# Create a dataframe using the generated .csv file. Store bar graph in a variable form.
df = pd.read_csv("Movies.csv")
graph1 = Bar(df, 'Title', values='IMDb Rating', color='Title', palette=pal, legend=False, title="IMDb Ratings for Movies")

# Generate the .html file for the Bokeh graph.
output_file("Movies.html")
save(graph1)