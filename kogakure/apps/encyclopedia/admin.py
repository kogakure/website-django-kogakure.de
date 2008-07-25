#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# (ɔ) Copyleft 2007-2008 Stefan Imhoff
# Licensed under the GNU General Public License, version 3.
# http://www.gnu.org/copyleft/gpl.txt

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from kogakure.apps.encyclopedia.models import Entry

class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'japanese', 'explanation', 'status', 'pub_date',)
    list_filter = ('pub_date',)
    search_fields = ('title', 'title_alt', 'japanese', 'explanation',)
    prepopulated_fields = {'slug': ('title',)}
    radio_fields = {'status': admin.HORIZONTAL}
    fieldsets = [
        (_(u'Datum'), {'fields': ['pub_date'], 
                       'classes': ['wide']}),
        (None,        {'fields': ['status', 'title', 'title_alt', 'slug', 'japanese', 'explanation'],
                       'classes': ['wide']}),
    ]

admin.site.register(Entry, EntryAdmin)
    