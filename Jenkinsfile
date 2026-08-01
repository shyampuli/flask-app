pipeline {
    agent any

    environment {
        DOCKER_USER = 'shyamprasad2310'
        IMAGE_NAME = 'flask-app'
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/shyampuli/flask-app.git'
            }
        }

        stage('Build Image') {
            steps {
                bat """
                docker build -t %DOCKER_USER%/%IMAGE_NAME%:%BUILD_NUMBER% .
                docker tag %DOCKER_USER%/%IMAGE_NAME%:%BUILD_NUMBER% %DOCKER_USER%/%IMAGE_NAME%:latest
                """
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

                    bat """
                    @echo off

                    echo Logging into Docker Hub...

                    echo %HUB_PASS% | docker login -u %HUB_USER% --password-stdin
                    if errorlevel 1 exit /b 1

                    docker push %DOCKER_USER%/%IMAGE_NAME%:%BUILD_NUMBER%
                    if errorlevel 1 exit /b 1

                    docker push %DOCKER_USER%/%IMAGE_NAME%:latest
                    if errorlevel 1 exit /b 1

                    docker logout
                    """
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed!'
        }
    }
}
