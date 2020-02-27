"""
Car insurance service
Car (/car/<str:CarId>) ?
"""
from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

Cars = {0: {'id':0, 'vin':'whd2050041f241488', 'make':'nissan', 'model':'200sx', 'insurance':'yes'},
        1: {'id':1, 'vin':'wdd1458068d241987', 'make':'mazda', 'model':'mx-5', 'insurance':'yes'},
        2: {'id':2, 'vin':'wdd4580011e241548', 'make':'nissan', 'model':'350z', 'insurance':'no'},
        3: {'id':3, 'vin':'wfd2050069l241488', 'make':'nissan', 'model':'300zx', 'insurance':'no'},
        4: {'id':4, 'vin':'wed4870077a581488', 'make':'lexus', 'model':'sc400', 'insurance':'no'},
        5: {'id':5, 'vin':'wgd1080041l666488', 'make':'toyota', 'model':'celica', 'insurance':'yes'}
        };
keyCounter = 5
vinArray = ['whd2050041f241488', 'wdd1458068d241987', 'wdd4580011e241548', 
            'wfd2050069l241488', 'wed4870077a581488', 'wgd1080041l666488'
            ]

class Car(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('vin', type=str, required=True, location='json', help="Vin number must be provided")
        self.parser.add_argument('make', type=str, required=True, location='json', help="Make must be provided")
        self.parser.add_argument('model', type=str, required=True, location='json', help="Model must be provided")
        self.parser.add_argument('insurance', type=str, required=True, location='json', help="Insurance status must be provided")

    def get(self):
        allCars = []
        for car in Cars.values():
            allCars.append(car)
        if len(allCars) is 0:
            return "List is empty", 201
        else:
            return allCars, 200
    
    def post(self):
        args = self.parser.parse_args()
        global keyCounter
        keyCounter += 1
        newCar = {
            'id':keyCounter,
            'vin':args['vin'],
            'make':args['make'],
            'model':args['model'],
            'insurance':args['insurance']
        }
        if args['vin'] in vinArray:
            keyCounter -= 1
            return "vin number must be unique to the car", 400
        else:
            Cars[newCar['id']] = newCar
            vinArray.append(newCar['vin'])
            return "Succesfully posted car with id: " + str(keyCounter), 201

    def put(self):
        return "Update is not allowed on this page", 400

    def delete(self):
        return "Delete is not allowed on this page", 400

class CarById(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('vin', type=str, required=True, location='json', help="Vin number must be provided")
        self.parser.add_argument('make', type=str, required=True, location='json', help="Make must be provided")
        self.parser.add_argument('model', type=str, required=True, location='json', help="Model must be provided")
        self.parser.add_argument('insurance', type=str, required=True, location='json', help="Insurance status must be provided")

    def get(self, id):
        if id not in Cars:
            return "No car found by provided id", 404
        else:
            return Cars[id], 200
    
    def post(self, id):
        return "Posting is not allowed on this page", 400

    def put(self, id):
        if id not in Cars:
            return "Wrong car id provided", 404
        else:
            args = self.parser.parse_args()
            tempVin = Cars[id].get('vin')
            vinArray.remove(tempVin)
            updateCar = {
            'id':id,
            'vin':args['vin'],
            'make':args['make'],
            'model':args['model'],
            'insurance':args['insurance']
            }
            if args['vin'] in vinArray:
                return "vin number must be unique to the car", 400
            else:
                Cars[id] = updateCar
                vinArray.append(updateCar['vin'])
                return "Succesfully updated car with id: " + str(id), 200

    def delete(self, id):
        if id not in Cars:
            return "Wrong car id provided", 404
        else:
            Cars.pop(id)
            return "Succesfully deleted car with id: " + str(id), 200


class Home(Resource):
    def get(self):
        pass
    
api.add_resource(Home, '/')
api.add_resource(Car, '/cars')
api.add_resource(CarById, '/cars/<int:id>')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)