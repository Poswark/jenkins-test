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
                                        
                    // Leer el archivo cuyo nombre es el del servicio con extensión .txt
                    def fileContent = readFile("${env.SERVICE_NAME}.txt")
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
}
