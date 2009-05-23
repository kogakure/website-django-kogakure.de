#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# (ɔ) Copyleft 2007-2008 Stefan Imhoff
# Licensed under the GNU General Public License, version 3.
# http://www.gnu.org/copyleft/gpl.txt

from django.db.models.signals import post_save, post_delete
from blog.models import Entry
from blog.signals import purge_cache

post_save.connect(purge_cache, sender=Entry)
post_delete.connect(purge_cache, sender=Entry)