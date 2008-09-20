#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# (ɔ) Copyleft 2007-2008 Stefan Imhoff
# Licensed under the GNU General Public License, version 3.
# http://www.gnu.org/copyleft/gpl.txt

import datetime
import urlparse
from django.conf import settings
from kogakure.lib.templatetags.thumbnail import thumbnail
from django.db import models
from django.db.models import permalink
from django.utils.translation import ugettext_lazy as _

class Category(models.Model):
    '''Category of a Product (Book, Movie, &hellip;)'''
    name = models.CharField(max_length=100, null=False, blank=False)
    slug = models.SlugField(_(u'URL'), unique=True, null=False, blank=False)
    
    class Meta:
        db_table = 'product_categories'
        verbose_name = _(u'Category')
        verbose_name_plural = _(u'Categories')
    
    def __unicode__(self):
        return self.name
    
    @permalink
    def get_absolute_url(self):
        return ('kaufempfehlungen', (), { 'slug': self.slug })
    
    @permalink
    def get_feed_url(self):
        return ('kaufempfehlungen_feed_produkt', (), { 'produkt': 'produkt', 'url': self.slug })
    
class Entry(models.Model):
    '''A product'''
    ENTRY_STATUS_CHOICES = (
        ('D', _(u'Draft')),
        ('P', _(u'Published')),
        ('C', _(u'Closed')),
    )
    title = models.CharField(_(u'Title'), max_length=200, null=False, blank=False)
    slug = models.SlugField(_(u'Slug'), unique=True, max_length='150', null=False, blank=False)
    pub_date = models.DateTimeField(_(u'Published'), default=datetime.datetime.now, null=False, blank=False)
    cover = models.ImageField(_(u'Cover'), upload_to='img/kaufempfehlungen', blank=False, null=False, help_text=_(u'60 pixel width, auto height'))
    asin = models.CharField(_(u'ASIN'), max_length='15', null=False, blank=False)
    category = models.ForeignKey(Category, verbose_name=_(u'Category'), null=False, blank=False)
    body = models.TextField(_(u'Information'), null=True, blank=True, help_text=_(u'Use Markdown'))
    status = models.CharField(max_length=1, null=False, blank=False, choices=ENTRY_STATUS_CHOICES, default='P')
    
    class Meta:
        db_table = 'product_entries'
        verbose_name = _(u'Recommendations')
        verbose_name_plural = _(u'Recommendations')
        ordering = ('title',)
        get_latest_by = 'pub_date'
    
    def __unicode__(self):
        return self.title
    
    @permalink
    def get_absolute_url(self):
        return ('kaufempfehlungen', (), { 'slug': self.slug })
    
    def preview_image_url(self):
        image_path = thumbnail(self.cover, '60x60')
        image_path = image_path.replace('\\','/') # Windows-Fix
        image_path = urlparse.urljoin(settings.MEDIA_URL, image_path)
        return '<a href="' + str(self.id) + '/"><img src="' + str(image_path) + '" /></a>'
    
    preview_image_url.short_description = 'Cover'
    preview_image_url.allow_tags = True