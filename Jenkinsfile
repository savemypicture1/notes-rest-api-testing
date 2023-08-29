pipeline {
    agent any
    stages {
        stage("Clone repository") {
            steps {
                git branch: "main", url: "https://github.com/savemypicture1/notes-rest-api-testing"
            }
        }
        stage("Set path") {
            steps {
                script {
                    env.PATH = "C:\\Python311\\;${env.PATH}"
                }
            }
        }
        stage("Setup environment") {
            steps {
                bat "python -m pip install -r requirements.txt"
            }
        }
        stage("Testing") {
            steps {
                bat "pytest"
            }
        }
    }
}