# core/settings/dev.py

from .base import *

LOCAL = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    "default": {
        "ENGINE": get_env_variable('DJANGO_DATABASE_ENGINE', 'django.db.backends.sqlite3'),
        "NAME": get_env_variable('DJANGO_DATABASE_NAME', os.path.join(BASE_DIR, 'db.sqlite3')),
        "USER": get_env_variable('DJANGO_DATABASE_USER', 'user'),
        "PASSWORD": get_env_variable('DJANGO_DATABASE_PASSWORD', 'password'),
        "HOST": get_env_variable('DJANGO_DATABASE_HOST', 'localhost'),
        "PORT": get_env_variable('DJANGO_DATABASE_PORT', '5432'),
    }
}