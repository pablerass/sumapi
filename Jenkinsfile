node {
	stage 'Test'
	docker.image('python:3.5').inside {
		checkout scm
		withEnv(["HOME=${env.WORKSPACE}",
				 "PATH=${env.WORKSPACE}/.local/bin:${env.PATH}",
				 "PYTHONPATH=${env.WORKSPACE}/.local/lib/python3.5:${env.PYTHONPATH}"]) {
			sh 'pip install --user -r requirements.txt -r requirements-dev.txt'
			sh 'flake8 .'
			sh 'nosetests'
		}
	}
}