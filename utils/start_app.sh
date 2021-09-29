#!/usr/bin/env bash
filestamp=`date +%H%M%S`
filename=country_app.log
get_project_dir() { # Gets the root directory of the repository
    cd "${BASH_SOURCE[0]%*/*}/.." && pwd
}
if [[ $CONTAINERISED != "true" ]] ; then
    PROJECT_DIR=$(get_project_dir)
else
    PROJECT_DIR="/app"
fi

mkdir -p $PROJECT_DIR/logs
mkdir -p $PROJECT_DIR/logs/test_results/functional
mkdir -p $PROJECT_DIR/logs/test_results/performance
echo "Starting the Country App..."
echo "Starting the Country App..." >> $PROJECT_DIR/logs/$filename
echo
source $PROJECT_DIR/utils/app_run.config && export $(cut -d= -f1 $PROJECT_DIR/utils/app_run.config)
if [ "$1" = "Y" ]
then
    source $PROJECT_DIR/utils/app_run.config && export $(cut -d= -f1 $PROJECT_DIR/utils/app_run.config)
    rm -rf $PROJECT_DIR/lib/db.sqlite
    python3 $PROJECT_DIR/initialise_db.py
    echo "Created new database for application..."
    echo "Created new database for application..." >> $PROJECT_DIR/logs/$filename
    python3 -m flask run --host=0.0.0.0 >> $PROJECT_DIR/logs/$filename 2>&1 &
    if [[ $2 == "--load-data" ]]
    then
       echo "Loading Preloaded Country Data to Container..."
       sleep 5
       sqlite3 $PROJECT_DIR/lib/db.sqlite ".mode csv" ".import $PROJECT_DIR/utils/preload_country.csv country" 2>/dev/null
       sqlite3 $PROJECT_DIR/lib/db.sqlite ".mode csv" ".import $PROJECT_DIR/utils/preload_cities.csv citydata" 2>/dev/null
    else
       echo "Using Empty Database For Container"
    fi
     
elif [ "$1" = "N" ]
then
    source $PROJECT_DIR/utils/app_run.config && export $(cut -d= -f1 $PROJECT_DIR/utils/app_run.config)
    echo "Using the existing database..."
    echo "Using the existing database..." >> $PROJECT_DIR/logs/$filename
    python3 -m flask run --host=0.0.0.0>> $PROJECT_DIR/logs/$filename 2>&1 &

elif [ "$1" = "Jenkins" ]
then
    rm -rf $PROJECT_DIR/lib/db.sqlite
    python3 $PROJECT_DIR/initialise_db.py
    echo "Created new database for application..."
    echo "Created new database for application..." >> $PROJECT_DIR/logs/$filename
    export FLASK_APP=$PROJECT_DIR/lib/
    export FLASK_DEBUG=0
    export FLASK_RUN_PORT=5000
    python3 -m flask run --host=0.0.0.0 >> $PROJECT_DIR/logs/$filename 2>&1 &
else
    echo "Error: No Database Creation option specified.."
    echo "usage ./start_app.sh <Y/N>"
    exit
fi

echo "Wating for the application to initialise...."
sleep 10
echo "Application Started Successfully"
if [[ "$2" == 'local' ]]
then
    source $PROJECT_DIR/utils/app_run.config && export $(cut -d= -f1 $PROJECT_DIR/utils/app_run.config)
    echo "Starting Tests in Container....."
    echo "Keeping the Container running while executing the tests...."
    # Run the automated behave test suite
    echo "Starting the Automated Test Suite..."
    echo "--------------------------------------------------------------------------------"
    echo "Executing Only ADD GET and UPDATE Scenarios now...Skipping DELETE Scenarios"
    echo "--------------------------------------------------------------------------------"
    behave --tags=~@delete --no-skipped -f allure_behave.formatter:AllureFormatter -o $PROJECT_DIR/logs/allure_output_"$filestamp" tests
    echo "--------------------------------------------------------------------------------"
    echo "Executing only DELETE Scenarios now....Skipping ADD/GET/UPDATE Scenarios"
    echo "--------------------------------------------------------------------------------"
    behave --tags=@delete --no-skipped -f allure_behave.formatter:AllureFormatter -o $PROJECT_DIR/logs/allure_output_"$filestamp" tests
    echo "Waiting for the container to finish the behave tests...."
    sleep 5
    allure generate $PROJECT_DIR/logs/allure_output_"$filestamp" --clean -o allure_report_"$filestamp"
    cp -R allure_report_"$filestamp" $PROJECT_DIR/logs/test_results/functional/
    echo "Now starting Performance Tests using Jmeter...."
    jmeter -n -t $PROJECT_DIR/tests/load_tests/Country_API.jmx -l $PROJECT_DIR/logs/"$filename"_"$filestamp"_jmeter.log -e -o $PROJECT_DIR/logs/test_results/performance/performance_output_$filestamp
    echo "Finishing off the Performance Tests..."
    echo "Generating the Test reports........"
    echo "Shutting down container....."
else
    echo "Container for Country_App Started successfully. Country_App API is ready to serve http requests now...."
    echo "To Shutdown Container, press Ctrl+C AND run /utils/shutdown.sh (For Standalone and Detached Containers)"
    trap printout SIGINT
    printout() {
       echo ""
       echo "Shutting Down Container..User Interrupted Container"
       sleep 5
       exit
    }
    while true ; do continue ; done
fi
# For Development and Debug Purposes, to keep the container running, uncomment the following line
#tail -200f $PROJECT_DIR/logs/$filename
