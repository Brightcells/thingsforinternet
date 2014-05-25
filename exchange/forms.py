# -*- coding: utf-8 -*-

from django import forms
from django.forms import Form, ModelForm, CharField, ModelChoiceField
from django.forms.widgets import TextInput, PasswordInput, EmailInput, URLInput, HiddenInput, Textarea
from django.utils.translation import ugettext_lazy as _

from exchange.models import Tips, UserTips

from utils.utils import *


class TipsModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(TipsModelForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Tips
        fields = ('tips', 'tag', 'url')
        widgets = {
            'tips': Textarea(
                attrs={'autocomplete': 'off', 'autofocus': 'autofocus', 'onscroll': 'this.rows++;', 'placeholder': _('Tips')}
            ),
            'tag': TextInput(
                attrs={'autocomplete': 'off', 'placeholder': _('Tags')}
            ),
            'url': URLInput(attrs={'autocomplete': 'off', 'placeholder': _('Url')}),
        }

    def clean_tips(self):
        """ Clean for tips """

        tips = self.cleaned_data['tips'].strip()
        if tips:
            t = Tips.objects.filter(tips=tips)
            if t.count() > 0:
                ut = UserTips.objects.filter(tips=t, user=getUI(getUsr(self.request)))
                if ut.count() > 0:
                    raise forms.ValidationError(_('This tip has already record by you'))
                else:
                    return tips
            else:
                return tips
        else:
            raise forms.ValidationError(_('Tips is needed'))

    def clean_tag(self):
        """ Clean for tag """

        tag = self.cleaned_data['tag'].strip()
        return ' '.join([t.strip() for t in tag.split(' ')])
