pipeline {
    agent any

    stages {
        stage('Test Credential') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-credentials-id',
                        usernameVariable: 'USER',
                        passwordVariable: 'PASS'
                    )
                ]) {

                    bat '''
                    echo USER=%USER%
                    powershell -Command "$env:PASS.Length"
                    '''
                }
            }
        }
    }
}
