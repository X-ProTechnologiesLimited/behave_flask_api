pipeline {
  agent { docker { image 'python:3.7.2' } }
  stages {
    stage('build') {
      steps {
        sh 'cd ../behave_flask_api_master'
	sh 'build_container.sh'
      }
    }
  }
}
