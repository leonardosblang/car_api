import pymongo

client = pymongo.MongoClient("mongodb+srv://root:root@cluster0.mexdq.mongodb.net/test")

db = client["car"]

car = db["car"]


def create_car(cars):
    car.insert_one(cars.__dict__)


def read_car(cars_id):
    return car.find_one({"car_id": cars_id}, {'_id': 0})


def read_all_cars():
    return list(car.find({}, {'_id': 0}))


def update_car(cars_id, cars):
    car.update_one({"car_id": cars_id}, {"$set": cars.__dict__}, upsert=True)


def delete_car(cars_id):
    car.delete_one({"car_id": cars_id})
