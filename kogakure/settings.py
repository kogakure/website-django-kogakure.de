#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# (ɔ) Copyleft 2007-2008 Stefan Imhoff
# Licensed under the GNU General Public License, version 3.
# http://www.gnu.org/copyleft/gpl.txt

import os.path
import sys

# Basic Settings
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'applications'))

# Debug Settings
DEBUG = False
TEMPLATE_DEBUG = DEBUG

# Local Settings
TIME_ZONE = 'Europe/Berlin'
LANGUAGE_CODE = 'de-de'
USE_I18N = True
DEFAULT_CHARSET = 'utf-8'

# Site Settings
SITE_ID = 1
ROOT_URLCONF = 'kogakure.urls'
APPEND_SLASH = False
REMOVE_WWW = False

# Middleware
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    'django.middleware.doc.XViewMiddleware',
)

# Template Settings
TEMPLATE_CONTEXT_PROCESSORS = (
    'lib.context_processors.media_url',
    'lib.context_processors.web_url',
    'lib.context_processors.django_version',
    'django.core.context_processors.auth',
    'django.core.context_processors.request',
)

TEMPLATE_DIRS = (
    '%s/templates' % PROJECT_ROOT,
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

# Fixture Settings
FIXTURE_DIRS = (
    '%s/fixtures' % PROJECT_ROOT,
)

# Secret Key Generator
if not hasattr(globals(), 'SECRET_KEY'):
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
        
    

# Import Local settings
try:
    from local_settings import *
except ImportError:
    try:
        from mod_python import apache
        apache.log_error('local_settings.py not set; using default settings', apache.APLOG_NOTICE)
    except ImportError:
        import sys
        sys.stderr.write('local_settings.py not set; using default settings\n')