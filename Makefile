# ----------------------------------
#          INSTALL & TEST
# ----------------------------------
install_requirements:
	@pip install -r requirements.txt


test:
	@pytest -v tests
	


clean:
	@rm -f */version.txt
	@rm -f .coverage
	@rm -fr */__pycache__ */*.pyc __pycache__
	@rm -fr build dist
	@rm -fr mammography-*.dist-info
	@rm -fr mammography.egg-info


install:
	@pip install . -U

all: clean install test