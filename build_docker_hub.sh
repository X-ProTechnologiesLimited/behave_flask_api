docker build -f utils/Dockerfile.lite --tag=xprotech/country_ui .
docker build -f utils/Dockerfile.lite --tag=xprotech/country_api .
docker push xprotech/country_api
docker push xprotech/country_ui
