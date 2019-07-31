# behave_flask_app

This project is a demo for flask API and behave automated framework deployed on Docker
The API support documentation can be found at :- 

<https://documenter.getpostman.com/view/3312326/SVYnSgAS?version=latest#a4860551-fd24-838e-f195-1f2743764571>

## Runing locally (not containerised)
1. Clone the git repository
2. The application can be started with a fresh Database or existing
3. To start with fresh database - script `sh repo_root/utils/start.sh Y`
To start with existing database - script `sh repo_root/utils/start.sh N`
4. To start the behave tests - script `sh repo_root/utils/run_behave_tests.sh`
5. To shutdown the application - script `sh repo_root/utils/shutdown.sh`

Note: The logs of the application can be found at `repo_root/logs` directory

## Runing on Docker (Containerised)
1. Clone the git repository
2. Start the docker container with command `sh repo_root/build_container.sh`
This should build the image on container, start the container and run the automated
behave test suite.
3. The docker container can be accessed for logs and file systems in the
conventional way of `docker exec -it <container_id> /bin/bash` where the <container_id>
can be obtained by command `docker ps` once the container is started and
kept running

Note: For keeping the container running for debug or manual testing purposes:-

Uncomment the following line in script `repo_root/utils/start_app_container.sh`

`tail -200f /app/logs/$filename`