PYTHON = python
VENV_NAME = venv

venv:
	python3 -m venv $(VENV_NAME) 
	./$(VENV_NAME)/bin/python3 -m pip install --upgrade pip

.PHONY: setup
setup: venv
	$(VENV_NAME)/bin/pip3 install -r requirements.txt

train:
	./$(VENV_NAME)/bin/python3 -m src.model.train

run:
	./$(VENV_NAME)/bin/python3 -m src.model.model

start:
	gunicorn -w 4 -b 0.0.0.0:8000 src.model.model:app


format:
	./$(VENV_NAME)/Scripts/isort ./src/
	./$(VENV_NAME)/Scripts/black ./src/
	./$(VENV_NAME)/Scripts/flake8 ./src/



