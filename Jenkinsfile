pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials-id')
        IMAGE_NAME = 'shyamprasad2310/flask-app'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/YOUR_USERNAME/flask-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    appImage = docker.build("${IMAGE_NAME}:${BUILD_NUMBER}")
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'dockerhub-credentials-id') {
                        appImage.push("${BUILD_NUMBER}")
                        appImage.push("latest")
                    }
                }
            }
        }
    }
}
