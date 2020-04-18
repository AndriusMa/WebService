from flask_restful import Resource, Api, reqparse
from data import Cars, keyCounter, vinArray
from DannoService import DannoService

class CarById(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('vin', type=str, required=True, location='json', help="Vin number must be provided")
        self.parser.add_argument('make', type=str, required=True, location='json', help="Make must be provided")
        self.parser.add_argument('model', type=str, required=True, location='json', help="Model must be provided")
        self.parser.add_argument('movies', type=str, required=True, location='json', help="At least one movie must be provided")


    def get(self, car_id):
        if id not in Cars:
            return "No car found by provided id", 404
        else:
            return Cars[car_id], 200
    
    def post(self, car_id):
        return "Posting is not allowed on this page", 400

    def put(self, car_id):
        if car_id not in Cars:
            return "Wrong car id provided", 404
        else:
            args = self.parser.parse_args()
            tempVin = Cars[car_id].get('vin')
            vinArray.remove(tempVin)
            updateCar = {
            'car_id':car_id,
            'vin':args['vin'],
            'make':args['make'],
            'model':args['model'],
            'movies':args['movies']
            }
            if args['vin'] in vinArray:
                return "vin number must be unique to the car", 400
            
            elif args['movies'] == "":
                return "At least one movie must be provided", 400

            else:
                movie_ids = args['movies'].split(',')
                movies = DannoService().get_all_movies()
                
                if movies == "Movie service is down":
                    return "Movie service is down", 503

                duplicates = []
                for movie_id in movie_ids:
                    try:                  
                        movies[int(movie_id)].get('movie_id')
                        for duplicate in duplicates:
                            if duplicate == int(movie_id):
                                return "Movie duplicates found in provided json", 400

                        duplicates.append(int(movie_id))
                        
                    except IndexError as e:
                        vinArray.append(tempVin)
                        return "At least one movie id is invalid or the json format is unrecognized", 400
                
                Cars[car_id] = updateCar
                vinArray.append(args['vin'])
                return "Succesfully updated car with id: " + str(car_id), 200

    def delete(self, car_id):
        if car_id not in Cars:
            return "Wrong car id provided", 404
        else:
            Cars.pop(car_id)
            return "Succesfully deleted car with id: " + str(car_id), 200
