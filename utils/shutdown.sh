#!/bin/bash
echo "Calling Shutdown..."
sleep 1
. app_run.config && export $(cut -d= -f1 app_run.config)
response=$(curl --silent "http://localhost:$FLASK_RUN_PORT/quit")
if [ "$response" == "Appliation shutting down..." ];
then
  printf "\nApplication shutdown successful\n"
else
 printf "\nShutdown Error: No Flask Application Running\n"
fi

printf "\nChecking Container.....\n"

if [[ $(docker ps | grep country_app | awk -F ' ' '{print $1}') ]]; then
        docker kill `docker ps | grep country_app | awk -F ' ' '{print $1}'`
        printf "\nContainer Stopped Successfully\n"
else
        printf "\nNo Container is there for Country_App\n"
fi
