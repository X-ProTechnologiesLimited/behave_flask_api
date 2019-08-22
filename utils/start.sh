#!/bin/bash
filestamp=`date +%H%M%S`
filename=country_app.log
mkdir -p ../logs
mv ../logs/country_app.log ../logs/country_app_$filestamp.log
touch ../logs/country_app_$filestamp.log
gzip ../logs/country_app_$filestamp.log

echo "Started the Country App..."
echo "Started the Country App..." >> ../logs/$filename
echo
. app_run.config && export $(cut -d= -f1 app_run.config)
if [ "$1" = "Y" ]
then
    rm -rf ../lib/db.sqlite
    python3 ../initialise_db.py
    echo "Created new database for application..."
    echo "Created new database for application..." >> ../logs/$filename
    python3 -m flask run >> ../logs/$filename 2>&1 &
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
    python3 -m flask run >> ../logs/$filename 2>&1 &
else
    echo "Error: No Database Creation option specified.."
    echo "usage ./app_run.sh <Y/N>"
fi

echo
