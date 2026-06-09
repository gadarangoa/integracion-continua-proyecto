pipeline {
    agent any

    stages {
        stage('Clonar Repositorio') {
            steps {
                echo 'Descargando la última versión del código desde GitHub...'
            }
        }

        stage('Construir Infraestructura Docker') {
            steps {
                echo 'Iniciando compilación de contenedores...'
                // Compila y levanta los microservicios localmente
                sh 'docker compose up --build -d'
            }
        }

        stage('Validar Estado') {
            steps {
                echo 'Verificando que los contenedores estén activos...'
                sh 'docker compose ps'
            }
        }
    }
}