pipeline {
    agent any

    environment {
        PYTHON_BIN = "/Library/Frameworks/Python.framework/Versions/3.13/bin"
        PATH = "${env.PATH}:${env.PYTHON_BIN}"
    }

    stages {
        stage('Run Tests') {
            steps {
                sh 'bash mail-test.sh'
            }
        }
    }

    post {
        always {
            emailext(
                to: 'neeraj.kumar2@shorthills.ai',
                subject: "Build ${env.BUILD_NUMBER} - ${currentBuild.currentResult}",
                body: """
                    <p>Hi,</p>
                    <p>The build <b>${env.JOB_NAME} #${env.BUILD_NUMBER}</b> has <b>${currentBuild.currentResult}</b>.</p>
                    <p>Attached is the test report.</p>
                    <p>Regards,<br/>Jenkins</p>
                """,
                mimeType: 'text/html',
                attachmentsPattern: 'report.html'
            )
        }
    }
}
