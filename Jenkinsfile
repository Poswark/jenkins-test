pipeline {
    agent any

    parameters {
        choice(name: 'BRANCH_NAME', choices: ['trunk', 'qa', 'xxx'], description: 'Branch to build')
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
                        error "\u001B[31mERROR:\u001B[0m BRANCH_NAME is not set"
                    }
                    git branch: branchName, url: REPO_URL, credentialsId: 'github'
                    echo "\u001B[32mSUCCESS:\u001B[0m Cloned repository successfully"
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
                        error "\u001B[31mERROR:\u001B[0m NAMESPACE is not set properly"
                    }
                    if (!serviceName?.trim()) {
                        error "\u001B[31mERROR:\u001B[0m SERVICE_NAME is not set properly"
                    }

                    // Asignar las variables de entorno
                    env.NAMESPACE = namespace
                    env.SERVICE_NAME = serviceName

                    echo "\u001B[32mINFO:\u001B[0m NAMESPACE: ${env.NAMESPACE}"
                    echo "\u001B[32mINFO:\u001B[0m SERVICE_NAME: ${env.SERVICE_NAME}"
                    // Listar archivos de ese namespace
                    sh "echo \u001B[32mINFO:\u001B[0m Listing services in namespace: ${env.NAMESPACE}"
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
                        error "\u001B[31mERROR:\u001B[0m File not found: ${fileName}"
                    }
                    echo "\u001B[32mINFO:\u001B[0m File content of ${fileName}:"
                    sh "cat ${fileName}"
                }
            }
        }
    }
}
