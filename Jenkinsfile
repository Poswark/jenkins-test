pipeline {
    agent any

    environment {
        // Variables para el namespace y el nombre del servicio
        NAMESPACE = ''
        SERVICE_NAME = ''
    }

    stages {
        stage('Branch') {
            steps {
                script {
                    // Establecer las variables dependiendo de la rama
                    if (env.BRANCH_NAME == 'main') {
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
        stage('service') {
            steps {
                script {
                                        
                    // Leer el archivo y extraer la información
                    def fileContent = readFile('info.txt')
                    def lines = fileContent.split('\n')
                    def infoMap = [:]

                    lines.each { line ->
                        def parts = line.split('=')
                        if (parts.size() == 2) {
                            def key = parts[0].trim()
                            def value = parts[1].trim()
                            if (key.startsWith("${env.NAMESPACE}.${env.SERVICE_NAME}")) {
                                infoMap[key] = value
                            }
                        }
                    }

                    echo "Extracted Information:"
                    infoMap.each { key, value ->
                        echo "${key} = ${value}"
                    }

                }
            }
        }
    }
}
