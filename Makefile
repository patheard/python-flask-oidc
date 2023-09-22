.PHONY: fmt install run

fmt:
	black .

install:
	pip install -r requirements.txt &&\
	pip install -r requirements-dev.txt

run:
	flask run
