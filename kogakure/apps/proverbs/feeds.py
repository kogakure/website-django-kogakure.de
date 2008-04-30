#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# (ɔ) Copyleft 2007-2008 Stefan Imhoff
# Licensed under the GNU General Public License, version 3.
# http://www.gnu.org/copyleft/gpl.txt

import datetime
from django.contrib.syndication.feeds import Feed
from kogakure.apps.proverbs.models import Entry
from django.utils.translation import ugettext_lazy as _

class LatestProverbs(Feed):
    title_template = 'feeds/title_proverbs.html'
    description_template = 'feeds/description.html'
    
    title = _(u'kogakure.de &ndash; Proverbs')
    description = _('Newest Proverbs')
    link = '/sprueche/'
    
    def items(self):
        return Entry.objects.filter(status='P', pub_date__lte=datetime.datetime.now()).order_by('-pub_date')[:5]