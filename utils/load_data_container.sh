containerid=$(docker ps | grep country_app | awk -F ' ' '{print $1}')
docker exec -it $containerid sqlite3 /app/lib/db.sqlite ".mode csv" ".import /app/utils/preload_country.csv country" 2>/dev/null
