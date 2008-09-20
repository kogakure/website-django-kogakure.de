#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# (ɔ) Copyleft 2007-2008 Stefan Imhoff
# Licensed under the GNU General Public License, version 3.
# http://www.gnu.org/copyleft/gpl.txt

# Make Templatetags and Filters available to all templates
from django.template import add_to_builtins

add_to_builtins('kogakure.lib.templatetags.get_all_tag')
add_to_builtins('kogakure.lib.templatetags.get_stat_tag')
add_to_builtins('kogakure.lib.templatetags.smarttext_filter')