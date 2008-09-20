#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# (ɔ) Copyleft 2007-2008 Stefan Imhoff
# Licensed under the GNU General Public License, version 3.
# http://www.gnu.org/copyleft/gpl.txt

def media_url(request):
    '''Makes the MEDIA_URL setting available to all templates.'''
    from django.conf import settings
    return {'MEDIA_URL': settings.MEDIA_URL}

def web_url(request):
    '''Makes the WEB_URL setting available to all templates.'''
    from django.conf import settings
    return {'WEB_URL': settings.WEB_URL}

def django_version(request):
    '''Makes the URL_VALIDATOR_USER_AGENT setting available to all templates.'''
    from django.conf import settings
    return {'DJANGO_VERSION': settings.URL_VALIDATOR_USER_AGENT}