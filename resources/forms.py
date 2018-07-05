# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from django.forms.widgets import ClearableFileInput, HiddenInput, Textarea, TextInput, URLInput
from django.utils.translation import ugettext_lazy as _
from pysnippets.strsnippets import strip

from resources.models import ApiInfo, UserApiInfo, WebSiteInfo, WebSiteSubmit
from utils.tt4it_utils import *


class WebSiteDiyModelForm(ModelForm):
    class Meta:
        model = WebSiteInfo
        exclude = ('qiniu_logo', 'srcode', 'visit', 'evaluate', 'like', 'unlike', 'fav', 'display', 'create_time', 'modify_time')
        widgets = {
            'url': TextInput(
                attrs={'autocomplete': 'off', 'autofocus': 'autofocus', 'placeholder': _('Url')}
            ),
            'name': TextInput(
                attrs={'autocomplete': 'off', 'placeholder': _('Name')}
            ),
            'logo': ClearableFileInput(
                attrs={'autocomplete': 'off', 'placeholder': _('Logo')}
            ),
            'descr': Textarea(
                attrs={'autocomplete': 'off', 'placeholder': _('Description')}
            ),
            'tag': TextInput(
                attrs={'autocomplete': 'off', 'placeholder': _('Tag')}
            ),
        }

    def clean_url(self):
        url = self.cleaned_data['url']
        if not url:
            raise forms.ValidationError(_('The url is needed'))
        if 'http' not in url:
            raise forms.ValidationError(_('The url should starts with http(s)'))
        return url

    def clean_logo(self):
        logo = self.cleaned_data['logo']
        if not logo:
            raise forms.ValidationError(_('The logo is needed'))
        if logo.size > 50000:
            raise forms.ValidationError(_('The logo is too big'))
        return logo


class WebSiteSubmitModelForm(ModelForm):
    class Meta:
        model = WebSiteSubmit
        fields = '__all__'
        widgets = {
            'url': TextInput(
                attrs={'autocomplete': 'off', 'autofocus': 'autofocus', 'placeholder': _('Url')}
            ),
            'name': TextInput(
                attrs={'autocomplete': 'off', 'placeholder': _('Tag')}
            ),
            'deal': HiddenInput(),
        }


class ApiModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(ApiModelForm, self).__init__(*args, **kwargs)

    class Meta:
        model = ApiInfo
        fields = ('api', 'func', 'tag', 'url')
        widgets = {
            'api': TextInput(
                attrs={'autocomplete': 'off', 'autofocus': 'autofocus', 'placeholder': _('Api')}
            ),
            'func': Textarea(
                attrs={'autocomplete': 'off', 'onscroll': 'this.rows++;', 'placeholder': _('Func')}
            ),
            'tag': TextInput(
                attrs={'autocomplete': 'off', 'placeholder': _('Tags')}
            ),
            'url': URLInput(attrs={'autocomplete': 'off', 'placeholder': _('Url')}),
        }

    def clean_api(self):
        """ Clean for api """

        api = strip(self.cleaned_data['api'])
        if not api:
            raise forms.ValidationError(_('Api is needed'))
        a = ApiInfo.objects.filter(api=api)
        if a.exists():
            ua = UserApiInfo.objects.filter(api=a, user=getUI(getUsr(self.request)))
            if ua.exists():
                raise forms.ValidationError(_('This api has already record by you'))
            return api
        return api

    def clean_tag(self):
        """ Clean for tag """

        tag = strip(self.cleaned_data['tag'])
        return ' '.join([strip(t) for t in tag.split(' ')])
