from flask_restful import Resource, Api, reqparse
from data import Cars, keyCounter, vinArray
from DannoService import DannoService

class Car(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('vin', type=str, required=True, location='json', help="Vin number must be provided")
        self.parser.add_argument('make', type=str, required=True, location='json', help="Make must be provided")
        self.parser.add_argument('model', type=str, required=True, location='json', help="Model must be provided")
        self.parser.add_argument('movies', type=str, required=True, location='json', help="At least one movie must be provided")


    def get(self):
        allCars = []
        for car in Cars.values():
            allCars.append(car)
        if len(allCars) is 0:
            return "List is empty", 200
        else:
            return allCars, 200
    
    def post(self):
        args = self.parser.parse_args()
        global keyCounter
        keyCounter += 1
        newCar = {
            'car_id':keyCounter,
            'vin':args['vin'],
            'make':args['make'],
            'model':args['model'],
            'movies':args['movies']
        }
        if args['vin'] in vinArray:
            keyCounter -= 1
            return "vin number must be unique to the car", 400

        else:
            movie_ids = args['movies'].split(',')
            movies = DannoService().get_all_movies()

            if movies == "Movie service is down":
                return "Movie service is down, can't post new movies", 503

            duplicates = []
            for movie_id in movie_ids:
                try:                  
                    movies[int(movie_id)].get('id')
                    for duplicate in duplicates:
                        if duplicate == int(movie_id):
                            keyCounter -= 1
                            return "Movie duplicates found in provided json", 400

                    duplicates.append(int(movie_id))
                    
                except IndexError as e:
                    keyCounter -= 1
                    return "At least one movie id is invalid or json format is unrecognized", 400
                
            Cars[newCar['car_id']] = newCar
            vinArray.append(newCar['vin'])
            return "Succesfully posted car with id: " + str(keyCounter), 201

    def put(self):
        return "Update is not allowed on this page", 400

    def delete(self):
        return "Delete is not allowed on this page", 400