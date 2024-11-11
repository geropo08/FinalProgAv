pipeline {
    agent any
    parameters {
        
        choice(name: "TEST_CHOICE", choices: ["trivia", "procesarDatos", "USQL"], description: "Sample multi-choice parameter")
    }
    stages {
        stage("Build") {
            steps {
                script {
                    echo "Building trivia"
                    if (params.TEST_CHOICE == "trivia") {
                        dir('Entregable1') {
                            bat 'dir' 
                            echo "Building trivia"// For Windows
                        }
                       
            
                        //sh 'python main.py' 
                        //sh 'python tests.py'
                    } else if (params.TEST_CHOICE == "procesar pedidos") {
                        echo "Building procesar_pedido"
                        //sh 'javac -d out -sourcepath src src/main/java/org/yourcompany/yourproject/*.java'
                        //sh 'java -cp out org.yourcompany.yourproject.PedidoProcessor'
                        //sh 'mvn clean test'
                        
                        
                    } else if (params.TEST_CHOICE == "USQL") {
                        echo "Building USQL"
                        bat 'pip install ply'
                        bat 'pip install pytest'
                        bat 'pip install pytest-cov'
                        //sh 'python BD.py'
                        //sh 'python main.py'
                        //sh 'pytest --cov=traductorSQL --cov=DSL --cov-report=html --cov-report=term-missing'

                    }

                }
            }
        }
        stage("Test") {
            steps {
                echo "Test stage."
            }
        }
        
    }
}
