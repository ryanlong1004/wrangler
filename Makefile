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
	twine upload dist/* --verbose --skip-existing

lint:
	pylint **/[^_]*.py && echo "linting"
