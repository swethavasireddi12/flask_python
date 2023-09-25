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
        bat 'docker build -t flask_jenkins:v1 .'          
      }
     
        }
    stage('Run Image') {     
      steps {            
        bat 'docker run -d -p 5000:5000 --name container3 flask:v1'          
      }       
    }
  }
}
