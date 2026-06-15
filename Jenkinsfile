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

        stage('Setup Environment') {
            steps {
                // Creates a virtual environment and installs your testing tools
                sh '''
                    PYTHON_BIN="python3"
                    if ! command -v "$PYTHON_BIN" >/dev/null 2>&1; then
                        PYTHON_BIN="python"
                    fi
                    "$PYTHON_BIN" -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r docker/servicio1/requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                // Runs pytest and exports results as a JUnit XML report
                sh '''
                    . venv/bin/activate
                    mkdir -p reports
                    pytest -q docker/servicio1/tests --junitxml=reports/results.xml
                '''
            }
            post {
                always {
                    // Publishes the test results right into the Jenkins UI
                    junit 'reports/results.xml'
                }
            }
        }
    }
}
