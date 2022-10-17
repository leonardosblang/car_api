import unittest
import unittest.mock as mock

from database.database import create_car, read_car, read_all_cars, update_car, delete_car
from model.car import Car





# Testes com mock
class TestCarMock(unittest.TestCase):

    @mock.patch('database.database.car.insert_one')
    def test_create_car(self, mock_insert):
        car = Car(brand='test', max_speed=200, car_id=1, year=2002)
        create_car(car)
        mock_insert.assert_called_once_with(car.__dict__)

    @mock.patch('database.database.car.find_one')
    def test_read_car(self, mock_find):
        car_id = 1
        read_car(car_id)
        mock_find.assert_called_once_with({"car_id": car_id}, {'_id': 0})

    @mock.patch('database.database.car.find')
    def test_read_all_cars(self, mock_find):
        read_all_cars()
        mock_find.assert_called_once_with({}, {'_id': 0})

    @mock.patch('database.database.car.update_one')
    def test_update_car(self, mock_update):
        car_id = 1
        car = Car(brand='test', max_speed=200, car_id=1, year=2002)
        update_car(car_id, car)
        mock_update.assert_called_once_with({"car_id": car_id}, {"$set": car.__dict__}, upsert=True)

    @mock.patch('database.database.car.delete_one')
    def test_delete_car(self, mock_delete):
        car_id = 1
        delete_car(car_id)
        mock_delete.assert_called_once_with({"car_id": car_id})

    @mock.patch('database.database.car.insert_one')
    def test_create_car_negative(self, mock_insert):
        car = Car(brand='test', max_speed=200, car_id=1, year=2002)
        create_car(car)
        mock_insert.reset_mock()
        mock_insert.assert_not_called()

    @mock.patch('database.database.car.find_one')
    def test_read_car_negative(self, mock_find):
        car_id = 1
        read_car(car_id)
        mock_find.reset_mock()
        mock_find.assert_not_called()


# Testes sem mock

class TestCar(unittest.TestCase):

    def test_create_car(self):
        car = Car(brand="Audi", max_speed=250, car_id=1, year=2020)
        create_car(car)
        #assetr equal the car id from the database with the car id from the car object instead of the whole object
        self.assertEqual(read_car(1)["car_id"], car.car_id)

    def test_read_car(self):
        car = Car(brand="Audi", max_speed=250, car_id=1, year=2020)
        self.assertEqual(read_car(1)["car_id"], car.car_id)

    def test_update_car(self):
        car = Car(brand="Audi", max_speed=250, car_id=1, year=2020)
        update_car(1, car)
        self.assertEqual(read_car(1)["car_id"], car.car_id)


if __name__ == '__main__':
    unittest.main()
