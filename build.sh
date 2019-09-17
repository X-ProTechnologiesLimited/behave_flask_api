#!/bin/bash
. utils/app_run.config && export $(cut -d= -f1 utils/app_run.config)
cp utils/Dockerfile.local Dockerfile.local

#Setting up the flags for the Dockerfile
if [[ $1 == "--no-test" ]];then
  echo 'ENTRYPOINT ["utils/start_app.sh", "Y"]' >> Dockerfile.local
elif [[ $1 == "--load" ]];then
  echo 'ENTRYPOINT ["utils/start_app.sh", "Y", "--load-data"]' >> Dockerfile.local
elif [[ $1 == "--run-test" ]];then
  echo 'ENTRYPOINT ["utils/start_app.sh", "Y", "local"]' >> Dockerfile.local
else
  printf "Please use correct flags for either starting container with or without running tests....\n"
  printf "Usage: \n"
  printf "build.sh --no-test : [This will start the application. Use optional --d flag to start container in background]\n"
  printf "build.sh --load : [This will start the application and load sample data. Use optional --d flag to start container in background]\n"
  printf "build.sh --run-test : [This will start the application and run the behave unit tests and performance tests]\n"
  exit
fi

#Building the Image
docker build -f Dockerfile.local --tag=country_app .

#Running the Container

if [[ $2 == "--d" ]];then
  printf "\nStarting the Application in Detached mode in Background\n"
  docker run --rm -it --name country_api -v $PWD/logs:/app/logs --name country_api -p $FLASK_RUN_PORT:$FLASK_RUN_PORT -d -it country_app /bin/bash
elif [[ $1 == "--run-test" ]];then
  printf "\nStarting the Application\n"
  docker run --rm -it --name country_api -v $PWD/logs:/app/logs --name country_api -p $FLASK_RUN_PORT:$FLASK_RUN_PORT -it country_app /bin/bash
  printf "\nNow Starting the Reporting Container...\n"
  printf "\nReports will be available at http://localhost:8080/test_run_reports/\n"
  docker build -f utils/Dockerfile.reports --tag=http_reporting .
  docker run --rm -it --name http_reporter -p 8080:7000 http_reporting
else
  printf "\nStarting the Application\n"
  docker run --rm -it --name country_api -v $PWD/logs:/app/logs --name country_api -p $FLASK_RUN_PORT:$FLASK_RUN_PORT -it country_app /bin/bash
fi
