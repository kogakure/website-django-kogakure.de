#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# (ɔ) Copyleft 2007-2008 Stefan Imhoff
# Licensed under the GNU General Public License, version 3.
# http://www.gnu.org/copyleft/gpl.txt

import datetime
from django.views.decorators.cache import cache_page
from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.simple import direct_to_template, redirect_to
from django.views.generic.list_detail import object_detail, object_list
from articles.models import *
from lib.utils import cache_status

from sitemaps import StaticFileSitemap
from articles.sitemaps import ArticlesMap
from blog.sitemaps import BlogMap
from encyclopedia.sitemaps import EncylopediaMap

admin.autodiscover()

import os
DIRNAME = os.path.dirname(__file__)

inhalt_dict = {
    'queryset': Entry.objects.filter(status='P', pub_date__lte=datetime.datetime.now()),
    'template_object_name': 'entry',
    'template_name': 'inhalt.html',
    'extra_context': {
        'category_list': Category.objects.all(),
    }
}

category_detail_dict = {
    'template_object_name': 'category',
    'template_name': 'categories.html',
    'slug_field': 'slug'
}

static_urls = (
    '/',
    '/inhalt/',
    '/kaufempfehlungen',
    '/lexikon/',
    '/sprueche/',
    '/info/',
    '/faq/'
)

sitemaps = {
    'statisch': StaticFileSitemap(static_urls, priority=0.5),
    'artikel': ArticlesMap,
    'kurzmeldungen': BlogMap,
    'lexikon': EncylopediaMap
}

urlpatterns = patterns('',
    (r'^artikel/', include('articles.urls')),
    (r'^kurzmeldungen/', include('blog.urls')),
    (r'^sprueche/', include('proverbs.urls')),
    (r'^kaufempfehlungen/', include('products.urls')),
    (r'^lexikon/', include('encyclopedia.urls')),
    (r'^suche/$', 'search.views.search'),
    url(r'^inhalt/', object_list, dict(inhalt_dict), name='inhaltsverzeichnis'),
    url(r'^themen/(?P<category_slug>[-\w]+)/$', 'articles.views.category', name='thema'),
    url(r'^kontakt/', 'contact.views.contact', name='kontakt'),
    # Admin
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/(.*)', admin.site.root),
    # Homepage
    (r'^$', direct_to_template, {'template': 'homepage.html'}),
    # Cache Status
    (r'^cache-status/$', cache_status),
    # robots.txt
    (r'robots\.txt', direct_to_template, { 'template': 'seo/robots.txt' }),
    # Google Webmaster Tools (https://www.google.com/webmasters/tools/siteoverview)
    (r'googleeac4fc886a6f9f8d\.html', direct_to_template, { 'template': 'seo/googleeac4fc886a6f9f8d.html' }),
    # Yahoo Site Explorer (https://siteexplorer.search.yahoo.com/mysites)
    (r'y_key_dc6ca9ea04c4d2d2\.html', direct_to_template, { 'template': 'seo/y_key_dc6ca9ea04c4d2d2.html' }),
    # Microsoft Webmaster Tools (http://webmaster.live.com/webmaster/WebmasterManageSitesPage.aspx)
    (r'LiveSearchSiteAuth\.xml', direct_to_template, { 'template': 'seo/LiveSearchSiteAuth.xml' }),
)

urlpatterns += patterns('django.contrib.sitemaps.views',
    (r'^sitemap.xml$', 'index', {'sitemaps': sitemaps}),
    (r'^sitemap-(?P<section>.+).xml$', 'sitemap', {'sitemaps': sitemaps}),
)

if settings.LOCAL_DEVELOPMENT:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(DIRNAME, 'media'), 'show_indexes': True}),
    )

urlpatterns += patterns('',
    (r'', include('django.contrib.flatpages.urls')),
)