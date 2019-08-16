#!/usr/bin/env bash
filename=country_app_`date +%d%m%Y%H%M%S`.log
mkdir -p ../logs
echo "Started the Country App..."
echo "Started the Country App..." >> ../logs/$filename
echo
if [ "$1" = "Y" ]
then
    rm -rf ../lib/db.sqlite
    python ../initialise_db.py
    echo "Created new database for application..."
    echo "Created new database for application..." >> ../logs/$filename
    export FLASK_APP=../lib/
    export FLASK_DEBUG=0
    python -m flask run >> ../logs/$filename 2>&1 &
    if [ "$2" == "--load-data" ]
    then
       echo "Loading Preloaded Country Data...."
       echo "Loading Preloaded Country Data...." >> ../logs/$filename
       sqlite3 ../lib/db.sqlite ".mode csv" ".import preload_country.csv country"
       echo "Data Loaded Successfully..."
    else
       exit
    fi
elif [ "$1" = "N" ]
then
    echo "Using the existing database..."
    echo "Using the existing database..." >> ../logs/$filename
    export FLASK_APP=../lib/
    export FLASK_DEBUG=0
    python -m flask run >> ../logs/$filename 2>&1 &
else
    echo "Error: No Database Creation option specified.."
    echo "usage ./app_run.sh <Y/N>"
fi

echo
