// https://plugins.jenkins.io/email-ext-recipients-column/
pipeline {
    agent any

    stages {
        stage('Generar HTML') {
            steps {
                script {
                    // Generar archivo reporte.html
                    writeFile file: 'reporte.html', text: """
                    <!DOCTYPE html>
                    <html>
                      <head><title>Reporte</title></head>
                      <body>
                        <h1 style="color:#2c3e50;">Hola mundo</h1>
                        <p>Este es el Job: <b>${env.JOB_NAME}</b> #${env.BUILD_NUMBER}</p>
                      </body>
                    </html>
                    """
                }
            }
        }
    }

    post {
        always {
            emailext(
                from: 'contacto@gmailxxx.com',
                to: 'giovannyorjuel2@gmail.com',
                subject: "📊 Reporte del Job ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                mimeType: 'text/html',
                body: """
                <html>
                <body style="font-family:Arial, sans-serif; background:#f9f9f9; padding:20px;">
                  <h2 style="color:#2c3e50;">🔔 Notificación del Pipeline</h2>
                  <table style="border-collapse:collapse; width:100%; max-width:500px; background:#ffffff; box-shadow:0 2px 5px rgba(0,0,0,0.1);">
                    <tr style="background:#2c3e50; color:#ffffff;">
                      <th style="padding:10px; text-align:left;">Campo</th>
                      <th style="padding:10px; text-align:left;">Valor</th>
                    </tr>
                    <tr>
                      <td style="padding:8px; border-bottom:1px solid #ddd;">Job</td>
                      <td style="padding:8px; border-bottom:1px solid #ddd;">${env.JOB_NAME}</td>
                    </tr>
                    <tr>
                      <td style="padding:8px; border-bottom:1px solid #ddd;">Build</td>
                      <td style="padding:8px; border-bottom:1px solid #ddd;">#${env.BUILD_NUMBER}</td>
                    </tr>
                    <tr>
                      <td style="padding:8px;">Resultado</td>
                      <td style="padding:8px; font-weight:bold; color:${currentBuild.currentResult == 'SUCCESS' ? '#27ae60' : '#c0392b'};">
                        ${currentBuild.currentResult}
                      </td>
                    </tr>
                  </table>
                  <p style="margin-top:15px;">📎 Se adjunta el reporte en formato HTML.</p>
                  <p>🔗 <a href="${env.BUILD_URL}" style="color:#2980b9;">Ver detalles en Jenkins</a></p>
                </body>
                </html>
                """,
                attachmentsPattern: "reporte.html",
                attachLog: false
            )
        }
    }
}
