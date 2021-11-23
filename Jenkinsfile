pipeline { 
agent any
    stages {
        stage('Clone Git Repository') {
            steps {
                git 'https://github.com/alpineFrost/Jenkins_Demo.git'
            }
        }
        stage('Run Code') {
            steps {
                sh "/usr/bin/python3 main.py"
            }
        }
     stage('Test Code') {
            steps {
                sh "/usr/bin/python3 test.py"
            }
        }
    } 
}
