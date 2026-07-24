.PHONY: install-deps build serve all

install-deps:
	pip install -r requirements.txt

build:
	python scripts/build_content.py

serve:
	python scripts/run_server.py

all: install-deps build
