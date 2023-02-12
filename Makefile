install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --force-reinstall dist/*.whl

start:
	poetry run

lint:
	poetry run flake8 diff_finder

.PHONY: install
