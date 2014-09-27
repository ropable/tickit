honcho run python manage.py syncdb --migrate --noinput --settings=tickit_project.settings.local
honcho run python manage.py loaddata --settings=tickit_project.settings.local tickit_project/fixtures/sites.json
honcho run python manage.py loaddata --settings=tickit_project.settings.local tickit_project/fixtures/socialapp.json
honcho run python manage.py loaddata --settings=tickit_project.settings.local climbs/fixtures/test-business.json
honcho run python manage.py loaddata --settings=tickit_project.settings.local climbs/fixtures/test-wall.json
honcho run python manage.py loaddata --settings=tickit_project.settings.local climbs/fixtures/test-rope.json
honcho run python manage.py loaddata --settings=tickit_project.settings.local climbs/fixtures/test-climb.json
