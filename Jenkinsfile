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
                sh "python3 -m venv $VENV"
                sh "source $VENV/bin/activate"
                sh "pip install -r docker/servicio1/requirements.txt"
            }
        }

        stage('Test') {
            steps {
                sh "source $VENV/bin/activate"
                sh "mkdir -p reports"
                sh "pytest -q docker/servicio1/tests --junitxml=reports/pytest.xml"
            }
        }

        stage('Build') {
            steps {
                sh 'docker compose build servicio1'
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
