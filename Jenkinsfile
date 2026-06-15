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

run_tests_local() {
    py_bin="$1"
    "$py_bin" -m venv .venv
    .venv/bin/pip install --upgrade pip
    .venv/bin/pip install -r docker/servicio1/requirements.txt
    cd docker/servicio1
    ../../.venv/bin/pytest -q
}

if command -v docker >/dev/null 2>&1; then
    echo "Running tests with Docker"
    docker run --rm \
        -u root:root \
        -v "$PWD":/workspace \
        -w /workspace \
        python:3.11 \
        sh -c '
python -m venv .venv &&
.venv/bin/pip install --upgrade pip &&
.venv/bin/pip install -r docker/servicio1/requirements.txt &&
cd docker/servicio1 &&
../../.venv/bin/pytest -q
'
elif command -v python3 >/dev/null 2>&1; then
    echo "Docker not available. Running tests with local python3"
    run_tests_local python3
elif command -v python >/dev/null 2>&1; then
    echo "Docker not available. Running tests with local python"
    run_tests_local python
else
    echo "ERROR: docker, python3, and python are unavailable on this agent." >&2
    echo "Install Docker CLI or Python 3 on the agent, then retry." >&2
    exit 1
fi
'''
            }
        }
    }
}
