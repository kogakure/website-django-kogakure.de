#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# (ɔ) Copyleft 2007-2008 Stefan Imhoff
# Licensed under the GNU General Public License, version 3.
# http://www.gnu.org/copyleft/gpl.txt

import datetime
from django.views.decorators.cache import cache_page
from django.views.generic.list_detail import object_list, object_detail
from models import *

@cache_page(60 * 60)
def generic_wrapper_list(request, *args, **kwargs):
    if request.user.is_anonymous():
        queryset = Entry.objects.filter(status='P', pub_date__lte=datetime.datetime.now()).order_by('category', 'title')
    else:
        queryset = Entry.objects.all().order_by('category', 'title')
    return object_list(request, queryset, *args, **kwargs)

@cache_page(60 * 60)
def generic_wrapper_detail(request, *args, **kwargs):
    if request.user.is_anonymous():
        queryset = Entry.objects.filter(status='P', pub_date__lte=datetime.datetime.now())
    else:
        queryset = Entry.objects.all()
    return object_detail(request, queryset, *args, **kwargs)