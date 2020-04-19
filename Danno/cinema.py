from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

id_register = [ '10.5240/843E-C238-7F61-DDFC-F427-9', # THE GODFATHER
                '10.5240/31CA-F962-3A40-18BD-BFA5-7', # SHAWSHANK REDEMPTION
                '10.5240/A91C-90AE-1F45-6460-F6AC-U', # GREEN MILE
                '10.5240/29E6-2D4B-B704-2B69-441F-8', # TITANIC
                '10.5240/0EF3-54F9-2642-0B49-6829-R', # INCEPTION
                '10.5240/5C04-098C-6377-F2C5-51B2-J', # JOKER
                '10.5240/9AEF-D367-C3C0-A851-7D02-7', # INTOUCHABLES
                '10.5240/B298-00A2-FE19-FF89-8CDD-Z', # SEVENSAMURAI
                ]

movie_counter = len(id_register)

movies = {  0: {'id': 0, 'title': 'The Godfather',            'eidr': id_register[0], 'year': '1972', 'director': 'Francis Ford Coppola'}, 
            1: {'id': 1, 'title': 'The Shawshank Redemption', 'eidr': id_register[1], 'year': '1994', 'director': 'Frank Darabont'},
            2: {'id': 2, 'title': 'The Green Mile',           'eidr': id_register[2], 'year': '1999', 'director': 'Frank Darabont'},
            3: {'id': 3, 'title': 'Titanic',                  'eidr': id_register[3], 'year': '1997', 'director': 'James Cameron'},
            4: {'id': 4, 'title': 'Inception',                'eidr': id_register[4], 'year': '2010', 'director': 'Christopher Nolan'},
            5: {'id': 5, 'title': 'Joker',                    'eidr': id_register[5], 'year': '2019', 'director': 'Todd Phillips'},
            6: {'id': 6, 'title': 'Intouchables',             'eidr': id_register[6], 'year': '2011', 'director': 'Eric Toledano'},
            7: {'id': 7, 'title': 'Shichinin no samurai',     'eidr': id_register[7], 'year': '1954', 'director': 'Akira Kurosawa'}
            }

class Movie(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title',    type = str, required = True, location = 'json', help = "Title must be specified")
        self.reqparse.add_argument('eidr',     type = str, required = True, location = 'json', help = "EIDR must be specified")
        self.reqparse.add_argument('year',     type = str, required = True, location = 'json', help = "Year must be specified")
        self.reqparse.add_argument('director', type = str, required = True, location = 'json', help = "Director must be specified")

    def get(self):
        repertoire = []
        for movie in movies.values():
            repertoire.append(movie)
        if len(repertoire) is 0:
            return 'Nothing to watch', 404
        else:
            return repertoire, 200

    def post(self):
        args = self.reqparse.parse_args()
        global movie_counter
        movie_counter += 1
        new_movie = {'id': movie_counter, 'title': args['title'], 'eidr': args['eidr'], 'year': args['year'], 'director': args['director'] }
        if args['eidr'] in id_register:
            movie_counter -= 1
            return 'Every movie has its unique EIDR', 403
        else:
            movies[new_movie['id']] = new_movie
            id_register.append(new_movie['eidr'])
            return 'Movie "'+new_movie['title']+'" succesfully added with ID '+str(movie_counter), 201
    
class MovieById(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title',    type = str, required = True, location = 'json', help = "Title must be specified")
        self.reqparse.add_argument('eidr',     type = str, required = True, location = 'json', help = "EIDR must be specified")
        self.reqparse.add_argument('year',     type = str, required = True, location = 'json', help = "Year must be specified")
        self.reqparse.add_argument('director', type = str, required = True, location = 'json', help = "Director must be specified")
        
    def get(self, id):
        if id not in movies:
            return 'There is no movie with the given ID', 404
        else:
            return movies[id], 200

    def put(self, id):
        if id not in movies:
            return 'There is no movie with the given ID', 404
        else:
            args = self.reqparse.parse_args()
            temp_eidr = movies[id].get('eidr')
            id_register.remove(temp_eidr)
            changed_movie = {'id': id, 'title': args['title'], 'eidr': args['eidr'], 'year': args['year'], 'director': args['director'] }
            if args['eidr'] in id_register:
                return 'Every movie has its unique EIDR', 403
            else:
                movies[id] = changed_movie
                id_register.append(changed_movie['eidr'])
                return 'Movie "'+changed_movie['title']+'" succesfully changed with ID '+str(id), 200
    
    def delete(self, id):
        if id not in movies:
            return 'There is no movie with the given ID', 404
        else:
            movies.pop(id)
            return 'Movie with ID '+str(id)+' succesfully deleted', 200
    
class Home(Resource):
    def get(self):
        pass

api.add_resource(Home, '/')
api.add_resource(Movie, '/movies')
api.add_resource(MovieById, '/movies/<int:id>')

if __name__ == '__main__':
    app.run(host = "0.0.0.0", debug = True, port = 9999)