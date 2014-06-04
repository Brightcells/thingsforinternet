# -*- coding: utf-8 -*-

from django import forms
from django.forms import Form, ModelForm, CharField, ModelChoiceField
from django.forms.widgets import TextInput, PasswordInput, EmailInput, HiddenInput, URLInput, Textarea, ClearableFileInput
from django.utils.translation import ugettext_lazy as _

from resources.models import WebSiteSubmit, ApiInfo, UserApiInfo

from utils.utils import *


class WebSiteDiyModelForm(ModelForm):
    class Meta:
        model = WebSiteInfo
        exclude = ('srcode', 'visit', 'evaluate', 'like', 'unlike', 'fav', 'display', 'create_time', 'modify_time')
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


class WebSiteSubmitModelForm(ModelForm):
    class Meta:
        model = WebSiteSubmit
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

        api = self.cleaned_data['api'].strip()
        if api:
            a = ApiInfo.objects.filter(api=api)
            if a.count() > 0:
                ua = UserApiInfo.objects.filter(api=a, user=getUI(getUsr(self.request)))
                if ua.count() > 0:
                    raise forms.ValidationError(_('This api has already record by you'))
                else:
                    return api
            else:
                return api
        else:
            raise forms.ValidationError(_('Api is needed'))

    def clean_tag(self):
        """ Clean for tag """

        tag = self.cleaned_data['tag'].strip()
        return ' '.join([t.strip() for t in tag.split(' ')])