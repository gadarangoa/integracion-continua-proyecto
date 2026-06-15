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
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                // Runs pytest and exports results as a JUnit XML report
                sh '''
                    . venv/bin/activate
                    pytest --junitxml=reports/results.xml
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
