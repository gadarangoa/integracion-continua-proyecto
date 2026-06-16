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
            steps {
                sh '''
                    python3 -m venv ${VENV}
                    . ${VENV}/bin/activate
                    python -m pip install --upgrade pip
                    pip install -r docker/servicio1/requirements.txt
                    pip install -r docker/servicio2/requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    . ${VENV}/bin/activate
                    PYTHONPATH=docker/servicio1 python -m pytest -q docker/servicio1/tests --junitxml=reports/junit-servicio1.xml
                    PYTHONPATH=docker/servicio2 python -m pytest -q docker/servicio2/tests --junitxml=reports/junit-servicio2.xml
                '''
            }
            post {
                always {
                    junit 'reports/junit-*.xml'
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
