

1) Install virtual environment for python project using 

	virtualenv -p /usr/bin/python3.6 venvdemo

2) Activate created virtual environment using 

	source ./venvdemo/bin/activate 

3) Install all python packages using following command. File 'requiremets.txt' is located in lemonade container

	pip install -r requiremets.txt

4) Migrate db using following comand 

	python manage.py migrate

5) Run the project using 
	
	python manage.py runserver

	Developement server will run on localhost with port of 8000

6) Admin Username: akash.pagar and password: akash12345

7) Call User login API and proceed to use inventory API's
