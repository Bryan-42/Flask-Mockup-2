from flask import Flask, json, jsonify, request
from Storage import liked_movies, unliked_movies, unwatched_movies, all_movies
from DemographicFiltering import output
from ContentFiltering import get_recomendation

app = Flask(__name__)
@app.route("/get-movie")
def get_movie():
    movie_data = {
        "title":all_movies[0][19],
        "posted_link":all_movies[0][27],
        "release_data":all_movies[0][13] or "N/A",
        "duration":all_movies[0][15],
        "rating":all_movies[0][20],
        "overview":all_movies[0][9],
    }
    return jsonify({
        "data":movie_data,
        "status":"success"
    })

@app.route("/liked-movie", methods = ["POST"])
def liked_movie():
    movie = all_movies[0]
    liked_movies.append(movie)
    all_movies.pop(0)
    return jsonify({
        "status":"success"
    }),201

@app.route("/unliked-movie", methods = ["POST"])
def unliked_movie():
    movie = all_movies[0]
    unliked_movies.append(movie)
    all_movies.pop(0)
    return jsonify({
        "status":"success"
    }),201

@app.route("/unwatched-movie", methods = ["POST"])
def unwatched_movie():
    movie = all_movies[0]
    unwatched_movies.append(movie)
    all_movies.pop(0)
    return jsonify({
        "status":"success"
    }),201

@app.route("/popular-movie")
def popular_movie():
    movie_data = []
    for movie in output:
        _d = {
            "title":movie[0],
            "posted_link":movie[1],
            "release_date":movie[2] or "N/A",
            "duration":movie[3],
            "rating":movie[4],
            "overview":movie[5],
        }
        movie_data.append(_d)
    return jsonify({
        "data":movie_data,
        "status":"success"
    }),200

@app.route("/recomended-movie")
def recomended_movie():
    all_recomended_movies = []
    for all_liked_movie in liked_movies:
        output = get_recomendation(liked_movie[19])
        for data in output:
            all_recomended_movies.append(data)
    import itertools
    all_recomended_movies.sort()
    all_recomended_movies = list(all_recomended_movies for all_recomended_movies, _ in itertools.groupby(all_recomended_movies))
    movie_data = []
    for recomend in all_recomended_movies:
        _d = {
            "title":recomend[0],
            "posted_link":recomend[1],
            "release_data":recomend[2] or "N/A",
            "duration":recomend[3],
            "rating":recomend[4],
            "overview":recomend[5],
        }
        movie_data.append(_d)
        return jsonify({
            "data":movie_data,
            "status":"success"
        }),200

if __name__ == "__main__":
    app.run()