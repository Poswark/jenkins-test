######### groovy 
def call() {
  return '''
apiVersion: v1
kind: Pod
metadata:
  labels:
    app: git-cloner
spec:
  containers:
  - name: git
    image: alpine/git:2.45.2
    command: ["/bin/sh"]
    args: ["-c", "sleep 3600"]
    tty: true
    volumeMounts:
    - name: workspace-volume
      mountPath: /home/jenkins/agent
  - name: jnlp
    image: jenkins/inbound-agent:3309.v27b_9314fd1a_4-1
    volumeMounts:
    - name: workspace-volume
      mountPath: /home/jenkins/agent
  volumes:
  - name: workspace-volume
    emptyDir: {}
  restartPolicy: Never
'''
}
################
@Library('shared-library') _
pipeline {
    agent none

    stages {
        stage('Git Clone') {
            agent {
                kubernetes {
                    yaml gitTemplate()
                }
            }
            steps {
                container('git') {
                    sh '''
                      echo "🔹 Clonando repositorio..."
                      git clone https://github.com/Poswark/personal-page.git
                      echo "🔹 Archivos clonados:"
                      ls -la personal-page
                    '''
                }
            }
        }
    }
}
