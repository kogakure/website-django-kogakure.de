#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# (ɔ) Copyleft 2007-2008 Stefan Imhoff
# Licensed under the GNU General Public License, version 3.
# http://www.gnu.org/copyleft/gpl.txt

import datetime
from django.db import models
from django.db.models import permalink
from django.utils.translation import ugettext_lazy as _

class Entry(models.Model):
    '''An encylopedia entry'''
    ENTRY_STATUS_CHOICES = (
        ('D', _(u'Draft')),
        ('P', _(u'Published')),
        ('C', _(u'Closed')),
    )
    title = models.CharField(_(u'Title'), max_length=200, null=False, blank=False)
    slug = models.SlugField(_(u'Slug'), unique=True, prepopulate_from=('title',), max_length='150', null=False, blank=False)
    pub_date = models.DateTimeField(_(u'Published'), default=datetime.datetime.now, null=False, blank=False)
    title_alt = models.CharField(_(u'Alternative title'), null=True, blank=True, max_length='150')
    japanese = models.CharField(_(u'Japanese characters'), null=True, blank=True, max_length='50', help_text=_(u'Kanji, Katakana or Hiragana'))
    explanation = models.TextField(_(u'Explanation'), null=False, blank=False, help_text=_(u'Use Markdown'))
    status = models.CharField(max_length=1, null=False, blank=False, choices=ENTRY_STATUS_CHOICES, radio_admin=True, default=1)
    
    class Meta:
        db_table = 'encyclopedia_entries'
        verbose_name = _(u'Encyclopedia entry')
        verbose_name_plural = _(u'Encyclopedia entries')
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
            (_(u'Date'), {
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
    