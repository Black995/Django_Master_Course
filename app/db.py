import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_course',
        'USER': 'postgres',
        'PASSWORD': '12345',
        'HOST': 'localhost',
        'POST': '5432'
    }
}
    

