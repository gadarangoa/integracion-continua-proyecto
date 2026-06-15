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

    parameters {
        booleanParam(name: 'RUN_DEPLOY', defaultValue: false, description: 'Ejecuta deploy local con Docker Compose')
    }

    stages {
        stage('Checkout') {
            steps {
                git scm
            }
        }

        stage('Install') {
            steps {
                sh '''set -e
                python3 -m venv $VENV
                source $VENV/bin/activate
                python -m pip install --upgrade pip
                pip install -r docker/servicio1/requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''set -e
                source $VENV/bin/activate
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
            when {
                expression { params.RUN_DEPLOY }
            }
            steps {
                sh 'docker compose up -d servicio1'
            }
        }
    }

    post {
        always {
            sh 'docker compose down || true'
        }
    }
}
