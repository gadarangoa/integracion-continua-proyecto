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

        stage('Install') {
            agent {
                docker {
                    image 'python:3.11-slim'
                    reuseNode true
                }
            }
            steps {
                sh '''set -e
                python --version
                python -m venv $VENV
                . $VENV/bin/activate
                python -m pip install --upgrade pip
                python -m pip install -r docker/servicio1/requirements.txt
                '''
            }
        }

        stage('Test') {
            agent {
                docker {
                    image 'python:3.11-slim'
                    reuseNode true
                }
            }
            steps {
                sh '''set -e
                . $VENV/bin/activate
                mkdir -p reports
                pytest -q docker/servicio1/tests --junitxml=reports/pytest.xml
                '''
            }
            post {
                always {
                    junit testResults: 'reports/pytest.xml', allowEmptyResults: false
                    archiveArtifacts artifacts: 'reports/**/*', allowEmptyArchive: true
                }
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
