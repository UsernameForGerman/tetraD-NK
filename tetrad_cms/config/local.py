from .base import *

# GENERAL
# ------------------------------------------------------------------------------
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', ' ').split(' ')

# REST FRAMEWORK
# ------------------------------------------------------------------------------
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.AllowAny', ),
    'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework.authentication.TokenAuthentication', ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.JSONParser',
    )
}

# CORS
# ------------------------------------------------------------------------------
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('POSTGRES_DB'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': os.environ.get('POSTGRES_HOST'),
        'PORT': os.environ.get('POSTGRES_PORT'),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.dummy',
#     }
# }

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
STATIC_ROOT = os.path.join(DATA_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'core', 'static'),
)
SITE_ID = 1

