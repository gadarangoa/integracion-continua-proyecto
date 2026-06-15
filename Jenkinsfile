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
            steps {
                sh '''set -e
                if command -v python3 >/dev/null 2>&1; then
                    PYTHON_BIN=python3
                elif command -v python >/dev/null 2>&1; then
                    PYTHON_BIN=python
                else
                    echo "Python no encontrado. Intentando instalar en el agente..."
                    if command -v apt-get >/dev/null 2>&1; then
                        apt-get update
                        apt-get install -y python3 python3-venv python3-pip
                        PYTHON_BIN=python3
                    elif command -v apk >/dev/null 2>&1; then
                        apk add --no-cache python3 py3-pip
                        PYTHON_BIN=python3
                    elif command -v yum >/dev/null 2>&1; then
                        yum install -y python3 python3-pip
                        PYTHON_BIN=python3
                    else
                        echo "ERROR: No hay Python y no se pudo instalar automaticamente en este agente."
                        exit 1
                    fi
                fi

                $PYTHON_BIN --version
                $PYTHON_BIN -m venv $VENV
                . $VENV/bin/activate
                python -m pip install --upgrade pip
                python -m pip install -r docker/servicio1/requirements.txt
                '''
            }
        }

        stage('Test') {
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
