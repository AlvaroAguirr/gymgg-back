pipeline {
    agent any

    stages {
        stage('Clonar repositorio') {
            steps {
                git 'https://github.com/AlvaroAguirr/gymgg-back.git'
            }
        }

        stage('Instalar dependencias') {
            steps {
                bat 'python -m venv venv'
                bat '.\\venv\\Scripts\\activate && pip install --upgrade pip'
                bat '.\\venv\\Scripts\\activate && pip install -r requirements.txt'
            }
        }

        stage('Migraciones') {
            steps {
                bat '.\\venv\\Scripts\\activate && python manage.py migrate'
            }
        }

        stage('Pruebas') {
            steps {
                bat '. venv/bin/activate && python manage.py'
            }
        }
    }
}
