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
    '''An blog entry'''
    ENTRY_STATUS_CHOICES = (
        ('D', _(u'Draft')),
        ('P', _(u'Published')),
        ('C', _(u'Closed')),
    )
    title = models.CharField(_(u'Title'), max_length=200, null=False, blank=False)
    slug = models.SlugField(_(u'Slug'), unique=True, max_length='150', null=False, blank=False)
    pub_date = models.DateTimeField(_(u'Published'), default=datetime.datetime.now, null=False, blank=False)
    summary = models.TextField(_(u'Excerpt'), null=False, blank=False, help_text=_(u'Use Markdown'))
    body = models.TextField(_(u'Blog'), null=False, blank=False, help_text=_(u'Use Markdown'))
    status = models.CharField(max_length=1, null=False, blank=False, choices=ENTRY_STATUS_CHOICES, default='P')
    
    class Meta:
        db_table = 'blog_entries'
        verbose_name = _(u'Blog Entry')
        verbose_name_plural = _(u'Blog Entries')
        ordering = ('-pub_date',)
        get_latest_by = 'pub_date'
    
    def __unicode__(self):
        return self.title
    
    @permalink
    def get_absolute_url(self):
        return ('kurzmeldungen', (), { 'slug': self.slug })
    