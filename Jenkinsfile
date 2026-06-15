pipeline {
    agent any

    options {
        timestamps()
        timeout(time: 20, unit: 'MINUTES')
        disableConcurrentBuilds()
    }

    environment {
        COMPOSE_PROJECT_NAME = "ic-${BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install') {
            agent {
                docker {
                    image 'python:3.11'
                    args '-u root:root'
                }
            }
            steps {
                sh 'python -m venv .venv'
                sh '.venv/bin/pip install --upgrade pip'
                sh '.venv/bin/pip install -r docker/servicio1/requirements.txt'
            }
        }

        stage('Test') {
            agent {
                docker {
                    image 'python:3.11'
                    args '-u root:root'
                }
            }
            steps {
                sh 'mkdir -p reports'
                sh 'cd docker/servicio1 && ../../.venv/bin/pytest -q --junitxml=../../reports/pytest.xml'
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t servicio1:ci ./docker/servicio1'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker compose down || true'
                sh 'docker compose up -d --build servicio1 postgres'
            }
        }

    }

    post {
        always {
            junit allowEmptyResults: true, testResults: 'reports/*.xml'
            sh 'docker compose down || true'
        }
        failure {
            sh 'docker compose logs --no-color servicio1 postgres servicio2 || true'
        }
    }
}