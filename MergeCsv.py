import csv

with open("movies.csv", "r") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]
    headers = data[0]

headers.append("posted_link")

with open("final.csv", "a+")as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)

with open("movie_links.csv", "r") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movie_links = data[1:]

for movie_item in all_movies:
    posted_found = any(movie_item[8] in movie_link_items for movie_link_items in all_movie_links)
    if posted_found:
        for movie_link_item in all_movie_links:
            if movie_item[8] == movie_link_item[0]:
                movie_item.append(movie_link_item[1])
                if len(movie_item) == 28:
                    with open("final.csv", "a+") as f:
                        csv_writer = csv.writer(f)
                        csv_writer.writerow(movie_item)

