pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\sbhol\\AppData\\Local\\Programs\\Python\\Python310\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Train Model') {
            steps {
                bat '"C:\\Users\\sbhol\\AppData\\Local\\Programs\\Python\\Python310\\python.exe" train.py'
            }
        }

        stage('Test Model') {
            steps {
                bat '"C:\\Users\\sbhol\\AppData\\Local\\Programs\\Python\\Python310\\python.exe" test.py'
            }
        }

        stage('Deploy API') {
            steps {
                bat 'start /B "" "C:\\Users\\sbhol\\AppData\\Local\\Programs\\Python\\Python310\\python.exe" app.py'
            }
        }
    }
}