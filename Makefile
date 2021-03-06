install:
	poetry install

gendiff:
	poetry run gendiff

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install dist/*.whl

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest -vv --color=yes

print:
	poetry run gendiff --format stylish  fixtures/file1.json fixtures/file2.json > res