pipeline {
    agent any
    environment {
        NAME=credentials("name")
        EMAIL=credentials("email")
        PASSWORD=credentials("password")
        NEW_PASSWORD=credentials("new_password")
        MARKER=credentials("marker")
    }
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
                bat "python -m pytest -m ${env.MARKER} --junitxml=report.xml"
            }
        }
    }
    post {
        always {
            junit "report.xml"
        }
    }
}