PYTHON = python
VENV_NAME = venv

venv:
	python -m venv $(VENV_NAME) 
	./$(VENV_NAME)/Scripts/python -m pip install --upgrade pip

.PHONY: setup
setup: venv
	$(VENV_NAME)/Scripts/pip install -r requirements.txt

train:
	./$(VENV_NAME)/Scripts/python -m src.model.train

run:
	./$(VENV_NAME)/Scripts/python -m src.model.model

format:
	./$(VENV_NAME)/Scripts/isort ./src/
	./$(VENV_NAME)/Scripts/black ./src/
	./$(VENV_NAME)/Scripts/flake8 ./src/



