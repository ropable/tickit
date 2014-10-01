"""
Local development Django settings for prs2 project.
Extends the base settings.
"""
import sys
from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG
TESTING = 'test' in sys.argv
ALLOWED_HOSTS = ['*']
# Req'd to get django-allauth working while we don't have a mail server running.
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Additional apps installed in development env.
INSTALLED_APPS += (
    'debug_toolbar',
    'django_nose',
)

# Development DB: local SQLite3 db.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
ATOMIC_REQUESTS = True

# Test runner settings.
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = [
    '--nologcapture',
    '--with-fixture-bundling',
    '--with-coverage',
    '--cover-package=climbs',
    '--cover-package=people',
    '--cover-package=pages',
    '--verbosity=2',  # Nice, but tests take longer to run.
    '--detailed-errors']

# Debug Toolbar settings.
DEBUG_TOOLBAR_PATCH_SETTINGS = True

