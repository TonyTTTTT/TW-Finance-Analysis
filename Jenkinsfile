pipeline {
    agent any 
    stages {
        stage('Run Beckend') {
            steps {
				echo 'Sucess fetch github repo.'
            }
			steps {
				echo 'Run backend server...'
				sh '''#!/bin/bash
				cd backend
				set FLASK_APP=main.py
				python3 -m flask run
				echo 'Sucess run backend server!'
			}
        }
	}
}
