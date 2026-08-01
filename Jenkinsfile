pipeline {
    agent any

    stages {
        stage('Login Test') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-credentials-id',
                    usernameVariable: 'USER',
                    passwordVariable: 'PASS'
                )]) {
                    bat '''
                    echo %PASS% | docker login -u %USER% --password-stdin
                    docker info
                    '''
                }
            }
        }
    }
}
