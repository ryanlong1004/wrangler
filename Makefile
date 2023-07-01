default:

build:
	python -m build
	twine check dist/*

update-dependencies:
	pip-compile --extra dev pyproject.toml

install:
	pip install -e .

install-dev:
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
