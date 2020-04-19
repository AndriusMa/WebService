#!/bin/bash
# Create custom local network
docker network create ws_bridge
# Run Danno19 Cinema WebService
cd Danno
docker-compose up --build -d
# Run AndriusMa Car WebService
cd ..
docker-compose up --build -d