#!/bin/bash
echo "Calling Shutdown..."
sleep 1
. app_run.config && export $(cut -d= -f1 app_run.config)
response=$(curl --silent "http://localhost:$FLASK_RUN_PORT/quit")
if [ "$response" == "Appliation shutting down..." ];
then
  echo
  echo "Application shutdown successful"
  echo
else
 echo
 echo "Shutdown Error: No Flask Application Running"
 echo
fi
