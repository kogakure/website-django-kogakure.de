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

class Category(models.Model):
    '''Category of a Product (Book, Movie, …)'''
    name = models.CharField(max_length=100, null=False, blank=False)
    slug = models.SlugField(u'URL', unique=True, prepopulate_from=('name',), null=False, blank=False)
    
    class Meta:
        db_table = 'product_categories'
        verbose_name = u'Kategorie'
        verbose_name_plural = u'Kategorien'
    
    class Admin:
        list_display = ('name',)
        search_fields = ('name',)
    
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
        ('D', u'Entwurf'),
        ('P', u'Veröffentlicht'),
        ('C', u'Geschlossen'),
    )
    title = models.CharField(u'Titel', max_length=200, null=False, blank=False)
    slug = models.SlugField(u'URL-Titel', unique=True, prepopulate_from=('title',), max_length='150', null=False, blank=False)
    pub_date = models.DateTimeField(u'Veröffentlicht', null=False, blank=False)
    cover = models.ImageField(u'Cover', upload_to='img/kaufempfehlungen', blank=False, null=False, help_text=u'60 Pixel Breite, Höhe automatisch')
    asin = models.CharField(u'ASIN', max_length='15', null=False, blank=False)
    category = models.ForeignKey(Category, verbose_name=u'Kategorie', null=False, blank=False)
    body = models.TextField(u'Informationen', null=True, blank=True, help_text=u'Markdown benutzen')
    status = models.CharField(max_length=1, null=False, blank=False, choices=ENTRY_STATUS_CHOICES, radio_admin=True, default=1)
    
    class Meta:
        db_table = 'product_entries'
        verbose_name = 'Kaufempfehlung'
        verbose_name_plural = 'Kaufempfehlungen'
        ordering = ('title',)
        get_latest_by = 'pub_date'
    
    class Admin:
        list_display = (
            'preview_image_url',
            'title',
            'category',
            'status',
            'pub_date'
        )
        list_filter = ('category',)
        search_fields = (
            'title',
            'asin',
            'body'
        )
        fields = (
            ('Datum', {
                'classes': 'collapse wide',
                'fields': ('pub_date',), 
            }),
            (None, {
                'classes': 'wide',
                'fields': (
                    'status',
                    'title',
                    'slug',
                    'cover',
                    'asin',
                    'category',
                    'body'
                )
            }),
        )

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