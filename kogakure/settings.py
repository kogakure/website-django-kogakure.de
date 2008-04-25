#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# (ɔ) Copyleft 2007-2008 Stefan Imhoff
# Licensed under the GNU General Public License, version 3.
# http://www.gnu.org/copyleft/gpl.txt

import os
import platform

LOCAL_DEVELOPMENT = ('webXX.webfaction.com' not in platform.node())
PROJECT_ROOT = os.path.dirname(__file__)

ADMINS = (('Max Mustermann', 'max@mustermann.de'),)
MANAGERS = ADMINS

if LOCAL_DEVELOPMENT:
    DEBUG = True
    CACHE_BACKEND = 'dummy:///'
    TEMPLATE_DEBUG = DEBUG
    WEB_URL = 'http://127.0.0.1:8000/'
    MEDIA_URL = '%smedia/' % WEB_URL
    ADMIN_MEDIA_PREFIX = '/admin_media/'
    DATABASE_ENGINE = 'sqlite3'
    DATABASE_NAME = 'kogakure.db'
else:
    DEBUG = False
    CACHE_BACKEND = 'memcached://IP:PORT/'
    WEB_URL = 'http://kogakure.de/'
    MEDIA_URL = 'http://media.kogakure.de/'
    ADMIN_MEDIA_PREFIX = 'http://media.kogakure.de/admin_media/'
    DATABASE_ENGINE = 'postgresql_psycopg2'
    DATABASE_NAME = 'DATABASE_NAME'
    DATABASE_USER = 'DATABASE_USER'
    DATABASE_PASSWORD = 'DATABASE_PASSWORD'
    DATABASE_HOST = 'localhost'
    DATABASE_PORT = ''

DEFAULT_FROM_EMAIL = 'max@mustermann.de'
EMAIL_HOST = 'SMTP'
EMAIL_HOST_USER = 'SMTP_USER'
EMAIL_HOST_PASSWORD = 'SMTP_USER_PASSWORD'
EMAIL_PORT = '587'

SITE_ID = 1
APPEND_SLASH = False
REMOVE_WWW = False

TIME_ZONE = 'Europe/Berlin'
LANGUAGE_CODE = 'de-de'
USE_I18N = True
DEFAULT_CHARSET = 'utf-8'

MEDIA_ROOT = '%s/media/' % PROJECT_ROOT

# Secret Key
try:
    SECRET_KEY
except:
    SECRET_FILE = os.path.join(PROJECT_ROOT, 'secret.txt')
    try:
        SECRET_KEY = open(SECRET_FILE).read().strip()
    except IOError:
        try:
            from random import choice
            SECRET_KEY = ''.join([choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
            secret = file(SECRET_FILE, 'w')
            secret.write(SECRET_KEY)
            secret.close()
        except IOError:
            raise Exception('Please create a %s file with random characters to generate your secret key!' % SECRET_FILE)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    'django.middleware.doc.XViewMiddleware',
)

ROOT_URLCONF = 'kogakure.urls'

TEMPLATE_DIRS = (
    '%s/templates' % PROJECT_ROOT,
)

FIXTURE_DIRS = (
    '%s/fixtures' % PROJECT_ROOT,
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'kogakure.context_processors.media_url',
    'kogakure.context_processors.web_url',
    'kogakure.context_processors.django_version',
    'django.core.context_processors.auth',
    'django.core.context_processors.request',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.markup',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.flatpages',
    'django.contrib.redirects',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.sitemaps',
    'kogakure.lib',
    'kogakure.apps.articles',
    'kogakure.apps.blog',
    'kogakure.apps.encyclopedia',
    'kogakure.apps.products',
    'kogakure.apps.proverbs',
)

# Local settings
try:
    from local_settings import *
except ImportError:
    try:
        from mod_python import apache
        apache.log_error('local_settings.py not set; using default settings', apache.APLOG_NOTICE)
    except ImportError:
        import sys
        sys.stderr.write('local_settings.py not set; using default settings\n')