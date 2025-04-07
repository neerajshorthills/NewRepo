pipeline {
    agent any

    environment {
        PYTHON_BIN = "/Library/Frameworks/Python.framework/Versions/3.13/bin"
        PATH = "${env.PATH}:${env.PYTHON_BIN}"
    }

    stages {
        stage('Run Test Shell Script') {
            steps {
                echo "Executing shell script to run test cases..."
                sh 'bash mail-test.sh'
            }
        }
    }

    post {
        always {
            echo "Sending email with HTML report..."

            emailext(
                subject: "${currentBuild.currentResult}: ${env.JOB_NAME} Build #${env.BUILD_NUMBER}",
                body: """
                    <p>Hi Team,</p>
                    <p>Build <b>${env.JOB_NAME} #${env.BUILD_NUMBER}</b> has <b>${currentBuild.currentResult}</b>.</p>
                    <p>Please find the test report attached.</p>
                    <p>Thanks,<br/>Jenkins</p>
                """,
                to: 'neeraj.kumar2@shorthills.ai',
                attachmentsPattern: 'report.html',
                mimeType: 'text/html'
            )
        }
    }
}
