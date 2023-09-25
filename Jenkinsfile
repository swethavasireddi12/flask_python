
pipeline {
  agent any
  stages {
    stage('Checkout') {           
      steps {                              
        checkout scm          
      }   
    }
    stage('Build') {

       steps {      
        bat 'docker build -t flask_jenkins:v2 .'          
      }
     
        }
    stage('Run Image') {     
      steps {            
        bat 'docker run -d -p 5001:5001 --name jenkins_task1 flask_jenkins:v2'  
      }       
    }
  }
}
