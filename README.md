To build for first time: docker-compose up --build -d

To build after first time: docker build -t *your_container_name*:latest

To run: docker run -it  *your_directory*_web

Service can be reached at /cars .

This service can:

-Create a car

-Delete a car

-Get car list

-Update a car

If you want to reach a specific car, use /cars/*car_number*
