import unittest
from database.database import create_movie, read_movie, read_all_movies, update_movie, delete_movie
from model.movies import Movies
import unittest.mock as mock


class TestMovies(unittest.TestCase):

    @mock.patch('database.database.movies.insert_one')
    def test_create_movie(self, mock_insert):
        movie = Movies(title='test', release_date='test', movie_id=1, director='test')
        create_movie(movie)
        mock_insert.assert_called_once_with(movie.__dict__)

    @mock.patch('database.database.movies.find_one')
    def test_read_movie(self, mock_find):
        movie_id = 1
        read_movie(movie_id)
        mock_find.assert_called_once_with({"movie_id": movie_id}, {'_id': 0})

    @mock.patch('database.database.movies.find')
    def test_read_all_movies(self, mock_find):
        read_all_movies()
        mock_find.assert_called_once_with({}, {'_id': 0})

    @mock.patch('database.database.movies.update_one')
    def test_update_movie(self, mock_update):
        movie_id = 1
        movie = Movies(title='test', release_date='test', movie_id=1, director='test')
        update_movie(movie_id, movie)
        mock_update.assert_called_once_with({"movie_id": movie_id}, {"$set": movie.__dict__}, upsert=True)

    @mock.patch('database.database.movies.delete_one')
    def test_delete_movie(self, mock_delete):
        movie_id = 1
        delete_movie(movie_id)
        mock_delete.assert_called_once_with({"movie_id": movie_id})


    @mock.patch('database.database.movies.insert_one')
    def test_create_movie_negative(self, mock_insert):
        movie = Movies(title='test', release_date='test', movie_id=1, director='test')
        create_movie(movie)
        mock_insert.reset_mock()
        mock_insert.assert_not_called()

    @mock.patch('database.database.movies.find_one')
    def test_read_movie_negative(self, mock_find):
        movie_id = 1
        read_movie(movie_id)
        mock_find.reset_mock()
        mock_find.assert_not_called()




if __name__ == '__main__':
    unittest.main()