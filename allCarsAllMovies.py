from flask_restful import Resource, Api, reqparse
from data import Cars, keyCounter
from DannoService import DannoService

class AllCarsAllMovies(Resource):

    def get(self):
        allCars = []
        movieArray = []
        movieDescriptions = []

        for i in range(0, keyCounter + 1):
            movieDescriptions = []
            movieArray = Cars[i].get('movies').split(',')
            
            for movie in movieArray:
                serviceResponse = DannoService().get_movie(movie)
                if serviceResponse != "Movie service is down":
                    movieDescriptions.append(serviceResponse)
                else:
                    return "Movie service is down", 503

            newCar = {
            'car_id':i,
            'vin':Cars[i].get('vin'),
            'make':Cars[i].get('make'),
            'model':Cars[i].get('model'),
            'movie details': movieDescriptions
            }

            allCars.append(newCar)
      
        return allCars, 200
