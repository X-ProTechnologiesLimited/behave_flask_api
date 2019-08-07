node() {
    def myImg
    stage ("Build image") {
        // download the dockerfile to build from
        git 'https://github.com/X-ProTechnologiesLimited/behave_flask_api.git'

        // build our docker image
        myImg = docker.build 'my-image:snapshot'
    }
    stage ("Get Source") {
        // run a command to get the source code download
        myImg.inside('-v /home/git/repos:/home/git/repos') {
	    sh "rm -rf behave_flask_api_master*"
            sh "git clone https://github.com/X-ProTechnologiesLimited/behave_flask_api.git"
        }
    }
    stage ("Run Build") {
        myImg.inside() {
            sh "cd behave_flask_api/ && utils/start.sh Y  && utils/run_behave_tests.sh"
        }
    }
}
