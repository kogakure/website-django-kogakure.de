#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# (ɔ) Copyleft 2007-2008 Stefan Imhoff
# Licensed under the GNU General Public License, version 3.
# http://www.gnu.org/copyleft/gpl.txt

import datetime
from django.views.decorators.cache import cache_page
from django.template import RequestContext
from django import shortcuts
from django.views.generic.list_detail import object_list, object_detail
from kogakure.apps.articles.models import *

@cache_page(60 * 60)
def generic_wrapper_list(request, *args, **kwargs):
    if request.user.is_anonymous():
        queryset = Entry.objects.filter(status='P', pub_date__lte=datetime.datetime.now())
    else:
        queryset = Entry.objects.all()
    return object_list(request, queryset, *args, **kwargs)

@cache_page(60 * 60)
def generic_wrapper_detail(request, *args, **kwargs):
    if request.user.is_anonymous():
        queryset = Entry.objects.filter(status='P', pub_date__lte=datetime.datetime.now())
    else:
        queryset = Entry.objects.all()
    return object_detail(request, queryset, *args, **kwargs)

@cache_page(60 * 60)
def category(request, category_slug):
    category = shortcuts.get_object_or_404(Category, slug=category_slug)
    entries = category.entry_categories.filter(status='P', pub_date__lte=datetime.datetime.now())
    return shortcuts.render_to_response('categories.html', {'category':category, 'entries':entries}, context_instance=RequestContext(request))