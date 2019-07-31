if [[ $(docker ps | grep country_app | awk -F ' ' '{print $1}') ]]; then
	docker kill `docker ps | grep country_app | awk -F ' ' '{print $1}'`
	echo "Container Stopped Successfully"
else
	echo "No Container is there for Country_App"
fi
