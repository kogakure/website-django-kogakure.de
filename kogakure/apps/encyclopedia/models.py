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
    '''An encylopedia entry'''
    ENTRY_STATUS_CHOICES = (
        ('D', u'Entwurf'),
        ('P', u'Veröffentlicht'),
        ('C', u'Geschlossen'),
    )
    title = models.CharField(u'Titel', max_length=200, null=False, blank=False)
    slug = models.SlugField(u'URL-Titel', unique=True, prepopulate_from=('title',), max_length='150', null=False, blank=False)
    pub_date = models.DateTimeField(u'Veröffentlicht', null=False, blank=False)
    title_alt = models.CharField(u'Alternativer Titel', null=True, blank=True, max_length='150')
    japanese = models.CharField(u'Japanische Zeichen', null=True, blank=True, max_length='50', help_text=u'Kanji, Katakana oder Hiragana')
    explanation = models.TextField(u'Erkärung', null=False, blank=False, help_text=u'Markdown benutzen')
    status = models.CharField(max_length=1, null=False, blank=False, choices=ENTRY_STATUS_CHOICES, radio_admin=True, default=1)
    
    class Meta:
        db_table = 'encyclopedia_entries'
        verbose_name = u'Lexikoneintrag'
        verbose_name_plural = u'Lexikoneinträge'
        ordering = ('-pub_date',)
        get_latest_by = 'pub_date'
    
    class Admin:
        list_display = (
            'title',
            'japanese',
            'explanation',
            'status',
            'pub_date'
        )
        list_filter = ('pub_date',)
        search_fields = (
            'title',
            'title_alt',
            'japanese',
            'explanation'
        )
        fields = (
            (u'Datum', {
                'classes': 'collapse wide',
                'fields': ('pub_date',),
            }),
            (None, {
                'classes': 'wide',
                'fields': (
                    'status',
                    'title',
                    'title_alt',
                    'slug',
                    'japanese',
                    'explanation'
                )
            }),
        )
            
    def __unicode__(self):
        return self.title
    
    @permalink
    def get_absolute_url(self):
        return ('lexikon', (), { 'slug': self.slug })
    