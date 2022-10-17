from pydantic import BaseModel


class Car(BaseModel):
    brand: str
    max_speed: int
    car_id: int
    year: int
