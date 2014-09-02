"""
Local development Django settings for prs2 project.
Extends the base settings.
"""
from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = ['*']

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
    '--verbosity=2',  # Nice, but tests take longer to run.
    '--detailed-errors']
SOUTH_TESTS_MIGRATE = False

# Debug Toolbar settings.
DEBUG_TOOLBAR_PATCH_SETTINGS = False
