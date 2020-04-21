#!/bin/bash
echo "Stopping services"
docker rm external -f
docker rm andriusma_service -f
docker rm danno_service -f
echo "Removing local network"
docker network rm ws_bridge
docker network rm webservice2nd_ws_bridge
echo "Clearing empty images"
docker rmi $(docker images --filter dangling=true -q --no-trunc)
echo "Done"