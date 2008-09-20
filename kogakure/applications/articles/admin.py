#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# (ɔ) Copyleft 2007-2008 Stefan Imhoff
# Licensed under the GNU General Public License, version 3.
# http://www.gnu.org/copyleft/gpl.txt

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from models import Author, Category, Entry

class AuthorAdmin(admin.ModelAdmin):
    list_display = ( 'preview_image_url', 'last_name', 'first_name',)

admin.site.register(Author, AuthorAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)

class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'pub_date',)
    list_filter = ('categories', 'pub_date', 'author',)
    date_hierarchy = 'pub_date'
    search_fields = ('title', 'summary', 'body',)
    prepopulated_fields = {'slug': ('title',)}
    radio_fields = {'status': admin.HORIZONTAL}
    filter_horizontal = ('categories',)
    fieldsets = [
        (_(u'Date'), {'fields': ['pub_date'], 
                      'classes': ['wide']}),
        (_(u'Author'), {'fields': ['author', 'translators'], 
                        'classes': ['wide collapse']}),
        (None, {'fields': ['status', 'title', 'slug', 'summary', 'body', 'categories'], 
                'classes': ['wide']}),
    ]

admin.site.register(Entry, EntryAdmin)
