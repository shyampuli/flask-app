pipeline {
    agent any

    environment {
        // Change 'shyampuli' to your actual Docker Hub username
        DOCKER_USER = 'shyampuli'
        IMAGE_NAME  = 'flask-app'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/shyampuli/flask-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                // 'bat' runs Windows terminal commands
                bat "docker build -t ${DOCKER_USER}/${IMAGE_NAME}:${BUILD_NUMBER} ."
                bat "docker tag ${DOCKER_USER}/${IMAGE_NAME}:${BUILD_NUMBER} ${DOCKER_USER}/${IMAGE_NAME}:latest"
            }
        }

        stage('Push to Docker Hub') {
            steps {
                // Log in, push image tags, and log out safely using Jenkins credentials
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials-id', usernameVariable: 'HUB_USER', passwordVariable: 'HUB_PASS')]) {
                    bat "echo %HUB_PASS% | docker login -u %HUB_USER% --password-stdin"
                    bat "docker push ${DOCKER_USER}/${IMAGE_NAME}:${BUILD_NUMBER}"
                    bat "docker push ${DOCKER_USER}/${IMAGE_NAME}:latest"
                    bat "docker logout"
                }
            }
        }
    }
}
