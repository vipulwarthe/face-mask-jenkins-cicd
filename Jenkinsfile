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
         sh 'docker build -t flask_app .'
         }
    }
    stage('Run Image') {
         steps {
         sh 'docker run -p 8000:8000 face_mask'
         }
    }
    stage('Testing'){
         steps {
             echo 'Testing..'
             }
    }
    }
}