#!/bin/bash
. utils/app_run.config && export $(cut -d= -f1 utils/app_run.config)
app_run(){
printf "Starting the Country App API services..\n"
docker run --rm -it --name country_manager -v $PWD/logs:/app/logs \
       --name country_manager -p $FLASK_RUN_PORT:$FLASK_RUN_PORT \
       -d -it xprotech/country_api:latest /bin/bash -c "utils/start_app.sh Y --load-data"
sleep 5
printf "Starting the Country App UI services..\n"
docker run --rm -it --name country_gui -v $PWD/logs:/app/logs \
       --name country_gui --add-host $D_HOST:$D_IP \
       -p $FLASK_RUN_PORT_UI:$FLASK_RUN_PORT_UI -d -it xprotech/country_ui:latest /bin/bash \
       -c "./ui_start.sh"
}
if [[ $1 == '--no-pull' ]];
then
   printf "Country Applications starting..\n"
   printf "No-pull flag used; not pulling from docker hub..\n"
   app_run;
else
   printf "Country Applications starting..\n"
   printf "Pulling latest images from docker hub..\n"
   printf "Pulling latest image for Country App API services..\n"
   docker pull xprotech/country_api
   printf "Pulling latest image for Country App UI services..\n"
   docker pull xprotech/country_ui
   app_run;
fi
