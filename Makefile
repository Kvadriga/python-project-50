install:
	poetry install
gendiff:
	poetry run gendiff $(X)?
lint:
	poetry run flake8 gendiff



.PHONY: gendiff
