#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# (ɔ) Copyleft 2007-2008 Stefan Imhoff
# Licensed under the GNU General Public License, version 3.
# http://www.gnu.org/copyleft/gpl.txt

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from kogakure.apps.products.models import Category, Entry

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)

class EntryAdmin(admin.ModelAdmin):
    list_display = ('preview_image_url', 'title', 'category', 'status', 
                    'pub_date',)
    list_filter = ('category',)
    search_fields = ('title', 'asin', 'body',)
    prepopulated_fields = {'slug': ('title',)}
    radio_fields = {'status': admin.HORIZONTAL}
    fieldsets = [
        (_('Date'), {'fields': ['pub_date'],
                      'classes': ['wide']}),
        (None,       {'fields': ['status', 'title', 'slug', 'cover', 'asin', 'category', 'body'],
                      'classes': ['wide']}),
    ]

admin.site.register(Entry, EntryAdmin)    