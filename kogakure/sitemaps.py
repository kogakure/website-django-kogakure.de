#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# (ɔ) Copyleft 2007-2008 Stefan Imhoff
# Licensed under the GNU General Public License, version 3.
# http://www.gnu.org/copyleft/gpl.txt

from django.contrib.sitemaps import Sitemap

class StaticFilePage:
    '''
    Custom Page class for use with static template in sitemaps
    '''
    def __init__(self, url):
        self.url = url
    def get_absolute_url(self):
        return self.url
    
class StaticFileSitemap(Sitemap):
    '''
    Custom Sitemap Class for use with static templates
    '''
    def __init__(self, urls, priority):
        self.priority = priority
        self.item_list = []
        if type(urls) not in (list, tuple):
            url = [urls]
        for url in urls:
            self.item_list.append(StaticFilePage(url))
        
    def items(self):
        return self.item_list
    