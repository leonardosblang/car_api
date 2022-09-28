from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from database.database import create_movie, read_movie, read_all_movies, update_movie, delete_movie
from model.movies import Movies

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}




@app.post("/movies")
async def create_movie_api(movie: Movies):
    create_movie(movie)
    return {"message": "Movie created successfully"}


@app.get("/movies/{movie_id}")
async def read_movie_api(movie_id: int):
    return read_movie(movie_id)


@app.get("/movies")
async def read_all_movies_api():
    return read_all_movies()


@app.put("/movies/{movie_id}")
async def update_movie_api(movie_id: int, movie: Movies):
    update_movie(movie_id, movie)
    return {"message": "Movie updated successfully"}


@app.delete("/movies/{movie_id}")
async def delete_movie_api(movie_id: int):
    delete_movie(movie_id)
    return {"message": "Movie deleted successfully"}
