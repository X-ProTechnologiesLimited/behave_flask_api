#!/bin/bash
docker rm `docker ps -a | grep country_api | awk -F ' ' '{print $1}'`
. utils/app_run.config && export $(cut -d= -f1 utils/app_run.config)
if [[ $1 == "--run-tests" ]]
then
   #Build the Docker Image(Replaces any current image)
   echo "Setting the Dockerfile for the Local Containers"
   echo "Building the Docker Image for Country Application"
   echo
   docker build -f utils/Dockerfile.local --tag=country_app .
   #Start the docker container for building the rest api application and do the test
   echo "Starting the Container for Country App..."
   docker run -v $PWD/logs:/app/logs --name country_api -p $FLASK_RUN_PORT:$FLASK_RUN_PORT -it country_app /bin/bash
elif [[ $1 == "--no-tests" ]]
then
   if [[ $2 == "--load-data" ]]
   then
        echo "Building the Docker Image for Country Application"
        docker build -f utils/Dockerfile.preloaded --tag=country_app .
   else
        echo "Building the Docker Image for Country Application"
        docker build -f utils/Dockerfile.tests --tag=country_app .
   fi
        #Start the docker container for building the rest api application and do the test
   if [[ $2 == "--detached" ]]
   then
       echo "Starting the Container for Country App in detached mode"
       docker run -v $PWD/logs:/app/logs --name country_api -p $FLASK_RUN_PORT:$FLASK_RUN_PORT -d -it country_app /bin/bash
   else
       echo "Starting the Container for Country App..."
       docker run -v $PWD/logs:/app/logs --name country_api -p $FLASK_RUN_PORT:$FLASK_RUN_PORT -it country_app /bin/bash
   fi
else
   echo "Please use correct flags for either starting container with or without running tests...."
   echo "Usage: "
   echo ./build_container.sh --no-tests : [This will only start the country_app API in dockerised container]
   echo ./build_container.sh --no-tests --detached  : [This will only start the country_app API in dockerised container in detached mode]
   echo ./build_container.sh --run-tests : [This will start the country_app API in container and run the Behave tests]
   echo
fi
