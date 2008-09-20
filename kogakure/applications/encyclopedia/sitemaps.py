#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# (ɔ) Copyleft 2007-2008 Stefan Imhoff
# Licensed under the GNU General Public License, version 3.
# http://www.gnu.org/copyleft/gpl.txt

import datetime
from django.contrib.sitemaps import Sitemap
from kogakure.apps.encyclopedia.models import Entry

class EncylopediaMap(Sitemap):
    priority = '0.7'
    def items(self):
        return Entry.objects.filter(status='P', pub_date__lte=datetime.datetime.now())
