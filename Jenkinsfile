pipeline {
    agent any
    stages {
        stage("Clone repository") {
            steps {
                git branch: "main", url: "https://github.com/savemypicture1/notes-rest-api-testing"
            }
        }
    }
}