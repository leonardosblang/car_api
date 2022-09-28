from pydantic import BaseModel


class Movies(BaseModel):
    title: str
    release_date: str
    movie_id: int
    director: str
