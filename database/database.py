import pymongo
from model.movies import Movies

client = pymongo.MongoClient("mongodb+srv://root:root@cluster0.mexdq.mongodb.net/test")

db = client["movies"]

movies = db["movies"]


def create_movie(movie):
    movies.insert_one(movie.__dict__)


def read_movie(movie_id):
    return movies.find_one({"movie_id": movie_id}, {'_id': 0})


def read_all_movies():
    return list(movies.find({}, {'_id': 0}))


def update_movie(movie_id, movie):
    movies.update_one({"movie_id": movie_id}, {"$set": movie.__dict__}, upsert=True)


def delete_movie(movie_id):
    movies.delete_one({"movie_id": movie_id})
