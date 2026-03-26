pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Train Model') {
            steps {
                bat 'python train.py'
            }
        }

        stage('Test Model') {
            steps {
                bat 'python test.py'
            }
        }

        stage('Deploy API') {
            steps {
                bat 'start /B python app.py'
            }
        }
    }
}