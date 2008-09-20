#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# (ɔ) Copyleft 2007-2008 Stefan Imhoff
# Licensed under the GNU General Public License, version 3.
# http://www.gnu.org/copyleft/gpl.txt

from django import forms
from django.utils.translation import ugettext_lazy as _

class ContactForm(forms.Form):
    name = forms.CharField(label=_(u'Name'),
                           max_length=100,
                           min_length=2, 
                           error_messages={
                               'required': _(u'Please type in your name.'),
                               'max_length': _(u'Your name is to long.'),
                               'min_length': _(u'Your name is to short.')
                           })
    email = forms.EmailField(label=_(u'Email'),
                             error_messages={
                                 'required': _(u'Please type in your Email address.'),
                                 'invalid': _(u'Please provide a correct Email address.')
                             })
    message = forms.CharField(widget=forms.Textarea(),
                              label=_(u'Message'),
                              error_messages={
                                  'required': _(u'Please type in your message.')
                              })
    
    def clean_message(self):
        message = self.cleaned_data.get('message', '')
        num_words = len(message.split())
        if num_words < 2:
            raise forms.ValidationError(u'Bitte gibt mehr Worte für deine Nachricht ein.')
        stop_words = ['http://','www.']
        used_stop_words = []
        for word in stop_words:
            if word in message:
                used_stop_words.append(word)
            forbidden_words = ', '.join(used_stop_words)
        if forbidden_words:
            raise forms.ValidationError(u'Unerlaubte Zeichen im Nachrichtentext: %s' % forbidden_words)
        return message
        