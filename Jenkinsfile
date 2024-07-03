pipeline {
    agent { label 'jslave' }
    environment {
        DOCKER_CREDENTIALS_ID = 'docker_hub_login'
        DOCKER_IMAGE_BACKEND = 'deeeye2/devops-bot-backend-v1:latest'
        DOCKER_IMAGE_UI = 'deeeye2/devops-bot-ui:latest'
        SSH_SERVER_NAME = 'kubeconfig'
        DOCKER_CMD = '/usr/bin/docker'
    }
    stages {
        stage('Cleanup Workspace') {
            steps {
                deleteDir()
            }
        }
        stage('Cleanup Docker Images') {
            steps {
                script {
                    sh "${env.DOCKER_CMD} container prune -f"
                    sh "${env.DOCKER_CMD} image prune -a -f"
                    sh "${env.DOCKER_CMD} volume prune -f"
                    sh "${env.DOCKER_CMD} network prune -f"
                    sh "${env.DOCKER_CMD} system prune -a -f --volumes"
                }
            }
        }
        stage('Checkout') {
            steps {
                git 'https://github.com/deeeye2/devops_bot.git'
            }
        }
        stage('Build and Push Backend') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE_BACKEND}", "./backend")
                    docker.withRegistry('https://index.docker.io/v1/', "${DOCKER_CREDENTIALS_ID}") {
                        docker.image("${DOCKER_IMAGE_BACKEND}").push()
                    }
                }
            }
        }
        stage('Build and Push UI') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE_UI}", "./ui")
                    docker.withRegistry('https://index.docker.io/v1/', "${DOCKER_CREDENTIALS_ID}") {
                        docker.image("${DOCKER_IMAGE_UI}").push()
                    }
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                script {
                    sshPublisher(publishers: [
                        sshPublisherDesc(
                            configName: SSH_SERVER_NAME,
                            transfers: [
                                sshTransfer(
                                    sourceFiles: 'k8s/*',
                                    removePrefix: 'k8s/',
                                    remoteDirectory: '/home/minikubeuser/k8s',
                                    execCommand: '''
                                        cd /home/minikubeuser/k8s
                                        kubectl apply -f backend-deployment.yaml
                                        kubectl apply -f backend-service.yaml
                                        kubectl apply -f ui-deployment.yaml
                                        kubectl apply -f ui-service.yaml
                                    '''
                                )
                            ]
                        )
                    ])
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

