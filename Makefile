default:

build:
	python -m build
	twine check dist/*

update-dependencies:
	pip-compile --extra dev pyproject.toml

dev:
	pip install -e '.[dev]'

format:
	black .
	docformatter

publish:
	pip-compile --extra dev pyproject.toml
	python -m build
	twine check dist/*
	twine upload dist/*

lint:
	pylint **/[^_]*.py && echo "linting"
	# stop the build if there are Python syntax errors or undefined names
	flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
	# exit-zero treats all errors as warnings.
