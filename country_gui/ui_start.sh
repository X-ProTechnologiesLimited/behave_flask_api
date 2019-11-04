#!/usr/bin/env bash
filestamp=`date +%H%M%S`
filename=country_ui.log
get_project_dir() { # Gets the root directory of the repository
    cd "${BASH_SOURCE[0]%*/*}/.." && pwd
}
if [[ $CONTAINERISED != "true" ]] ; then
    PROJECT_DIR=$(get_project_dir)
else
    PROJECT_DIR="/app"
fi

mkdir -p $PROJECT_DIR/logs
echo "Starting the Country Manager UI..."
echo "Starting the Country Manager UI..." >> $PROJECT_DIR/logs/$filename
echo
source $PROJECT_DIR/ui_run.config && export $(cut -d= -f1 $PROJECT_DIR/ui_run.config)
python3 -m flask run --host=0.0.0.0 --port=15000 >> $PROJECT_DIR/logs/$filename 2>&1 &

echo "Container for Country_UI Started successfully. Country_App API is ready to serve http requests now...."
    echo "To Shutdown Container, press Ctrl+C AND run /utils/shutdown.sh (For Standalone and Detached Containers)"
    trap printout SIGINT
    printout() {
       echo ""
       echo "Shutting Down Container..User Interrupted Container"
       sleep 5
       exit
    }
    while true ; do continue ; done
