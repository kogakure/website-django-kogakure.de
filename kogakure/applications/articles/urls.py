#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# (ɔ) Copyleft 2007-2008 Stefan Imhoff
# Licensed under the GNU General Public License, version 3.
# http://www.gnu.org/copyleft/gpl.txt

import datetime
from django.conf.urls.defaults import *
from feeds import LatestArticles

article_dict = {
    'template_object_name': 'entry',
    'template_name': 'articles/article_list.html',
    'paginate_by': 100,
}

article_detail_dict = {
    'template_object_name': 'entry',
    'template_name': 'articles/article_detail.html',
    'slug_field': 'slug',
}

feeds = {
    'neuste': LatestArticles,
}

urlpatterns = patterns('articles.views',
    # Article Pagination
    (r'^seite-(?P<page>[0-9]+)/$', 'generic_wrapper_list', dict(article_dict)),
    # Article List
    url(r'^$', 'generic_wrapper_list', dict(article_dict), name='artikel_liste'),
    # Article Detail
    url(r'^(?P<slug>[-\w]+)/$', 'generic_wrapper_detail', dict(article_detail_dict), name='artikel'),
)

urlpatterns += patterns('django.contrib.syndication.views',
    url(r'^feeds/(?P<url>.*)/$', 'feed', {'feed_dict': feeds}, name='artikel_feed'),
)