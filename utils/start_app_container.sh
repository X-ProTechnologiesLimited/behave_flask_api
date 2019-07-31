#!/usr/bin/env bash
filename=country_app_`date +%d%m%Y%H%M%S`.log
mkdir -p /app/logs
echo "Starting the Country App..."
echo "Starting the Country App..." >> /app/logs/$filename
echo
if [ "$1" = "Y" ]
then
    rm -rf /app/lib/db.sqlite
    python /app/initialise_db.py
    echo "Created new database for application..."
    echo "Created new database for application..." >> /app/logs/$filename
    export FLASK_APP=/app/lib/
    export FLASK_DEBUG=0
    python -m flask run --host=0.0.0.0 >> /app/logs/$filename 2>&1 &
elif [ "$1" = "N" ]
then
    echo "Using the existing database..."
    echo "Using the existing database..." >> /app/logs/$filename
    export FLASK_APP=/app/lib/
    export FLASK_DEBUG=0
    python -m flask run --host=0.0.0.0>> /app/logs/$filename 2>&1 &
else
    echo "Error: No Database Creation option specified.."
    echo "usage ./app_run.sh <Y/N>"
fi

echo "Application Started Successfully"

sleep 5

# Run the automated behave test suite
echo "Starting the Automated Test Suite..."
echo
behave tests

# For Development and Debug Purposes, to keep the container running, uncomment the following line
#tail -200f /app/logs/$filename
