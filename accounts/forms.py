# -*- coding: utf-8 -*-

import hashlib

from django import forms
from django.forms import CharField, EmailField, Form, ModelForm
from django.forms.widgets import CheckboxInput, EmailInput, HiddenInput, PasswordInput, Select, TextInput, URLInput
from django.utils.translation import ugettext_lazy as _

from accounts.models import UserInfo


class SignupUserInfoModelForm(ModelForm):
    class Meta:
        model = UserInfo
        exclude = ('company', 'github', 'sof', 'weibo', 'rren', 'v2ex', 'blog', 'btc')
        widgets = {
            'username': TextInput(
                attrs={'autocomplete': 'off', 'autofocus': 'autofocus', 'placeholder': _('Username')}
            ),
            'password': PasswordInput(
                attrs={'autocomplete': 'off', 'placeholder': _('Password')}
            ),
            'email': EmailInput(attrs={'placeholder': _('Email')}),
            'status': HiddenInput(),
        }

    def clean_username(self):
        username = self.cleaned_data['username'].strip()
        if username:
            ui = UserInfo.objects.filter(username=username)
            if ui.count() > 0:
                raise forms.ValidationError(_('This user has already exists'))
            else:
                return username
        else:
            raise forms.ValidationError(_('User name is needed'))

    def clean_password(self):
        password = self.cleaned_data['password'].strip()
        if password:
            return hashlib.md5(password).hexdigest()
        else:
            raise forms.ValidationError(_('Password is needed'))


class LoginUserInfoModelForm(Form):
    username = CharField(
        max_length=255,
        widget=TextInput(attrs={'autofocus': 'autofocus', 'placeholder': _('Username')}),
        error_messages={'required': _('User name is needed')}
    )
    password = CharField(
        max_length=255,
        widget=PasswordInput(attrs={'placeholder': _('Password')}),
        error_messages={'required': _('Password is needed')}
    )

    def clean_username(self):
        username = self.cleaned_data['username'].strip()
        if username:
            ui = UserInfo.objects.filter(username=username)
            if ui.count() == 0:
                raise forms.ValidationError(_('This user doesn\'t exists'))
            else:
                return username
        else:
            raise forms.ValidationError(_('User name is needed'))

    def clean_password(self):
        password = self.cleaned_data['password'].strip()
        if password:
            return hashlib.md5(password).hexdigest()
        else:
            raise forms.ValidationError(_('Password is needed'))

    def clean(self):
        cleaned_data = self.cleaned_data
        username = cleaned_data.get('username', '')
        password = cleaned_data.get('password', '')
        if username and password:
            ui = UserInfo.objects.filter(username=username, password=password)
            if ui.count() == 0:
                raise forms.ValidationError(_('Username and Password does\'t match'))
            else:
                return cleaned_data
        else:
            return cleaned_data


class ForgotUserInfoModelForm(Form):
    email = EmailField(
        widget=EmailInput(attrs={'placeholder': _('Email')}),
        error_messages={'required': _('Email is needed')}
    )


class SettingsUserInfoModelForm(ModelForm):
    class Meta:
        model = UserInfo
        exclude = ('password', 'status')
        widgets = {
            'username': TextInput(
                attrs={'autocomplete': 'off', 'autofocus': 'autofocus', 'readonly': 'true', 'placeholder': _('Username')}
            ),
            'login_page': URLInput(
                attrs={'autocomplete': 'off', 'placeholder': _('Login Page')}
            ),
            'display_bg': CheckboxInput(
                attrs={'autocomplete': 'off', 'placeholder': _('Display Background')}
            ),
            'classify': Select(
                attrs={'autocomplete': 'off', 'placeholder': _('Background Classify')}
            ),
            'search_engine': Select(
                attrs={'autocomplete': 'off', 'placeholder': _('Search Engine')}
            ),
            'email': TextInput(
                attrs={'autocomplete': 'off', 'placeholder': _('Email')}
            ),
            'company': TextInput(
                attrs={'autocomplete': 'off', 'placeholder': _('Company')}
            ),
            'github': TextInput(
                attrs={'autocomplete': 'off', 'placeholder': _('Github')}
            ),
            'sof': TextInput(
                attrs={'autocomplete': 'off', 'placeholder': _('Stackoverflow')}
            ),
            'weibo': TextInput(
                attrs={'autocomplete': 'off', 'placeholder': _('Weibo')}
            ),
            'rren': TextInput(
                attrs={'autocomplete': 'off', 'placeholder': _('RRen')}
            ),
            'v2ex': TextInput(
                attrs={'autocomplete': 'off', 'placeholder': _('V2EX')}
            ),
            'blog': TextInput(
                attrs={'autocomplete': 'off', 'placeholder': _('Blog')}
            ),
            'btc': TextInput(
                attrs={'autocomplete': 'off', 'placeholder': _('BTC')}
            ),
        }
