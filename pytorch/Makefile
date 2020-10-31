UID ?= $(shell id -u) # to set UID of container user to match host
GID ?= $(shell id -g) # to set GID of container user to match host
USER_PASSWORD ?= password # container user password (for sudo)

.PHONY: build
build:
	docker-compose stop
	docker-compose build --no-cache --build-arg UID=$(UID) --build-arg GID=$(GID) --build-arg USER_PASSWORD=$(USER_PASSWORD) dimvr-pytorch

.PHONY: run
run:
	docker-compose stop
	docker-compose up -d dimvr-pytorch

.PHONY: terminal
terminal:
	docker-compose run dimvr-pytorch bash