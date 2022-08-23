pipeline {
	agent any 
	stages {
		stage('Pull Repo.') {
			steps {
				echo 'Sucess get the webhook by Github.'
				sh '''#!/bin/bash
				cd ~/TW-Finance-Analysis
				git pull https://{personal_access_token}@github.com/TonyTTTTT/TW-Finance-Analysis.git
				'''
				echo 'Sucess pull down github repo.'
			}
		}
		/*stage('Run Beckend') {
			steps {
				echo 'Run backend server...'
				sh '''#!/bin/bash
				cd ~/TW-Finance-Analysis/backend
				export FLASK_APP=main.py
				nohup python3 -m flask run --port=5050
				'''
				echo 'Sucess run backend server!'
		    }
		}*/
		/*stage('Run Frontend') {
			steps {
				echo 'Run frontend server...'
				sh '''#!/bin/bash
				cd ~/TW-Finance-Analysis/frontend
				npm start
				'''
				echo 'Sucess run frontend server!'
			}
		}*/
	}
}
