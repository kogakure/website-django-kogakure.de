#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# (ɔ) Copyleft 2007-2008 Stefan Imhoff
# Licensed under the GNU General Public License, version 3.
# http://www.gnu.org/copyleft/gpl.txt

import datetime
from django.contrib.syndication.feeds import Feed
from kogakure.apps.articles.models import Entry

class LatestArticles(Feed):
    title_template = 'feeds/title.html'
    description_template = 'feeds/description.html'
    
    title = 'kogakure.de – Artikel'
    description = 'Neuste Artikel'
    link = '/artikel/'
    
    def items(self):
        return Entry.objects.filter(status='P', pub_date__lte=datetime.datetime.now()).order_by('-pub_date')[:5]