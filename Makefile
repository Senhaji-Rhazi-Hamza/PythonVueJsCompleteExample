include .env

VARS:=$(shell sed -ne 's/ *\#.*$$//; /./ s/=.*$$// p' .env )
 $(foreach v,$(VARS),$(eval $(shell echo export $(v)="$($(v))")))

.PHONY: clean
clean: clean_pyc clean_tmp_t-ipynb

FILES:=  $(shell export $(cat .env | xargs))


.PHONY: clean_pyc
clean_pyc:
	find . -name "*pyc" -exec rm -f {} \;

clean_tmp_t-ipynb:
	find . -name "t-*ipynb" -exec rm -f {} \;



.PHONY: requirements
requirements:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt


run_back:
	python3 api/server.py

populate:
	python3 api/db/populate.py
	
run_front: 
	cd ui; yarn serve
