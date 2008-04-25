#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# (ɔ) Copyleft 2007-2008 Stefan Imhoff
# Licensed under the GNU General Public License, version 3.
# http://www.gnu.org/copyleft/gpl.txt

import datetime
import urlparse
from django.conf import settings
from django.db import models
from django.db.models import permalink

class Author(models.Model):
    '''Author of the articles'''
    first_name = models.CharField(u'Vorname', max_length=100, null=False, blank=False)
    last_name = models.CharField(u'Nachname', max_length=100, null=False, blank=False)
    photo = models.ImageField(u'Foto', upload_to='img/autoren', blank=True, help_text=u'50 Pixel (quadratisch)')
    website = models.URLField(u'URL', null=True, blank=True, verify_exists=True)
    location = models.CharField(u'Ort', max_length=200, blank=True, null=True)
    bio = models.TextField(u'Biographie', null=True, blank=True, help_text=u'Markdown benutzen')
    
    class Meta:
        db_table = 'article_authors'
        verbose_name = u'Autor'
        verbose_name_plural = u'Autoren'
    
    class Admin:
        list_display = (
            'preview_image_url',
            'last_name',
            'first_name'
        )
    
    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)
    
    def preview_image_url(self):
            image_path = self.photo # URL of the image, e.g. /gallery/image.jpg
            image_path = image_path.replace('\\','/') # Windows-Fix
            image_path = urlparse.urljoin(settings.MEDIA_URL, image_path)
            return '<a href="' + str(self.id) + '/"><img src="' + str(image_path) + '" /></a>'

    preview_image_url.short_description = 'Foto'
    preview_image_url.allow_tags = True

class Category(models.Model):
    '''Categories for related Articles'''
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    slug = models.SlugField(u'URL', unique=True, prepopulate_from=('name',), null=False, blank=False)
    
    class Meta:
        db_table = 'article_categories'
        verbose_name = u'Thema'
        verbose_name_plural = u'Themen'
    
    class Admin:
        list_display = ('name',)
        search_fields = ('name',)
    
    def __unicode__(self):
        return self.name
    
    @permalink
    def get_absolute_url(self):
        return ('thema', (), { 'category_slug': self.slug })

class Entry(models.Model):
    '''An article entry'''
    ENTRY_STATUS_CHOICES = (
        ('D', u'Entwurf'),
        ('P', u'Veröffentlicht'),
        ('C', u'Geschlossen'),
    )
    author = models.ForeignKey(Author,  verbose_name=u'Autor', null=False, blank=False, related_name='entry_authors')
    title = models.CharField(u'Titel', max_length=200, null=False, blank=False)
    slug = models.SlugField(u'URL-Titel', unique=True, prepopulate_from=('title',), max_length='150', null=False, blank=False)
    pub_date = models.DateTimeField(u'Veröffentlicht', null=False, blank=False)
    summary = models.TextField(u'Auszug', null=False, blank=False, help_text=u'Markdown benutzen')
    body = models.TextField(u'Artikel', null=False, blank=False, help_text=u'Markdown benutzen')
    translators = models.ManyToManyField(Author, verbose_name=u'Übersetzer', null=True, blank=True)
    categories = models.ManyToManyField(Category, verbose_name=u'Kategorien', null=True, blank=True, related_name='entry_categories')
    status = models.CharField(max_length=1, null=False, blank=False, choices=ENTRY_STATUS_CHOICES, radio_admin=True, default=1)
    
    class Meta:
        db_table = 'article_entries'
        verbose_name = 'Artikel'
        verbose_name_plural = 'Artikel'
        ordering = ('-pub_date',)
        get_latest_by = 'pub_date'
    
    class Admin:
        list_display = (
            'title',
            'author',
            'status',
            'pub_date'
        )
        list_filter = (
            'categories',
            'pub_date',
            'author'
        )
        date_hierarchy = 'pub_date'
        search_fields = (
            'title',
            'summary',
            'body'
        )
        fields = (
            (u'Datum', {
                'classes': 'collapse wide',
                'fields': ('pub_date',), 
            }),
            (u'Autor', {
                'classes': 'collapse wide',
                'fields': (
                    ('author', 'translators'),
                ), 
            }),
            (None, {
                'classes': 'wide',
                'fields': (
                    'status',
                    'title',
                    'slug',
                    'summary',
                    'body',
                    'categories'
                )
            }),
        )
        
    def __unicode__(self):
        return self.title
    
    @permalink
    def get_absolute_url(self):
        return ('artikel', (), { 'slug': self.slug })
    
    def get_next_article(self):
        return self.get_next_by_pub_date(pub_date__lte=datetime.datetime.now(), status='P')

    def get_previous_article(self):
        return self.get_previous_by_pub_date(pub_date__lte=datetime.datetime.now(), status='P')
        