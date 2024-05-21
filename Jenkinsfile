pipeline {
    agent any

    environment {
        // Variables para el namespace y el nombre del servicio
        NAMESPACE = ''
        SERVICE_NAME = ''
        REPO_URL = 'https://github.com/Poswark/jenkins-test.git'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: '${env.BRANCH_NAME}', url: 'https://github.com/Poswark/jenkins-test.git'}
            }
        }
        stage('Branch') {
            steps {
                script {
                    // Establecer las variables dependiendo de la rama
                    if (env.BRANCH_NAME == 'trunk') {
                        env.NAMESPACE = 'namespace1'
                        env.SERVICE_NAME = 'service1'
                    } else if (env.BRANCH_NAME == 'qa') {
                        env.NAMESPACE = 'namespace2'
                        env.SERVICE_NAME = 'service1'
                    } else {
                        error "Branch not supported"
                    }
                }
            }
        }
      stage('Extract Information') {
            steps {
                script {
                    // Validar que SERVICE_NAME no sea nulo ni vacío
                    if (!env.SERVICE_NAME?.trim()) {
                        error "SERVICE_NAME is not set properly"
                    }

                    // Leer el archivo cuyo nombre es el del servicio con extensión .txt
                    def fileName = "${env.SERVICE_NAME}.txt"
                    if (!fileExists(fileName)) {
                        error "File not found: ${fileName}"
                    }

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

                    // echo "Extracted Information:"
                    // infoMap.each { key, value ->
                    //     echo "${key} = ${value}"
                    // }

                }
            }
        }
    }

