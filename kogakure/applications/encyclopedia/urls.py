#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# (ɔ) Copyleft 2007-2008 Stefan Imhoff
# Licensed under the GNU General Public License, version 3.
# http://www.gnu.org/copyleft/gpl.txt

import datetime
from django.conf.urls.defaults import *
from feeds import LatestEncyclopedia

encyclopedia_dict = {
    'template_object_name': 'entry',
    'template_name': 'encyclopedia/encyclopedia_list.html',
}

encyclopedia_detail_dict = {
    'template_object_name': 'entry',
    'template_name': 'encyclopedia/encyclopedia_detail.html',
    'slug_field': 'slug',
}

feeds = {
    'neuste': LatestEncyclopedia
}

urlpatterns = patterns('encyclopedia.views',
    
    # Encyclopedia List
    url(r'^$', 'generic_wrapper_list', dict(encyclopedia_dict), name='lexikon_liste'),
    # Encyclopedia Detail
    url(r'^(?P<slug>[-\w]+)/$', 'generic_wrapper_detail', dict(encyclopedia_detail_dict), name='lexikon'),
)

urlpatterns += patterns('django.contrib.syndication.views',
    url(r'^feeds/(?P<url>.*)/$', 'feed', {'feed_dict': feeds}, name='lexikon_feed'),
)