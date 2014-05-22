# -*- coding: utf-8 -*-

from django import forms
from django.forms import Form, ModelForm, CharField, ModelChoiceField
from django.forms.widgets import TextInput, PasswordInput, EmailInput, HiddenInput
from django.utils.translation import ugettext_lazy as _

from resources.models import WebSiteSubmit


class WebSiteSubmitModelForm(ModelForm):
    class Meta:
        model = WebSiteSubmit
        widgets = {
            'url': TextInput(
                attrs={'autocomplete': 'off', 'autofocus': 'autofocus', 'placeholder': _('Url')}
            ),
            'tag': TextInput(
                attrs={'autocomplete': 'off', 'placeholder': _('Tag')}
            ),
            'deal': HiddenInput(),
        }