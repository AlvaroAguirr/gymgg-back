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
                bat '''
                python -m venv venv
                call venv\\Scripts\\activate
                venv\\Scripts\\python.exe -m pip install --upgrade pip
                venv\\Scripts\\pip install -r requirements.txt
                '''
            }
        }

        stage('Migraciones') {
            steps {
                bat '''
                call venv\\Scripts\\activate
                cd backend
                python manage.py makemigrations
                python manage.py migrate
                '''
            }
        }

        stage('Pruebas') {
            steps {
                bat '''
                call venv\\Scripts\\activate
                cd backend
                python manage.py test
                '''
            }
        }
    }
}
