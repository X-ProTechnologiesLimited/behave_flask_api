# COUNTRY_MANAGER_APPLICATION

This project is a demo for flask API and behave automated framework deployed on Docker
The project also support integration with Jenkins Pipeline. The pipeline is designed to build the project, run
the behave functional unit test cases and run a performance test on the APIs for a minute.

The API support documentation can be found at :- 

<https://documenter.getpostman.com/view/3312326/SVYnSgAS?version=latest#a4860551-fd24-838e-f195-1f2743764571>

## Runing locally (not containerised)
### Prerequisites for local run
1. Install python3 following the instructions from `https://www.python.org/downloads/`
2. Clone the git repository - `git clone https://github.com/X-ProTechnologiesLimited/country_manager.git`
3. Install pip tool and then install prerequistes `RUN pip3 install -r requirements.txt`
4. The application can be started with a fresh Database or existing
5. To start with fresh database - script `sh repo_root/utils/start_app.sh Y`
6. To start with existing database - script `sh repo_root/utils/start_app.sh N`
7. To start the behave tests - script `sh repo_root/utils/run_behave_tests.sh`
8. To shutdown the application - script `sh repo_root/utils/shutdown.sh`

Note: The logs of the application can be found at `repo_root/logs` directory

## Runing on Docker (Containerised)
1. Clone the git repository
2. Start the docker container with command `sh repo_root/build.sh` using the appropriate usage
flags mentioned below
3. To start the application within container without running the tests `build.sh --no-test`
Use optional `--d` flag to start application container in background
4. To start the application within container and run functional and performance test `build.sh --run-test`
5. To start the application within container without running the tests, but loading sample data `build.sh --load`
Use optional `--d` flag to start application container in background.
6. To start from the docker hub image, use the script `deploy.sh`. Use the optional flag `--no-pull` to run the
preloaded images for the applications

## Building in Jenkins Pipeline
1. The project is designed to work on both local Jenkins as well as Dockerised Jenkins.
For dockerised Jenkins, please refer to either `https://jenkins.io/doc/book/installing/` OR 
`https://hub.docker.com/r/jenkinsci/blueocean/`
2. The file `<repo_root>/Jenkinsfile` creates the pipeline and builds it automatically and
run the behave functional unit test case and Jmeter Performance tests.

### Notes
Linux
Yum install docker
systemctl start docker
Sudo chmod 666 /var/run/docker.sock
docker run -v /var/run/docker.sock:/var/run/docker.sock --rm -d --network="host" -p 8080:8080 jenkinsci
/blueocean

## Test Results and Logs

### Local and Container Test Runs
The tests are run and reports are automatically generated in html
format. 
1. Functional - Allure Format
2. Performance - Jmeter Apache Dashboard

Note: For Container Run, the reporting is done by a separate container automatically and reports
are generated in a separate http server and can be accessed at `http://localhost:8080/test_run_reports/`

The application logs are found in `<repo_root>/logs` directory. Even if the application is running
within container, the logs are mounted in the local host in the same directory.

### Jenkins Run
1. The results would be available on the Jenkins build dashboard for both Functional and Performance Test
2. The logs would be available in the Test-Artifact Section for the build

### Jenkins Dashboard - Running CSS and Javascript
By default the performance dashboard might not show the CSS content due to default Jenkins Security
Policy. Perform the following actions once Jenkins Starts Up before running the builds
1. Manage Jenkins->
2. Manage Nodes->
3. Click settings(gear icon)->
4. click Script console on left and type in the following command:

`System.setProperty("hudson.model.DirectoryBrowserSupport.CSP", "")`

and Press Run. If you see the output as 'Result:' below "Result" header then the protection disabled. 
Re-Run your build and you can see that the new HTML files archived will have the CSS enabled.


