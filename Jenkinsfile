node {
	docker.image('python:3.5').inside {
		stage 'Test'
		checkout scm
		sh 'export HOME="$WORKSPACE"'
		sh 'export PATH="$WORKSPACE/.local/bin:$PATH"'
		sh 'export PYTHONPATH="$WORKSPACE/.local/lib/python3.5:$PYTHONPATH"'
		sh 'pip install --user -r requirements.txt -r requirements-dev.txt'
		sh 'flake8 .'
		sh 'nosetests'
	}
}