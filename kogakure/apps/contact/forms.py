#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# (ɔ) Copyleft 2007-2008 Stefan Imhoff
# Licensed under the GNU General Public License, version 3.
# http://www.gnu.org/copyleft/gpl.txt

from django import newforms as forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Name',
                           max_length=100,
                           min_length=2, 
                           error_messages={
                               'required': 'Bitte gib deinen Namen ein.',
                               'max_length': 'Dein Name ist zu lang.',
                               'min_length': 'Dein Name ist zu kurz.'
                           })
    email = forms.EmailField(label='E-Mail',
                             error_messages={
                                 'required': 'Bitte gib deine E-Mail-Adresse ein.',
                                 'invalid': 'Bitte gib deine korrekte E-Mail-Adresse ein.'
                             })
    message = forms.CharField(widget=forms.Textarea(),
                              label='Nachricht',
                              error_messages={
                                  'required': 'Bitte gib deinen Nachrichtentext ein.'
                              })
    
    def clean_message(self):
        message = self.cleaned_data.get('message', '')
        num_words = len(message.split())
        if num_words < 2:
            raise forms.ValidationError(u'Bitte gibt mehr Worte für deine Nachricht ein.')
        return message
    
    