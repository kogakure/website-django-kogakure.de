import platform

LOCAL_DEVELOPMENT = ('webXX.webfaction.com' not in platform.node())

if LOCAL_DEVELOPMENT:
    # Debug Settings
    DEBUG = True
    TEMPLATE_DEBUG = DEBUG

    # Database Settings
    DATABASE_ENGINE = 'sqlite3'
    DATABASE_NAME = 'kogakure.db'

    # Media Settings
    WEB_URL = 'http://127.0.0.1:8000/'
    MEDIA_URL = '%smedia/' % WEB_URL
    ADMIN_MEDIA_PREFIX = '/admin_media/'

    # Cache Settings
    CACHE_BACKEND = 'dummy:///'
else:
    # Debug Settings
    DEBUG = False
    TEMPLATE_DEBUG = DEBUG
    
    # Database Settings
    DATABASE_ENGINE = 'postgresql_psycopg2'
    DATABASE_NAME = 'DATABASE_NAME'
    DATABASE_USER = 'DATABASE_USER'
    DATABASE_PASSWORD = 'DATABASE_PASSWORD'
    DATABASE_HOST = 'localhost'

    # Media Settings
    WEB_URL = 'http://domain.de/'
    MEDIA_URL = 'http://media.domain.de/'
    ADMIN_MEDIA_PREFIX = 'http://media.domain.de/admin_media/'
    
    # Cache Settings
    CACHE_BACKEND = 'memcached://IP:PORT/'

# Email Settings
ADMINS = (('Max Mustermann', 'max@mustermann.de'),)
MANAGERS = ADMINS
DEFAULT_FROM_EMAIL = 'max@mustermann.de'
SERVER_EMAIL = 'server@mustermann.de'
EMAIL_HOST = 'SMTP'
EMAIL_HOST_USER = 'SMTP_USER'
EMAIL_HOST_PASSWORD = 'SMTP_USER_PASSWORD'
EMAIL_PORT = '587'

# Application Settings
INSTALLED_APPS = (
    # kogakure
    'lib',
    'articles',
    'blog',
    'encyclopedia',
    'products',
    'proverbs',

    # Django Core
    'django.contrib.auth',
    'django.contrib.markup',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.flatpages',
    'django.contrib.redirects',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.sitemaps',
)