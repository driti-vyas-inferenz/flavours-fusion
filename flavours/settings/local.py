from .base import *

SECRET_KEY = 'This_Is_SEcret!!'

DEBUG = True

ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': PARENT_DIR / 'db.sqlite3',
    }
}