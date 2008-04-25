#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# (ɔ) Copyleft 2007-2008 Stefan Imhoff
# Licensed under the GNU General Public License, version 3.
# http://www.gnu.org/copyleft/gpl.txt

import datetime
from django.conf.urls.defaults import *
from kogakure.apps.products.feeds import LatestProducts, LatestProductsByProduct

products_dict = {
    'template_object_name': 'product',
    'template_name': 'products/products_list.html',
}

products_detail_dict = {
    'template_object_name': 'entry',
    'template_name': 'products/products_detail.html',
    'slug_field': 'slug',
}

feeds = {
    'neuste': LatestProducts,
    'produkt': LatestProductsByProduct
}

urlpatterns = patterns('kogakure.apps.products.views',
    # Product Recommendations List
    url(r'^$', 'generic_wrapper_list', dict(products_dict), name='kaufempfehlungen_liste'),
    # Product Recommendations Detail
    url(r'^(?P<slug>[-\w]+)/$', 'generic_wrapper_detail', dict(products_detail_dict), name='kaufempfehlungen'),
)

urlpatterns += patterns('django.contrib.syndication.views',
    url(r'^feeds/(?P<url>.*)/$', 'feed', {'feed_dict': feeds}, name='kaufempfehlungen_feed'),
    url(r'^feeds/(?P<produkt>.*)/(?P<url>.*)/$', 'feed', {'feed_dict': feeds}, name='kaufempfehlungen_feed_produkt'),
)