#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# (ɔ) Copyleft 2007-2008 Stefan Imhoff
# Licensed under the GNU General Public License, version 3.
# http://www.gnu.org/copyleft/gpl.txt

import datetime
from django.db.models import Q
from django.shortcuts import render_to_response
from kogakure.apps.articles.models import Entry as Article_Entries
from kogakure.apps.blog.models import Entry as Blog_Entries
from kogakure.apps.encyclopedia.models import Entry as Encyclopedia_Entries
from kogakure.apps.proverbs.models import Entry as Proverb_Entries

from django.template import RequestContext

def search(request):
    terms = request.GET.get('q', '')
    
    # Access to database only when terms were entered (and maxlenght is X)
    if terms: # and len(terms) >= 3 (Disabled to find Kanji)
        query = Q()
        query_encyclopedia = Q()
        query_proverbs = Q()

        # Article- & Blog-Entries (Queryset)
        for term in terms.split(' '):
            q = Q(title__icontains=term) | \
                Q(summary__icontains=term) | \
                Q(body__icontains=term)
            query = query & q
    
        article_results = Article_Entries.objects.filter(query, status='P', pub_date__lte=datetime.datetime.now()).distinct()
        blog_results = Blog_Entries.objects.filter(query, status='P', pub_date__lte=datetime.datetime.now()).distinct()
    
        # Encyclopedia (Queryset)
        for term in terms.split(' '):
            q = Q(title__icontains=term) | \
                Q(title_alt__icontains=term) | \
                Q(japanese__icontains=term) | \
                Q(explanation__icontains=term)
            query_encyclopedia = query_encyclopedia & q
    
        encyclopedia_results = Encyclopedia_Entries.objects.filter(query_encyclopedia, status='P', pub_date__lte=datetime.datetime.now()).distinct()
    
        # Proverbs (Queryset)
        for term in terms.split(' '):
            q = Q(body__icontains=term) | \
                Q(author__icontains=term)
            query_proverbs = query_proverbs & q
    
        proverbs_results = Proverb_Entries.objects.filter(query_proverbs, status='P', pub_date__lte=datetime.datetime.now()).distinct()

        return render_to_response('search.html', {
            'article_list': article_results,
            'blog_list': blog_results,
            'encyclopedia_list': encyclopedia_results,
            'proverbs_list': proverbs_results,
            'q': terms,
        }, context_instance=RequestContext(request))
    else:
        return render_to_response('search.html', {
            'q': terms,
        }, context_instance=RequestContext(request))
