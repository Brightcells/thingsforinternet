# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from django.forms.widgets import TextInput, URLInput, Textarea
from django.utils.translation import ugettext_lazy as _

from exchange.models import Tips, UserTips, BlogInfo

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

        tag = self.cleaned_data['tag'].strip()
        return ' '.join([t.strip() for t in tag.split(' ')])
