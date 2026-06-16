pipeline {
    agent any

    options {
        timestamps()
        disableConcurrentBuilds()
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup') {
            agent {
                docker {
                    image 'python:3.11'
                    reuseNode true
                }
            }
            steps {
                sh '''
                    python -m pip install --upgrade pip
                    pip install -r docker/servicio1/requirements.txt
                    pip install -r docker/servicio2/requirements.txt
                    pip install pytest
                '''
            }
        }

        stage('Test') {
            agent {
                docker {
                    image 'python:3.11'
                    reuseNode true
                }
            }
            steps {
                sh '''
                    mkdir -p reports
                    PYTHONPATH=docker/servicio1 pytest -q docker/servicio1/tests --junitxml=reports/junit-servicio1.xml
                    PYTHONPATH=docker/servicio2 pytest -q docker/servicio2/tests --junitxml=reports/junit-servicio2.xml
                '''
            }
            post {
                always {
                    junit 'reports/*.xml'
                }
            }
        }

        stage('Build') {
            steps {
                echo 'Run Docker Compose o docker build para construir imágenes.'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploy stage habilitado (sin despliegue real por ahora).'
            }
        }
    }

    post {
        always {
            sh 'docker compose down || true'
        }
    }
}