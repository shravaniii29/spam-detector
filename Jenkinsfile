pipeline {
    agent any

    environment {
        EC2_IP = "13.60.68.110"
        KEY_PATH = "C:\Shravani Data\Study\ENGINEERING\TE\SEM 6\Cloud Computing\CCAI_CA_Jenkins\spam-detector-key.pem"
    }

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

        stage('Deploy to EC2') {
            steps {
                bat """
                ssh -i %KEY_PATH% ubuntu@%EC2_IP% ^
                "cd spam-detector || git clone https://github.com/shravaniii29/spam-detector.git && ^
                cd spam-detector && git pull && ^
                pkill -f app.py || true && ^
                nohup python3 app.py > output.log 2>&1 &"
                """
            }
        }
    }
}