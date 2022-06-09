pipeline {
  agent any
  stages {
    stage('Log Tool Version') {
      parallel {
        stage('Log Tool Version') {
          steps {
            sh 'mvn --version'
            sh 'git --version'
            sh 'java -version'
          }
        }

        stage('Check file') {
          steps {
            fileExists 'main.py'
          }
        }

      }
    }

    stage('Build') {
      steps {
        sh 'python main.py'
      }
    }

    stage('Post Build Steps') {
      steps {
        writeFile(file: 'status.txt', text: 'it works !!!')
      }
    }

  }
}