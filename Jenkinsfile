
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
        bat 'docker run -d -p 5000:5000 --name jenkins_task2 flask_jenkins:v2'  
      }       
    }
  }
}
