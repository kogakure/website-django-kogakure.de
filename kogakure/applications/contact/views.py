#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# (ɔ) Copyleft 2007-2008 Stefan Imhoff
# Licensed under the GNU General Public License, version 3.
# http://www.gnu.org/copyleft/gpl.txt

from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _
from forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data.get('email', 'noreply@domain.com')
            message = form.cleaned_data['message']
            meta = request.META['HTTP_USER_AGENT']
            message += '\n\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n\n' + meta
            send_mail(
                _(u'Contact form: domain.com'),
                message, email,
                ['email@domain.com']
            )
            return HttpResponseRedirect('/email/verschickt/')
    else:
        form = ContactForm()
    return render_to_response('contact.html', {'form': form}, context_instance=RequestContext(request))
