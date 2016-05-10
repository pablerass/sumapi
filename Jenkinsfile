node {
	stage 'Test'
	docker.image('pablerass/python-builder').inside {
		checkout scm
		sh 'virtualenv dev'
		sh 'dev/bin/activate && pip install -r requirements.txt -r requirements-dev.txt'
		sh 'dev/bin/activate && flake8 .'
		sh 'dev/bin/activate && nosetests'
	}
}