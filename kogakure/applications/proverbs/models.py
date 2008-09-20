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
    '''An proverb entry'''
    ENTRY_STATUS_CHOICES = (
        ('D', _(u'Draft')),
        ('P', _(u'Published')),
        ('C', _(u'Closed')),
    )
    pub_date = models.DateTimeField(_(u'Published'), default=datetime.datetime.now, null=False, blank=False)
    body = models.TextField(_(u'Proverb'), null=False, blank=False, help_text=_(u'Use Markdown, with quotes'))
    author = models.CharField(_(u'Author'), null=False, blank=False, max_length=150)
    status = models.CharField(max_length=1, null=False, blank=False, choices=ENTRY_STATUS_CHOICES, default='P')
    
    class Meta:
        db_table = 'proverb_entries'
        verbose_name = _(u'Proverb')
        verbose_name_plural = _(u'Proverbs')
        ordering = ('-pub_date',)
        get_latest_by = 'pub_date'
    
    def __unicode__(self):
        return self.body
    
    @permalink
    def get_absolute_url(self):
        return ('sprueche', (), { 'object_id': self.id })
    