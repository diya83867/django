# Blog Project

## Create Virtualenv with Python3 in Linux, Ubuntu or MAC
	virtualenv blogenv -p python3

## Create Virtualenv with Python3 in Windows
	python -m venv blogenv

## Activate Virtualenv in Linux, Ubuntu or MAC
	source blogenv/bin/activate

## Activate Virtualenv in Windows
	. blogenv\Scripts\activate

## Install Django with pip
	pip install django

## Update requirements.txt file
	pip freeze > requirements.txt

## To find installed requirements with version
	pip freeze | grep django

## Start New Project in Django
	django-admin startproject mergeall

## Create New App in Django
	python manage.py startapp blog
	python manage.py startapp pollapp

## Run Django
	python manage.py runserver
	python manage.py runserver 8080
	python manage.py runserver 0:8000
	python manage.py runserver 192.168.1.134:8000

## Create Superuser
	python manage.py createsuperuser

## Reset user Password from Terminal
	python manage.py changepassword username

## Makemigrations of Project or Single App
	python manage.py makemigrations
	python manage.py makemigrations blog

## Migrate Project or Single App
	python manage.py migrate
	python manage.py migrate blog
	python manage.py migrate --fake
	python manage.py migrate blog --fake

## Install Requirements 
1. pip install mysqlclient
2. pip install celery
3. pip install redis
4. sudo apt-get install redis-server
5. redis-server
6. redis-cli ping
7. sudo service redis-server start
8. sudo apt-get install mysql-server
9. sudo apt-get install libmysqlclient-dev

## Run Celery
1. celery -A .celery_redis worker --loglevel=info

## Create user in mysql
1. sudo mysql;
2. CREATE USER 'flask'@'localhost' IDENTIFIED BY 'flask';
3. GRANT ALL PRIVILEGES ON *.* TO 'flask'@'localhost' WITH GRANT OPTION;
4. FLUSH PRIVILEGES;

## Create database in mysql
1. create database flask;

## KILL THE RUNNING PROCCESS OF CELERY AND BEATS
1. kill -9 $(ps aux | grep celery | grep -v grep | awk '{print $2}' | tr '\n'  ' ') > /dev/null 2>&1