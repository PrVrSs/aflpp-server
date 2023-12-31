.PHONY: unit mypy lint test

SHELL := /usr/bin/env bash
GRPC := python -m grpc_tools.protoc


unit:
	poetry run pytest


mypy:
	poetry run mypy aflpp_server


lint:
	poetry run pylint aflpp_server


test: lint mypy unit


proto:
	$(GRPC) -I . \
		--python_out=./aflpp_server \
		--mypy_out=./aflpp_server \
		--grpc_python_out=./aflpp_server \
		./protoc/v1/*.proto