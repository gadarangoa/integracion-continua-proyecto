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
            steps {
                sh '''#!/bin/sh
set -eu
docker run --rm \
  -u root:root \
  -v "$PWD":/workspace \
  -w /workspace \
  python:3.11 \
  sh -c "python -m venv .venv && .venv/bin/pip install --upgrade pip && .venv/bin/pip install -r docker/servicio1/requirements.txt && cd docker/servicio1 && ../../.venv/bin/pytest -q"
'''
            }
        }
    }
}
