import csv

all_movies = []

with open("final.csv", "r") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]

liked_movies = []
unliked_movies = []
unwatched_movies = []