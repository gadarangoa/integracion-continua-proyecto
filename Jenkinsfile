pipeline {
    agent any

    environment {
        VENV = '.venv'
    }

    stages {
        stage('Checkout') {
            steps {
                git scm
            }
        }
        stage('Setup') {
            steps {
                sh '''python3 -m venv $VENV
                source $VENV/bin/activate
                pip install -r docker/servicio1/requirements.txt
                pip install pytest
                '''
            }
        }
    }
}
