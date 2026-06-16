pipeline {
    agent any

    environment {
        VENV = '.venv'
        PYTHONPATH = 'docker/servicio1'
    }

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
                    python3 -m venv ${VENV}
                    ${VENV}/bin/python -m pip install --upgrade pip
                    ${VENV}/bin/pip install -r docker/servicio1/requirements.txt
                    ${VENV}/bin/pip install -r docker/servicio2/requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    mkdir -p reports
                    PYTHONPATH=docker/servicio1 ${VENV}/bin/python -m pytest -q docker/servicio1/tests --junitxml=reports/junit-servicio1.xml
                    PYTHONPATH=docker/servicio2 ${VENV}/bin/python -m pytest -q docker/servicio2/tests --junitxml=reports/junit-servicio2.xml
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
                echo 'Run Docker Compose (install docker in machine before run this stage).'
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
