pipeline {
    agent any

    environment {
        GIT_REPO    = 'https://github.com/shyampuli/flask-app.git'
        GIT_BRANCH  = 'main'

        // Docker Hub details
        DOCKER_USER = 'shyamprasad2310'
        IMAGE_NAME  = 'flask-app'
    }

    stages {

        

        stage('Checkout') {
            steps {
                git branch: "${GIT_BRANCH}", url: "${GIT_REPO}"
            }
        }

        stage('Build Docker Image') {
            steps {
                bat """
                docker build -t %DOCKER_USER%/%IMAGE_NAME%:%BUILD_NUMBER% .
                docker tag %DOCKER_USER%/%IMAGE_NAME%:%BUILD_NUMBER% %DOCKER_USER%/%IMAGE_NAME%:latest
                """
            }
        }

        stage('Login to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-credentials-id',
                    usernameVariable: 'HUB_USER',
                    passwordVariable: 'HUB_PASS'
                )]) {
                    bat 'echo %HUB_PASS% | docker login -u %HUB_USER%'
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                bat """
                docker push %DOCKER_USER%/%IMAGE_NAME%:%BUILD_NUMBER%
                docker push %DOCKER_USER%/%IMAGE_NAME%:latest
                """
            }
        }
    }

    post {
        always {
            bat 'docker logout'
        }

        success {
            echo 'Docker image built and pushed successfully!'
        }

        failure {
            echo 'Pipeline failed. Check the console output for details.'
        }
    }
}
