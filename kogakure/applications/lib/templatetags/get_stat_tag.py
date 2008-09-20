#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# (ɔ) Copyleft 2007-2008 Stefan Imhoff
# Licensed under the GNU General Public License, version 3.
# http://www.gnu.org/copyleft/gpl.txt

import datetime
from django.template import Library, Node
from django.template import TemplateSyntaxError
from django.db.models import get_model

register = Library()

class StatNode(Node):
    def __init__(self, model, varname):
        self.varname = varname
        self.modelname = model
        self.model = get_model(*model.split('.'))
    
    def render(self, context):
        context[self.varname] = self.model._default_manager.filter(status='P', pub_date__lte=datetime.datetime.now()).count()
        return ''

@register.tag
def get_stat(parser, token):
    '''
    Returns the Count of an specific model in a variable:
    
    {% get_stat model.Model as varname %}
    '''
    bits = token.contents.split()
    if len(bits) != 4:
        raise TemplateSyntaxError, 'get_stat tag takes exactly four arguments'
    if bits[2] != 'as':
        raise TemplateSyntaxError, 'second argument to get_stat tag must be "as"'
    return StatNode(bits[1], bits[3])
