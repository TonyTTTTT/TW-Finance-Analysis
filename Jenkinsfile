pipeline {
    agent any 
    stages {
		stage('Pull Repo.') {
			steps {
				echo 'Sucess get the webhook by Github.'
				sh '''#!/bin/bash
				cd ~/TW-Finance-Analysis
				git pull https://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@github.com/TonyTTTTT/TW-Finance-Analysis.git
				'''
				echo 'Sucess pull down github repo.'
			}
		}
        stage('Run Beckend') {
            steps {
				echo 'Run backend server...'
				sh '''#!/bin/bash
				cd ~/TW-Finance-Analysis/backend
				export FLASK_APP=main.py
				nohup python3 -m flask run
				'''
				echo 'Sucess run backend server!'
            }
        }
	}
}
