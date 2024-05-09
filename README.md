# Flavours Fusion
Online Recipes Sharing Platform

### Technology

_Backend_

> - Python 3.9.18
> - Django 4.2.13 
> - djangorestframework==3.15.1
> - database - sqlite


### Project Set-Up

1. Clone the repository

    ``
        git clone url
    ``

2. Create Virtual environment

   ``
      virtualenv flavours_venv
   ``
3. Install Dependencies 

    > kindly make sure your virtual environment is active.

     ``
        pip install -r requirements.tx  
     ``

4. Create & Run Migrations

    ``
    - python manage.py makemigrations
    - python manage.py migrate
    ``

5. Create Superuser

    ``
    python manage.py createsuperuser
    ``

6. Run Project

    ``
    python manage.py runserver
    ``


#### Admin Panel

- http://localhost:8000/admin/
