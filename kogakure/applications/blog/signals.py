#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# (ɔ) Copyleft 2007-2008 Stefan Imhoff
# Licensed under the GNU General Public License, version 3.
# http://www.gnu.org/copyleft/gpl.txt

from django.core.cache import cache

def purge_cache(sender, instance, **kwargs):
    cache.delete(u'blog_entry:%s' % instance.pk)
    cache.delete(u'blog_entry_list')
    cache.delete(u'inhalt_stats')
