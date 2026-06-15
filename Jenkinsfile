pipeline {
    agent any

    stages {
        stage('checkout') {
            steps {
                checkout scm
            }
        }

        stage('install') {
            steps {
                sh 'python3 -m venv .venv'
                sh '. .venv/bin/activate && pip install --upgrade pip && pip install -r docker/servicio1/requirements.txt'
            }
        }

        stage('test') {
            steps {
                sh '. .venv/bin/activate && cd docker/servicio1 && pytest -q'
            }
        }

        stage('build') {
            steps {
                sh 'docker build -t servicio1:ci ./docker/servicio1'
            }
        }

        stage('deploy') {
            steps {
                sh 'docker compose up -d --build servicio1 postgres'
            }
        }
    }
}
