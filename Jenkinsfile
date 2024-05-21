pipeline {
    agent any

    parameters {
        string(name: 'BRANCH_NAME', defaultValue: 'trunk', description: 'Branch to build')
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

                    def fileContent = readFile(fileName)
                    def lines = fileContent.split('\n')
                    def infoMap = [:]

                    lines.each { line ->
                        def parts = line.split('=')
                        if (parts.size() == 2) {
                            def key = parts[0].trim()
                            def value = parts[1].trim()
                            // Verificar si la clave empieza con el namespace y el nombre del servicio
                            if (key.startsWith("${env.NAMESPACE}.${env.SERVICE_NAME}")) {
                                infoMap[key] = value
                            }
                        }
                    }

                    // Imprimir la información extraída
                    echo "Extracted Information:"
                    infoMap.each { key, value ->
                        echo "${key} = ${value}"
                    }
                }
            }
        }
    }
}