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

class ContentNode(Node):
    def __init__(self, model, num, varname, order_type):
        self.num, self.varname = num, varname
        self.modelname = model
        self.order_type = order_type
        self.model = get_model(*model.split('.'))
    
    def render(self, context):
        context[self.varname] = self.model._default_manager.filter(status='P', pub_date__lte=datetime.datetime.now()).order_by(self.order_type)[:self.num]
        return ''

@register.tag
def get_all(parser, token):
    '''
    Loads a specific number of entries from a model in a context and orders them as wished:
    
    {% get_all model.Model maxnum as varname order_by field %}
    '''
    bits = token.contents.split()
    if len(bits) != 7:
        raise TemplateSyntaxError, 'get_all tag takes exactly six arguments'
    if bits[3] != 'as':
        raise TemplateSyntaxError, 'third argument to get_all tag must be "as"'
    return ContentNode(bits[1], bits[2], bits[4], bits[6])
