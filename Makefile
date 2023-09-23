.PHONY: fmt install keys run

fmt:
	black .

install:
	pip install -r requirements.txt &&\
	pip install -r requirements-dev.txt

keys:
	mkdir -p keys &&\
	openssl genrsa -out keys/private.pem 2048 &&\
	openssl rsa -in keys/private.pem -outform PEM -pubout -out keys/public.pem

run:
	flask run
