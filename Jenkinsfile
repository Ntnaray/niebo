pipeline {
        agent any
        environment {
            IMAGE_TAG= "${BUILD_NUMBER}"
            DOCKERHUB_CREDENTIALS = credentials ('swamy-docker-hub')

        }   
        stages {
        stage ('Checkout') {
            steps {

                git branch: 'master', credentialsId: '6120597c-372c-4107-b092-a73af23bdb18', url: 'https://github.com/Ntnaray/niebo.git'
            }
        }
        stage ('Build Docker') {
            steps {
                sh 'echo "Build Docker image"'
                sh 'docker build -t swamy877/cipipeline:${BUILD_NUMBER} .'
                //sh 'docker build -t swamy877/niebo:latest .'
        }
        }

        stage('Docker Login'){
        steps {
            sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'

        }
        }


        stage ('Push to Repo') {
            steps {
                sh 'echo "Push to Repo"'
                sh 'docker push swamy877/cipipeline:${BUILD_NUMBER}'
                // sh 'docker push swamy877/niebo:latest'
        }
        }
        stage ('Checkout K8S manifest SCM') {
            steps {
             git branch: 'main', credentialsId: '6120597c-372c-4107-b092-a73af23bdb18', url: 'https://github.com/Ntnaray/kube-manifest.git'   
            }
        }
        stage('Update K8S manifest & push to Repo'){
            steps {
                script{
                    withCredentials([usernamePassword(credentialsId: '6120597c-372c-4107-b092-a73af23bdb18', passwordVariable: '', usernameVariable: '')]){
                        sh '''
                        cat deployment.yaml
                        sed -i '' "s/replaceImageTag/${BUILD_NUMBER}/g" deployment.yaml
                        cat deployment.yaml
                        git add deployment.yaml
                        git commit -m 'Updated the deployment yaml | Jenkins Pipeline'
                        git remote -v
                        git push https://github.com/Ntnaray/kube-manifest.git HEAD:main
                        '''                      
                    }
                }
            }

        }
       }

}

