# Lifeideology

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

