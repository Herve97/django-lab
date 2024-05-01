#Django installation process windows on cmd

python -m venv venv

venv\Scripts\activate

pip install django

django-admin startproject mysite

# Pour créer une autre application
python manage.py startapp firstapp

# make migrations
python manage.py makemigrations

# Run migration to active model
python3 manage.py migrate

# Run the main app
python manage.py runserver

# create super user for admin page
python manage.py createsuperuser

# docker cmd
docker build . -t my-django-app:latest && docker run -e PYTHONUNBUFFERED=1 -p  8000:8000 my-django-app

# Linux
pip install virtualenv
virtualenv djangoenv
source djangoenv/bin/activate