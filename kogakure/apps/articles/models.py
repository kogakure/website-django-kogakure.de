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
from django.utils.translation import ugettext_lazy as _

class Author(models.Model):
    '''Author of the articles'''
    first_name = models.CharField(_(u'First Name'), max_length=100, null=False, blank=False)
    last_name = models.CharField(_(u'Last Name'), max_length=100, null=False, blank=False)
    photo = models.ImageField(_(u'Photo'), upload_to='img/autoren', blank=True, help_text=_(u'50 Pixel (square)'))
    website = models.URLField(_(u'URL'), null=True, blank=True, verify_exists=True)
    location = models.CharField(_(u'City'), max_length=200, blank=True, null=True)
    bio = models.TextField(_(u'Biography'), null=True, blank=True, help_text=_(u'Use Markdown'))
    
    class Meta:
        db_table = 'article_authors'
        verbose_name = _(u'Author')
        verbose_name_plural = _(u'Authors')
    
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
    slug = models.SlugField(_(u'URL'), unique=True, prepopulate_from=('name',), null=False, blank=False)
    
    class Meta:
        db_table = 'article_categories'
        verbose_name = _(u'Topic')
        verbose_name_plural = _(u'Topics')
    
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
        ('D', _(u'Draft')),
        ('P', _(u'Published')),
        ('C', _(u'Closed')),
    )
    author = models.ForeignKey(Author,  verbose_name=_(u'Author'), null=False, blank=False, related_name='entry_authors')
    title = models.CharField(_(u'Title'), max_length=200, null=False, blank=False)
    slug = models.SlugField(_(u'Slug'), unique=True, prepopulate_from=('title',), max_length='150', null=False, blank=False)
    pub_date = models.DateTimeField(_(u'Published'), default=datetime.datetime.now, null=False, blank=False)
    summary = models.TextField(_(u'Excerpt'), null=False, blank=False, help_text=_(u'Use Markdown'))
    body = models.TextField(_(u'Article'), null=False, blank=False, help_text=_(u'Use Markdown'))
    translators = models.ManyToManyField(Author, verbose_name=_(u'Translator'), null=True, blank=True)
    categories = models.ManyToManyField(Category, verbose_name=_(u'Categories'), null=True, blank=True, related_name='entry_categories')
    status = models.CharField(max_length=1, null=False, blank=False, choices=ENTRY_STATUS_CHOICES, radio_admin=True, default=1)
    
    class Meta:
        db_table = 'article_entries'
        verbose_name = _(u'Article')
        verbose_name_plural = _(u'Articles')
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
            (_(u'Date'), {
                'classes': 'collapse wide',
                'fields': ('pub_date',), 
            }),
            (_(u'Author'), {
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
        