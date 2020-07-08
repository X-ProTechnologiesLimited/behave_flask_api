docker build -f utils/Dockerfile.ui --tag=xprotech/country_ui .
docker build -f utils/Dockerfile.local --tag=xprotech/country_api .
docker push xprotech/country_api
docker push xprotech/country_ui
