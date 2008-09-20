#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# (ɔ) Copyleft 2007-2008 Stefan Imhoff
# Licensed under the GNU General Public License, version 3.
# http://www.gnu.org/copyleft/gpl.txt

import datetime
from django.conf.urls.defaults import *
from feeds import LatestBlog

blog_dict = {
    'template_object_name': 'entry',
    'template_name': 'blog/blog_list.html',
    'paginate_by': 100,
}

blog_detail_dict = {
    'template_object_name': 'entry',
    'template_name': 'blog/blog_detail.html',
    'slug_field': 'slug',
}

feeds = {
    'neuste': LatestBlog,
}

urlpatterns = patterns('blog.views',
    # Blog Pagination
    (r'^seite-(?P<page>[0-9]+)/$', 'generic_wrapper_list', dict(blog_dict)),
    # Blog List
    url(r'^$', 'generic_wrapper_list', dict(blog_dict), name='kurzmeldungen_liste'),
    # Blog Detail
    url(r'^(?P<slug>[-\w]+)/$', 'generic_wrapper_detail', dict(blog_detail_dict), name='kurzmeldungen'),
)

urlpatterns += patterns('django.contrib.syndication.views',
    url(r'^feeds/(?P<url>.*)/$', 'feed', {'feed_dict': feeds}, name='kurzmeldungen_feed'),
)