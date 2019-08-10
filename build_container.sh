#!/bin/bash
#Build the Docker Image(Replaces any current image)
echo "Building the Docker Image for Country Application"
echo
docker build --tag=country_app .
#Start the docker container for building the rest api application and do the test
echo "Starting the Container for Country App..."
docker run -v $PWD/logs:/app/logs -p 5000:5000 country_app
