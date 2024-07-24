#!/bin/sh

docker ps -a | grep gitlab | awk '{print $1}' | xargs -I{} docker stop {}
docker ps -a | grep gitlab | awk '{print $1}' | xargs -I{} docker rm {}
#docker images -a | grep gitlab | awk '{print $3}' | xargs -I{} docker rmi {}
docker system prune
