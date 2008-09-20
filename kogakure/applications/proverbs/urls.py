#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# (ɔ) Copyleft 2007-2008 Stefan Imhoff
# Licensed under the GNU General Public License, version 3.
# http://www.gnu.org/copyleft/gpl.txt

import datetime
from django.conf.urls.defaults import *
from feeds import LatestProverbs

proverb_dict = {
    'template_object_name': 'entry',
    'template_name': 'proverbs/proverb_list.html',
}

proverb_detail_dict = {
    'template_object_name': 'entry',
    'template_name': 'proverbs/proverb_detail.html',
}
feeds = {
    'neuste': LatestProverbs
}

urlpatterns = patterns('proverbs.views',
    # Proverbs List
    url(r'^$', 'generic_wrapper_list', dict(proverb_dict), name='sprueche_liste'),
    # Proverbs Detail
    url(r'^(?P<object_id>\d+)/$', 'generic_wrapper_detail', dict(proverb_detail_dict), name='sprueche'),
)

urlpatterns += patterns('django.contrib.syndication.views',
    url(r'^feeds/(?P<url>.*)/$', 'feed', {'feed_dict': feeds}, name='sprueche_feed'),
)