#!/bin/sh

docker ps -a | grep jenkins | awk '{print $1}' | xargs docker stop
docker ps -a | grep jenkins | awk '{print $1}' | xargs docker rm


