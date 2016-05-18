node {
	stage 'Code test'
	docker.image('pablerass/python-builder').inside {
		sh 'rm -Rf *'
		checkout scm
		sh 'virtualenv dev'
		sh 'dev/bin/activate && pip install -r requirements.txt -r requirements-dev.txt'
		sh 'dev/bin/activate && flake8 --exclude=dev,test .'
	}

	stage 'Test versions'
	def version_stages = [:]
	def versions = [ '2.7', '3.4', '3.5' ]
	for (version in versions) {
		version_stages = {
			stage 'Test " + $version
			node {
				docker.image('pablerass/python-builder' + version).inside {
					sh 'rm -Rf *'
					checkout scm
					sh 'virtualenv dev'
					sh 'dev/bin/activate && pip install -r requirements.txt -r requirements-dev.txt'
					sh 'dev/bin/activate && nosetests -e dev'
				}
			}
		}
	}
	parallel version_stages
}