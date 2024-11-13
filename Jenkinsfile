pipeline {
    agent any
    parameters {
        
        choice(name: "TEST_CHOICE", choices: ["trivia", "procesarDatos", "USQL"], description: "Sample multi-choice parameter")
    }
    stages {
        stage("Build") {
            steps {
                script {
                    
                    if (params.TEST_CHOICE == "trivia") {
                        echo "Building trivia"
                        dir('Entregable1') {
                            echo "Building trivia"// For Windows
                            bat 'python main.py'
                        }
                    } else if (params.TEST_CHOICE == "procesarDatos") {
                        echo "Building procesar_pedido"
                        dir('Entregable2') {
                            bat 'javac -d out -sourcepath src src/main/java/org/yourcompany/yourproject/*.java'
                            bat 'java -cp out org.yourcompany.yourproject.PedidoProcessor'
                        }
                        
                        
                    } else if (params.TEST_CHOICE == "USQL") {
                        dir('Entregable3') {
                            echo "Building USQL"
                            bat 'pip install ply'
                            bat 'pip install pytest'
                            bat 'pip install pytest-cov'
                            bat 'python BD.py'
                            bat 'python main.py'
                        }
                    }

                }
            }
        }
        stage("Test") {
            steps {
                script {
                    if (params.TEST_CHOICE == "trivia") {
                        echo "Building trivia"
                        dir('Entregable1') {
                            echo "Test stage trivia."
                            bat 'python tests.py'
                        }
                    } else if (params.TEST_CHOICE == "procesarDatos") {
                        echo "Testing procesar_pedido"
                        dir('Entregable2') {
                            bat 'mvn clean test'
                        }
                        //sh 'javac -d out -sourcepath src src/main/java/org/yourcompany/yourproject/*.java'
                        //sh 'java -cp out org.yourcompany.yourproject.PedidoProcessor'
                        //sh 'mvn clean test'
                        
                        
                    } else if (params.TEST_CHOICE == "USQL") {
                        dir('Entregable3') {
                            echo "Testing USQL"


                            bat 'pytest --cov=traductorSQL --cov=DSL --cov-report=html --cov-report=term-missing'
                        }
                    }

                }
            }
        }
        
    }
    post {
        success {
                mail to: 'geronimocopiawpp@gmail.com',
                subject: "Build Successful: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: "Good news! The build for ${env.JOB_NAME} #${env.BUILD_NUMBER} succeeded."
                
            
        }
        failure {
                mail to: 'geronimocopiawpp@gmail.com',
                subject: "Build Failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: "Unfortunately, the build for ${env.JOB_NAME} #${env.BUILD_NUMBER} failed."
                
            
        }
    }
}
