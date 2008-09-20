#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# (ɔ) Copyleft 2007-2008 Stefan Imhoff
# Licensed under the GNU General Public License, version 3.
# http://www.gnu.org/copyleft/gpl.txt

from django.template import Library, Node
from django.conf import settings
from django.utils.safestring import mark_safe
from lib.markdown import markdown

register = Library()

@register.filter
def smarttext(content):
    '''
    Replaces the String "{{ MEDIA_URL }}" and "{{ WEB_URL }}" in text and 
    renders content with markdown:
    
    {{ content|smarttext }}
    '''
    content = content.replace('{{ MEDIA_URL }}', settings.MEDIA_URL)
    content = content.replace('{{ WEB_URL }}', settings.WEB_URL)
    content = markdown(content)
    return mark_safe(content)
