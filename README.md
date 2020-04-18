<<<<<<< HEAD
# Car Movies WebService

Possibilities:
- Get all records of the cars that starred in all or one movie that are currently shown at the theatre
- Create a record for a car that is starring in movie or movies
- Update information about the car that is starring in movie or movies
- Delete a record of car that is starring in movie or movies

Build and start:  ./run.sh
Stop:             ./stop.sh

View:  localhost:80/<PATH>
<PATH> = /cars/movies
         /cars/<car_id>/movies
         /cars
=======
To build for first time: docker-compose up --build -d

To build after first time: docker build -t *your_container_name*:latest .

To run: docker run -it  *your_directory*_web

Service can be reached at /cars .

This service can:

-Create a car

-Delete a car

-Get car list

-Update a car

If you want to reach a specific car, use /cars/*car_number*
>>>>>>> 6121de2b598be54987908c4710896fd54d57f102
