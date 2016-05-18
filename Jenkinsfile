node {
	stage 'Test'
	docker.image('pablerass/python-builder').inside {
		bash 'rm -Rf *'
		checkout scm
		bash 'virtualenv dev'
		bash 'source dev/bin/activate && pip install -r requirements.txt -r requirements-dev.txt'
		bash 'source dev/bin/activate && flake8 --exclude=dev,test .'
		bash 'source dev/bin/activate && nosetests -e dev'
	}
}