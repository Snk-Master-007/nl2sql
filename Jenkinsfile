pipeline {
    agent any

    stages {
        stage('Trigger Test') {
            steps {
                script {
                    sh 'curl http://127.0.0.1:8000'
                }
            }
        }
    }
}