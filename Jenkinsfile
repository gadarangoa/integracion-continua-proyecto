pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Sanity Check') {
            steps {
                echo 'Todo funciona'
                sh 'echo "Pipeline base ejecutandose correctamente"'
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
                sh 'python -m venv .venv'
                sh '.venv/bin/pip install --upgrade pip'
                sh '.venv/bin/pip install -r docker/servicio1/requirements.txt'
                sh 'cd docker/servicio1 && ../../.venv/bin/pytest -q'
            }
        }
    }
}