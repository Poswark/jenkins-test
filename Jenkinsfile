pipeline {
    agent any

    parameters {
        string(name: 'BRANCH', defaultValue: 'main', description: 'Nombre de la rama a clonar')
        choice(name: 'ENVIRONMENT', choices: ['developer', 'qa', 'prd'], description: 'Ambiente de ejecución')
    }

    environment {
        GIT_REPO = 'https://github.com/Poswark/kics-checkmarx.git' 
        DOCKER_IMAGE = 'poswark/tools:latest'
    }

    stages {
        stage('Clonar repositorio') {
            steps {
                echo "🔁 Clonando rama ${params.BRANCH} desde ${env.GIT_REPO}"
                dir('repo') {
                    git branch: "${params.BRANCH}", url: "${env.GIT_REPO}"
                }
            }
        }

        stage('Ejecutar en contenedor Docker') {
            steps {
                script {
                    echo "🚀 Ejecutando entorno: ${params.ENVIRONMENT}"
                    try {
                        sh """
                            docker run --rm -v "\$PWD/repo":/app -w /app ${DOCKER_IMAGE} bash -c '
                              echo "🧪 Ambiente: ${params.ENVIRONMENT}"
                              echo "📂 Contenido del repositorio:"
                              ls -la
                              # Simulación de despliegue o procesamiento
                              # ./deploy.sh ${params.ENVIRONMENT}
                            '
                        """
                        echo "✅ Script ejecutado exitosamente en el contenedor Docker."
                    } catch (err) {
                        echo "❌ Error durante la ejecución del contenedor Docker:"
                        echo "${err}"
                        error("Falló la ejecución del bash en el contenedor.")
                    }
                }
            }
        }
    }
}
