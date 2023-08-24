pipeline {
        agent any
        environment {
            IMAGE_TAG= "${BUILD_NUMBER}"
            DOCKERHUB_CREDENTIALS = credentials ('swamy-docker-hub')

        }   
        stages {
        stage ('Checkout') {
            steps {

                git branch: 'main', credentialsId: '6120597c-372c-4107-b092-a73af23bdb18', url: 'https://github.com/Ntnaray/niebo_django.git'
            }
        }
        stage ('Build Docker') {
            steps {
                sh 'echo Build Docker image'
                sh 'docker build -t swamy877/cipipeline:${BUILD_NUMBER} .'
        }
        }

        stage('Docker Login'){
        steps {
            sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'

        }
        }


        stage ('Push to Repo') {
            steps {
                sh 'Push to Repo'
                sh 'docker push swamy877/cipipeline:${BUILD_NUMBER}'
        }
        }

        }
       }
