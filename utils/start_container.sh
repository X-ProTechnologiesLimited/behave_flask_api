#!/usr/bin/env bash
filestamp=`date +%H%M%S`
filename=country_app.log
mkdir -p /app/logs
mkdir -p /app/logs/test_results/functional
mkdir -p /app/logs/test_results/performance
echo "Starting the Country App..."
echo "Starting the Country App..." >> /app/logs/$filename
echo
source /app/utils/app_run.config && export $(cut -d= -f1 /app/utils/app_run.config)
if [ "$1" = "Y" ]
then
    source /app/utils/app_run.config && export $(cut -d= -f1 /app/utils/app_run.config)
    rm -rf /app/lib/db.sqlite
    python /app/initialise_db.py
    echo "Created new database for application..."
    echo "Created new database for application..." >> /app/logs/$filename
    python -m flask run --host=0.0.0.0 >> /app/logs/$filename 2>&1 &
    if [[ $2 == "--load-data" ]]
    then
       echo "Loading Preloaded Country Data to Container..."
       sleep 5
       sqlite3 /app/lib/db.sqlite ".mode csv" ".import /app/utils/preload_country.csv country" 2>/dev/null
    else
       echo "Using Empty Database For Container"
    fi
     
elif [ "$1" = "N" ]
then
    source /app/utils/app_run.config && export $(cut -d= -f1 /app/utils/app_run.config)
    echo "Using the existing database..."
    echo "Using the existing database..." >> /app/logs/$filename
    python -m flask run --host=0.0.0.0>> /app/logs/$filename 2>&1 &

elif [ "$1" = "Jenkins" ]
then
    rm -rf /app/lib/db.sqlite
    python /app/initialise_db.py
    echo "Created new database for application..."
    echo "Created new database for application..." >> /app/logs/$filename
    export FLASK_APP=/app/lib/
    export FLASK_DEBUG=0
    export FLASK_RUN_PORT=5000
    python -m flask run --host=0.0.0.0 >> /app/logs/$filename 2>&1 &
else
    echo "Error: No Database Creation option specified.."
    echo "usage ./app_run.sh <Y/N>"
fi

echo "Wating for the application to initialise...."
sleep 10
echo "Application Started Successfully"
if [[ "$2" == 'local' ]]
then
    source /app/utils/app_run.config && export $(cut -d= -f1 /app/utils/app_run.config)
    echo "Starting Tests in Container....."
    echo "Keeping the Container running while executing the tests...."
    # Run the automated behave test suite
    echo "Starting the Automated Test Suite..."
    echo "--------------------------------------------------------------------------------"
    echo "Executing Only ADD GET and UPDATE Scenarios now...Skipping DELETE Scenarios"
    echo "--------------------------------------------------------------------------------"
    behave --tags=~@delete --no-skipped -f allure_behave.formatter:AllureFormatter -o /app/logs/allure_output_"$filestamp" tests
    echo "--------------------------------------------------------------------------------"
    echo "Executing only DELETE Scenarios now....Skipping ADD/GET/UPDATE Scenarios"
    echo "--------------------------------------------------------------------------------"
    behave --tags=@delete --no-skipped -f allure_behave.formatter:AllureFormatter -o /app/logs/allure_output_"$filestamp" tests
    echo "Waiting for the container to finish the behave tests...."
    sleep 5
    allure generate /app/logs/allure_output_"$filestamp" --clean -o allure_report_"$filestamp"
    cp -R allure_report_"$filestamp" /app/logs/test_results/functional/
    echo "Now starting Performance Tests using Jmeter...."
    jmeter -n -t /app/tests/load_tests/Country_API.jmx -l /app/logs/"$filename"_"$filestamp"_jmeter.log -e -o /app/logs/test_results/performance/performance_output_$filestamp
    echo "Finishing off the Performance Tests..."
    echo "Generating the Test reports........"
    echo "Shutting down container....."
else
    echo "Container for Country_App Started successfully. Country_App API is ready to serve http requests now...."
    echo "To Shutdown Container, press Ctrl+C  OR run /utils/shutdown_container.sh"
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
#tail -200f /app/logs/$filename
