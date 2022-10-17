from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from database.database import create_car, read_car, read_all_cars, update_car, delete_car
from model.car import Car

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


@app.post("/car")
async def create_car_api(car: Car):
    create_car(car)
    return {"message": "Car created successfully"}


@app.get("/car/{car_id}")
async def read_car_api(car_id: int):
    return read_car(car_id)


@app.get("/car")
async def read_all_car_api():
    return read_all_cars()


@app.put("/car/{car_id}")
async def update_car_api(car_id: int, car: Car):
    update_car(car_id, car)
    return {"message": "Car updated successfully"}


@app.delete("/car/{car_id}")
async def delete_car_api(car_id: int):
    delete_car(car_id)
    return {"message": "Car deleted successfully"}
