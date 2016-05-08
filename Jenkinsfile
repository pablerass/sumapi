node {
	def py = docker.image('python:3')
	py.run('pip install -r requirements.txt -r requirements-dev.txt')

	py.inside {
		stage 'Build and test'
		checkout scm
		sh 'flake8 .'
		sh 'nosetests'
	}
}