# https://opensource.com/article/18/8/what-how-makefile

# brew install jupyterlab

clean:
	rm -rf venv

venv:
	python3 -m venv venv
	. venv/bin/activate; pip install --upgrade pip; pip install --upgrade -r requirements.txt

run: venv
	#. venv/bin/activate; jupyter lab
	. venv/bin/activate; python3 test.py
