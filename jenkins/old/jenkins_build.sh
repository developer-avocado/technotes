#!/bin/sh

# Create jenkins network

docker network create jenkins

# Create docker image

docker images | grep my-jenkins
if [ $? -eq 0 ]; then 
  echo "Docker image has already been created."
else
  echo "Create docker image."
  sudo docker build -t my-jenkins:2.440.3-1 .
fi

# Create docker container

docker ps -a | grep my-jenkins

if [ $? -eq 0 ]; then
  echo "Docker container has already been created."
else
  echo "Create docker container"
  sudo docker run \
  --name my-jenkins \
  --restart=on-failure \
  --detach \
  --network jenkins \
  --env DOCKER_HOST=tcp://docker:2376 \
  --env DOCKER_CERT_PATH=/certs/client \
  --env DOCKER_TLS_VERIFY=1 \
  --publish 8080:8080 \
  --publish 50000:50000 \
  --volume jenkins-data:/var/jenkins_home \
  --volume jenkins-docker-certs:/certs/client:ro \
  my-jenkins:2.440.3-1
fi

# Get the password
echo "password: "
sudo docker exec my-jenkins cat /var/jenkins_home/secrets/initialAdminPassword

# Paste the password
echo "Access http://localhost:8080/ and paste the password"
read -p "When finished, enter y" ret

# Install jenkins plugins
if [ $ret = "y" ]; then
  echo "Click [Intall suggested plugins]"
  read -p "When finished, enter y" ret
else
  echo "Finish setup of jenkins"
  exit
fi

# Create First Admin User
if [ $ret = "y" ]; then
  echo "Click [Create First Admin User]"
  read -p "When finished, enter y" ret
else
  echo "Finish setup of jenkins"
  exit
fi

# Proceed 
echo "Click [Save and Continue]"
echo "Click [Save and Finish]"
echo "Click [Start using Jenkins]"

