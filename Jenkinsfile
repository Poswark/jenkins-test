pipeline {
    agent any

    parameters {
        string(name: 'NAMESPACE', defaultValue: '', description: 'Namespace of the service')
        string(name: 'SERVICE_NAME', defaultValue: '', description: 'Name of the service')
    }
    environment {
        REPO_URL = 'https://github.com/Poswark/jenkins-test.git'
    }

    stages {
        stage('Clone Repository') {
            steps {
                script {
                    // Configurar las credenciales si es necesario
                    def branchName = env.BRANCH_NAME
                    if (!branchName) {
                        error "BRANCH_NAME is not set"
                    }
                    git branch: branchName, url: REPO_URL, credentialsId: 'github'
                }
            }
        }
        
        stage('Set Variables') {
            steps {
                script {
                    // Usar parámetros en lugar de variables locales
                    def namespace = params.NAMESPACE
                    def serviceName = params.SERVICE_NAME

                    // Validar que los parámetros no sean nulos ni vacíos
                    if (!namespace?.trim()) {
                        error "NAMESPACE is not set properly"
                    }
                    if (!serviceName?.trim()) {
                        error "SERVICE_NAME is not set properly"
                    }

                    // Asignar las variables de entorno
                    env.NAMESPACE = namespace
                    env.SERVICE_NAME = serviceName

                    echo "NAMESPACE: ${env.NAMESPACE}"
                    echo "SERVICE_NAME: ${env.SERVICE_NAME}"
                    // Listar archivos de ese namespace
                    sh "echo Listar servicios de namespace"
                    sh "ls -ltr ${env.NAMESPACE}"
                }
            }
        }

        stage('Extract Information') {
            steps {
                script {
                    // Leer el archivo cuyo nombre es el del servicio con extensión .txt
                    def fileName = "${env.NAMESPACE}/${env.SERVICE_NAME}.txt"
                    if (!fileExists(fileName)) {
                        error "File not found: ${fileName}"
                    }
                    sh "cat ${fileName}"
                }
            }
        }
    }
}