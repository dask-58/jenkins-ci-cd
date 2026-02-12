pipeline {
    agent any

    environment {
        DOCKER_USER = 'dask58'
        IMAGE_NAME = 'flask-web-app'
        IMAGE_TAG = "${env.BUILD_ID}"
        REGISTRY = "docker.io/${DOCKER_USER}/${IMAGE_NAME}"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/dask-58/jenkins-ci-cd'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    app = docker.build("${REGISTRY}:${IMAGE_TAG}",
                        "--build-arg BUILD_ID=${env.BUILD_ID} .")
                }
            }
        }

        stage('Push to Registry') {
            steps {
                script {
                    docker.withRegistry('', 'docker-hub-credentials') {
                        app.push()
                        app.push("latest")
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    sh "docker stop ${IMAGE_NAME} || true"
                    sh "docker rm ${IMAGE_NAME} || true"
                    sh """
                        docker run -d --name ${IMAGE_NAME} \
                        -p 5000:5000 \
                        -e BUILD_ID=${env.BUILD_ID} \
                        ${REGISTRY}:latest
                    """
                }
            }
        }
    }

    post {
        always {
            sh "docker rmi ${REGISTRY}:${IMAGE_TAG} || true"
        }
    }
}
