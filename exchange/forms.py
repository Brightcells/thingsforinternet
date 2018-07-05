# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from django.forms.widgets import Textarea, TextInput, URLInput
from django.utils.translation import ugettext_lazy as _
from pysnippets.strsnippets import strip

from exchange.models import BlogInfo, Tips, UserTips
from utils.tt4it_utils import *


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

        tips = strip(self.cleaned_data['tips'])
        if not tips:
            raise forms.ValidationError(_('Tips is needed'))
        t = Tips.objects.filter(tips=tips)
        if t.exists():
            ut = UserTips.objects.filter(tips=t, user=getUI(getUsr(self.request)))
            if ut.exists():
                raise forms.ValidationError(_('This tip has already record by you'))
            return tips
        return tips

    def clean_tag(self):
        """ Clean for tag """

        tag = strip(self.cleaned_data['tag'])
        return ' '.join([strip(t) for t in tag.split(' ')])


class BlogInfoModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(BlogInfoModelForm, self).__init__(*args, **kwargs)

    class Meta:
        model = BlogInfo
        fields = ('title', 'blog', 'tag')
        widgets = {
            'title': TextInput(
                attrs={'autocomplete': 'off', 'autofocus': 'autofocus', 'onscroll': 'this.rows++;', 'placeholder': _('Blog Title')}
            ),
            'blog': Textarea(
                attrs={'autocomplete': 'off', 'placeholder': _('Blog Content')}
            ),
            'tag': TextInput(
                attrs={'autocomplete': 'off', 'placeholder': _('Tags')}
            ),
        }

    def clean_tag(self):
        """ Clean for tag """

        tag = strip(self.cleaned_data['tag'])
        return ' '.join([strip(t) for t in tag.split(' ')])
