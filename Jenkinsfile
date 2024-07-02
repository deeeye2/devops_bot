pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build and Push Backend') {
            steps {
                script {
                    docker.build("deeeye2/devops-bot-backend:latest", "./backend")
                    docker.withRegistry('https://index.docker.io/v1/', "${DOCKERHUB_CREDENTIALS}") {
                        docker.image("deeeye2/devops-bot-backend:latest").push()
                    }
                }
            }
        }

        stage('Build and Push UI') {
            steps {
                script {
                    docker.build("deeeye2/devops-bot-ui:latest", "./ui")
                    docker.withRegistry('https://index.docker.io/v1/', "${DOCKERHUB_CREDENTIALS}") {
                        docker.image("deeeye2/devops-bot-ui:latest").push()
                    }
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    sh 'kubectl apply -f k8s/backend-deployment.yaml'
                    sh 'kubectl apply -f k8s/backend-service.yaml'
                    sh 'kubectl apply -f k8s/ui-deployment.yaml'
                    sh 'kubectl apply -f k8s/ui-service.yaml'
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
