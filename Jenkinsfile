pipeline {
    agent any

    environment {
        DOCKER_USER = "shyamprasad2310"
        IMAGE_NAME = "flask-app"
        GIT_REPO = "https://github.com/shyampuli/flask-app.git"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: "${GIT_REPO}"
            }
        }

        stage('Build Image') {
            steps {
                bat "docker build -t %DOCKER_USER%/%IMAGE_NAME%:%BUILD_NUMBER% ."
                bat "docker tag %DOCKER_USER%/%IMAGE_NAME%:%BUILD_NUMBER% %DOCKER_USER%/%IMAGE_NAME%:latest"
            }
        }

        stage('Login & Push') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-credentials-id',
                        usernameVariable: 'HUB_USER',
                        passwordVariable: 'HUB_PASS'
                    )
                ]) {

                    bat '''
                    echo %HUB_PASS% | docker login -u %HUB_USER% --password-stdin
                    docker push %DOCKER_USER%/%IMAGE_NAME%:%BUILD_NUMBER%
                    docker push %DOCKER_USER%/%IMAGE_NAME%:latest
                    docker logout
                    '''
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully.'
        }

        failure {
            echo 'Pipeline failed.'
        }
    }
}
