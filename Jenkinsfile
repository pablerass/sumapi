node {
	stage 'Test'
	docker.image('pablerass/python-builder').inside {
		sh 'rm -Rf *'
		checkout scm
		sh 'virtualenv dev'
		sh 'dev/bin/activate && pip install -r requirements.txt -r requirements-dev.txt'
		sh 'dev/bin/activate && flake8 --exclude=dev,test .'
		sh 'dev/bin/activate && nosetests -e dev'
	}
}