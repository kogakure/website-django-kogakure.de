#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# (ɔ) Copyleft 2007-2008 Stefan Imhoff
# Licensed under the GNU General Public License, version 3.
# http://www.gnu.org/copyleft/gpl.txt

import datetime
from django.contrib.syndication.feeds import Feed
from kogakure.apps.encyclopedia.models import Entry

class LatestEncyclopedia(Feed):
    title_template = 'feeds/title_encyclopedia.html'
    description_template = 'feeds/description_encyclopedia.html'
    
    title = 'kogakure.de – Lexikon'
    description = 'Neuste Lexikoneinträge'
    link = '/lexikon/'
    
    def items(self):
        return Entry.objects.filter(status='P', pub_date__lte=datetime.datetime.now()).order_by('-pub_date')[:5]