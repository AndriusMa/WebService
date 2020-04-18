from flask import Flask
from flask_restful import Resource, Api, reqparse
from carById import CarById
from cars import Car
from allCarMovies import AllCarMovies
from allCarsAllMovies import AllCarsAllMovies

app = Flask(__name__)
api = Api(app)
    
api.add_resource(Car, '/cars')
api.add_resource(CarById, '/cars/<int:car_id>')
api.add_resource(AllCarsAllMovies, '/cars/movies')
api.add_resource(AllCarMovies, '/cars/<int:car_id>/movies')
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)