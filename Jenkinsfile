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
                sh 'python -m venv venv'
                sh '. venv/bin/activate && pip install --upgrade pip'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Migraciones') {
            steps {
                sh '. venv/bin/activate && python manage.py migrate'
            }
        }

        stage('Pruebas') {
            steps {
                sh '. venv/bin/activate && python manage.py'
            }
        }
    }
}
