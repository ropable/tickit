"""
Base Django settings for tickit project.
Call and extend these settings by passing --settings=<PATH> to runserver, e.g.

    python manage.py runserver --settings=tickit_project.settings.base
"""
import os
from unipath import Path

# Project paths
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).ancestor(3)

# Application definition
ALLOWED_HOSTS = []
SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = False
TEMPLATE_DEBUG = False
INSTALLED_APPS = (
    'grappelli',  # Needs to be before contrib.admin
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'south',
    'django_wsgiserver',
    'climbs',
)
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
)
ROOT_URLCONF = 'tickit_project.urls'
WSGI_APPLICATION = 'tickit_project.wsgi.application'
ANONYMOUS_USER_ID = -1


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
# NOTE: Handled individually in each env-specific settings file.

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Australia/Perth'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images) and user-uploaded media.
# https://docs.djangoproject.com/en/1.6/howto/static-files/
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
    #'compressor.finders.CompressorFinder',  # TODO: django-compressor
)
