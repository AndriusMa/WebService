import requests

class DannoService:
    def __init__(self):
        self.url = "http://external:9999/"
        # self.url = "http://localhost:80/"

    def get_all_movies(self):
        movies = []
        try:
            request = requests.get(self.url + 'movies')
            requests.RequestException()
            jsonMovies = request.json()
            body = jsonMovies

            for obj in body:
                movies.append(obj)
            return movies

        except requests.exceptions.RequestException as e:
            return "Movie service is down"

    def get_movie(self, movie_id):
        try:
            request = requests.get(self.url + 'movies/' + str(movie_id))
            requests.RequestException()
            jsonMovies = request.json()
            movie = jsonMovies
            return movie

        except requests.exceptions.RequestException as e:
            return "Movie service is down"
