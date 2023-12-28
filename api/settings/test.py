from api.settings.base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'testdb', # This is where you put the name of the db file. 
                 # If one doesn't exist, it will be created at migration time.
    }
}
