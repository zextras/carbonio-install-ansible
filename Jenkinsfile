library(
    identifier: 'jenkins-lib-common@v4.10.0',
    retriever: modernSCM([
        $class: 'GitSCMSource',
        remote: 'git@github.com:zextras/jenkins-lib-common.git',
        credentialsId: 'jenkins-integration-with-github-account'
    ])
)

pipeline {
    agent {
        node {
            label 'infra-v1'
        }
    }

    options {
        skipDefaultCheckout()
        buildDiscarder(logRotator(numToKeepStr: '10'))
        timeout(time: 1, unit: 'HOURS')
        disableConcurrentBuilds()
    }
    
    stages {
        stage('Checkout') {
            when {
                anyOf {
                    expression { env.BRANCH_NAME == 'main'}
                    buildingTag()
                }
            }
            steps {
                checkout scm
            }
        }

        stage('Build Collection') { 
            when {
                anyOf {
                    expression { env.BRANCH_NAME == 'main'}
                    buildingTag()
                }
            }          
            steps {
                container('ansible') {
                    sh 'ansible-galaxy collection build'
                }
            }
        }

        stage('Publish Collection') {   
            when {
                buildingTag()
            }         
            steps {
                container('ansible') {
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
}
