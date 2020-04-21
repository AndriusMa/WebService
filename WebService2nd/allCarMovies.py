from flask_restful import Resource, Api, reqparse
from data import Cars, keyCounter
from DannoService import DannoService

class AllCarMovies(Resource):

    def get(self, car_id):
        movieDescriptions = []
        movieArray = Cars[car_id].get('movies').split(',')
        
        for movie in movieArray:
            serviceResponse = DannoService().get_movie(movie)
            if serviceResponse != 503:
                movieDescriptions.append(serviceResponse)
            else:
                return "Movie service is down", 503
        
        newCar = {
        'car_id':car_id,
        'vin':Cars[car_id].get('vin'),
        'make':Cars[car_id].get('make'),
        'model':Cars[car_id].get('model'),
        'movie details': movieDescriptions
        }

        return newCar, 200

