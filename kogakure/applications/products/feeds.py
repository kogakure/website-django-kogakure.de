#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# (ɔ) Copyleft 2007-2008 Stefan Imhoff
# Licensed under the GNU General Public License, version 3.
# http://www.gnu.org/copyleft/gpl.txt

import datetime
from django.contrib.syndication.feeds import Feed
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ugettext_lazy as _
from models import Entry, Category

class LatestProducts(Feed):
    title_template = 'feeds/title.html'
    description_template = 'feeds/description.html'
    
    title = _(u'kogakure.de &ndash; Recommendations')
    description = _(u'Newest Recommendations')
    link = '/kaufempfehlungen/'
    
    def items(self):
        return Entry.objects.filter(status='P', pub_date__lte=datetime.datetime.now()).order_by('-pub_date')[:5]
    
class LatestProductsByProduct(Feed):
    title_template = 'feeds/title.html'
    description_template = 'feeds/description.html'
    
    def get_object(self, bits):
        if len(bits) < 1:
            raise ObjectDoesNotExist
        return Category.objects.get(slug=bits[-1])
    
    def title(self, obj):
        return _(u'Recommendations: %s') % obj.name
    
    def description(self, obj):
        return _(u'Newest recommendations from "%s"') % obj.name
    
    def link(self, obj):
        return obj.get_absolute_url()
    
    def items(self, obj):
        return Entry.objects.filter(category__slug=obj.slug, status='P', pub_date__lte=datetime.datetime.now())[:5]