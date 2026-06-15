pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install') {
            steps {
                sh 'python3 -m venv .venv'
                sh '.venv/bin/pip install --upgrade pip'
                sh '.venv/bin/pip install -r docker/servicio1/requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh 'cd docker/servicio1 && ../../.venv/bin/pytest -q'
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

        stage('Smoke Test') {
            steps {
                sh 'sleep 10'
                sh 'curl --fail http://localhost:3000/health'
            }
        }
    }
}