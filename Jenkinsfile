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
	    sh "behave --junit tests"
            junit "reports/*.xml"
            sh "ls /logs"
            sh "touch /app/logs/* && ls /app/logs"
            sh "cp /app/logs/* ${WORKSPACE}"
            archiveArtifacts '*.log'
            }
}
    stage ("Cleanup") {
            cleanWs()
        }

}


