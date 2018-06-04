# Django Issue Tracker

A simple issue tracker in Django

## Features

* Django 2.0 and Python 3.6
* Pipenv for virtualenv

## First-time setup

1.  Make sure Python 3.6x and Pipenv are already installed
2.  Clone the repo and configure the virtualenv

```
git clone https://github.com/rayray1/django-issue-tracker.git
cd django-issue-tracker
pipenv install
pipenv shell
```

3.  Set up the initial migration and build the database

```
python manage.py makemigrations applications
python manage.py migrate
```

4.  Create a superuser account

```
python manage.py createsuperuser
(username = admin)
(password = password123)
```

5.  Confirm everything is working and login via the django admin page

```
python manage.py runserver
```

Load the site at http://127.0.0.1:8000/admin
