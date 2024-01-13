

* Install virtual environment for python project using 

	virtualenv -p /usr/bin/python3.6 venvdemo

* Activate created virtual environment using 

	source ./venvdemo/bin/activate 

* Install all python packages using following command. File 'requiremets.txt' is located in lemonade container

	pip install -r requiremets.txt

* Migrate db using following comand 

	python manage.py migrate

* Run the project using 
	
	python manage.py runserver

	Developement server will run on localhost with port of 8000

* Call User login API and proceed to use inventory API's
