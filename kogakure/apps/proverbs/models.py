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
    '''An proverb entry'''
    ENTRY_STATUS_CHOICES = (
        ('D', u'Entwurf'),
        ('P', u'Veröffentlicht'),
        ('C', u'Geschlossen'),
    )
    pub_date = models.DateTimeField('Veröffentlicht', null=False, blank=False)
    body = models.TextField('Spruch', null=False, blank=False, help_text='Markdown benutzen, mit Anführungszeichen')
    author = models.CharField('Autor', null=False, blank=False, max_length=150)
    status = models.CharField(max_length=1, null=False, blank=False, choices=ENTRY_STATUS_CHOICES, radio_admin=True, default=1)
    
    class Meta:
        db_table = 'proverb_entries'
        verbose_name = 'Spruch'
        verbose_name_plural = 'Sprüche'
        ordering = ('-pub_date',)
        get_latest_by = 'pub_date'
    
    class Admin:
        list_display = (
            'body',
            'status',
            'pub_date'
        )
        list_filter = ('pub_date',)
        search_fields = ('body',)
        fields = (
            ('Datum', {
                'classes': 'collapse wide',
                'fields': ('pub_date',), 
            }),
            (None, {
                'classes': 'wide',
                'fields': (
                    'status',
                    'body',
                    'author'
                )
            }),
        )
            
    def __unicode__(self):
        return self.body
    
    @permalink
    def get_absolute_url(self):
        return ('sprueche', (), { 'object_id': self.id })
    