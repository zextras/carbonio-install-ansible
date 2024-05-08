pipeline {
    agent {
        node {
            label 'infra-agent-v3'
        }
    }

    options {
        skipDefaultCheckout()
        buildDiscarder(logRotator(numToKeepStr: '10'))
        timeout(time: 1, unit: 'HOURS')
    }
    
    stages {

        stage('Checkout') {
            when {
                expression { env.BRANCH_NAME == 'main'}
            }
                steps {
                    checkout scm
                }
        }

        stage('Build Collection') { 
            when {
                expression { env.BRANCH_NAME == 'main'}
            }          
            steps {
                sh 'ansible-galaxy collection build'
            }
        }

        stage('Publish Collection') {   
            when {
                expression { env.BRANCH_NAME == 'main'}
            }         
            steps {
                withCredentials([string(credentialsId: 'ansible-galaxy-token', variable: 'galaxy_token')]) {
                    sh """
                    ARTIFACT=`ls | grep tar.gz`
                    ansible-galaxy   collection publish \$ARTIFACT --token ${galaxy_token}
                """
                }   
            }
        }
    }

}

