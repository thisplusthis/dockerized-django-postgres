# core/settings/base.py

import os

from django.core.exceptions import ImproperlyConfigured


def get_env_variable(var_name, *args):
    """get an environment variable or return an exception
    """
    try:
        return os.environ[var_name]
    except KeyError:
        if args:
            return args[0]
        raise ImproperlyConfigured("Missing %s in environment" % var_name)


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SECRET_KEY = get_env_variable('DJANGO_SECRET_KEY')
DEBUG = get_env_variable('DJANGO_DEBUG')
ALLOWED_HOSTS = []
ADMINISTRATOR_EMAIL = 'test@tester.com'
ADMINS = (
    ('Testy McTesterson', ADMINISTRATOR_EMAIL),
)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'
APP_TEMPLATES = []
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        "DIRS": [
            os.path.join(BASE_DIR, "core/templates"),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "middleware.context.environment",  # custom context processor
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
