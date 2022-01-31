pipeline {
 agent any
     stages {
         stage('Clone Repository') {
         /* Cloning the repository to our workspace */
         steps {
         checkout scm
         }
    }
    stage('Build Image') {
         steps {
         sh 'sudo docker build -t flask_app .'
         }
    }
    stage('Run Image') {
         steps {
         sh 'sudo docker run -p 8000:8000 flask_app'
         }
    }
    stage('Testing'){
         steps {
             echo 'Testing..'
             }
    }
    }
}
