from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'letran',
        'USER': 'postgres',
        'PASSWORD': '123.abcd',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]
STATIC_ROOT = BASE_DIR.child('staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')

EMAIL_HOST  = 'smtp.googlemail.com'
EMAIL_PORT  = 587
EMAIL_HOST_USER = 'firstsource.net2020@gmail.com'
EMAIL_HOST_PASSWORD = '123.abcd*'
EMAIL_USE_TLS = True
