#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# (ɔ) Copyleft 2007-2008 Stefan Imhoff
# Licensed under the GNU General Public License, version 3.
# http://www.gnu.org/copyleft/gpl.txt

import datetime
from django.db import models
from django.db.models import permalink

class Entry(models.Model):
    '''An blog entry'''
    ENTRY_STATUS_CHOICES = (
        ('D', u'Entwurf'),
        ('P', u'Veröffentlicht'),
        ('C', u'Geschlossen'),
    )
    title = models.CharField(u'Titel', max_length=200, null=False, blank=False)
    slug = models.SlugField(u'URL-Titel', unique=True, prepopulate_from=('title',), max_length='150', null=False, blank=False)
    pub_date = models.DateTimeField(u'Veröffentlicht', null=False, blank=False)
    summary = models.TextField(u'Auszug', null=False, blank=False, help_text=u'Markdown benutzen')
    body = models.TextField(u'Kurzmeldung', null=False, blank=False, help_text=u'Markdown benutzen')
    status = models.CharField(max_length=1, null=False, blank=False, choices=ENTRY_STATUS_CHOICES, radio_admin=True, default=1)
    
    class Meta:
        db_table = 'blog_entries'
        verbose_name = u'Kurzmeldung'
        verbose_name_plural = u'Kurzmeldungen'
        ordering = ('-pub_date',)
        get_latest_by = 'pub_date'
    
    class Admin:
        list_display = (
            'title',
            'status',
            'pub_date'
        )
        list_filter = ('pub_date',)
        search_fields = (
            'title',
            'summary',
            'body'
        )
        fields = (
            (u'Datum', {
                'classes': 'collapse wide',
                'fields': ('pub_date',)
            }),
            (None, {
                'classes': 'wide',
                'fields': (
                    'status',
                    'title',
                    'slug',
                    'summary',
                    'body'
                )
            }),
        )
            
    def __unicode__(self):
        return self.title
    
    @permalink
    def get_absolute_url(self):
        return ('kurzmeldungen', (), { 'slug': self.slug })
    