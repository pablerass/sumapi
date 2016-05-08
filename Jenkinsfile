node {
	docker.image('python:3').inside {
		stage 'Build and test'
		checkout scm
		sh 'pip install -r requirements.txt -r requirements-dev.txt'
	}
}