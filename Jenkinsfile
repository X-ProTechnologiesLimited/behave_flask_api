pipeline {
  agent { docker { image 'python:3.7.2' } }
  stages {
    stage('build') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('test') {
      steps {
        sh 'utils/start.sh Y'
	sh 'utils/run_behave.sh
      }   
    }
  }
}
