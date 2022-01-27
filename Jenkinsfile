pipeline {
    agent any 
    stages {
		stage('Pull Repo.') {
			steps {
				echo 'Sucess get the webhook by Github.'
				sh '''#!/bin/bash
				cd ~/TW-Finance-Analysis
				git pull
				'''
				echo 'Sucess pull down github repo.'
			}
		}
        stage('Run Beckend') {
            steps {
				echo 'Run backend server...'
				sh '''#!/bin/bash
				echo 'Run backend server...'
				cd ~/TW-Finance-Analysis/backend
				set FLASK_APP=main.py
				python3 -m flask run
				'''
				echo 'Sucess run backend server!'
            }
        }
	}
}
