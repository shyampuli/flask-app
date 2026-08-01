pipeline {
    agent any

    stages {
        stage('Docker Test') {
            steps {
                bat '''
                whoami
                docker context ls
                docker info
                docker login -u shyamprasad2310
                '''
            }
        }
    }
}
