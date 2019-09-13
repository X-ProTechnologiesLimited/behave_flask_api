node() {
    def myImg
    stage ("Build image") {
        // download the dockerfile to build from
        git 'https://github.com/X-ProTechnologiesLimited/behave_flask_api.git'

        // build our docker image
        myImg = docker.build 'my-image:snapshot'
    }
    stage ("Run Build") {
        myImg.inside('-v $WORKSPACE:/logs -u root') {
            sh 'echo Waiting for Container to start before tests && sleep 10'
	    sh 'echo Clearing old reports...'
	    sh "rm -rf reports/*.xml"
	    sh """
            	echo "Starting the Automated Test Suite..."
		echo "--------------------------------------------------------------------------------"
		echo "Executing Only ADD GET and UPDATE Scenarios now...Skipping DELETE Scenarios"
		echo "--------------------------------------------------------------------------------"
		behave --tags=~@delete --no-skipped --junit tests
		echo "--------------------------------------------------------------------------------"
		echo "Executing only DELETE Scenarios now....Skipping ADD/GET/UPDATE Scenarios"
		echo "--------------------------------------------------------------------------------"
		behave --tags=@delete --no-skipped --junit tests
                echo "--------------------------------------------------------------------------------"
                echo "Executing Performance Tests now for 1 minute....Using Jmeter"
                jmeter -n -t tests/load_tests/Country_API.jmx -l ${WORKSPACE}/country_app_load.log -e -o ${WORKSPACE}/output
	      """
            publishHTML (target: [
            allowMissing: true,
            alwaysLinkToLastBuild: false,
            keepAll: true,
            reportDir: "${WORKSPACE}/output",
            reportFiles: "index.html",
            reportName: "Performance"
            ])
            junit "reports/*.xml"
            sh "ls /logs"
            sh "touch /app/logs/* && ls /app/logs"
            sh "cp /app/logs/* ${WORKSPACE}"
            archiveArtifacts '*.log,*.html'
            }
}
    stage ("Cleanup") {
            cleanWs()
        }

}


