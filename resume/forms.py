# -*- coding: utf-8 -*-

from django import forms
from django.forms import Form, ModelForm, CharField, ModelChoiceField
from django.forms.widgets import TextInput, PasswordInput, EmailInput, URLInput, HiddenInput, Textarea, FileInput
from django.utils.translation import ugettext_lazy as _

from resume.models import ResumeInfo

from utils.utils import *


class ResumeInfoModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(ResumeInfoModelForm, self).__init__(*args, **kwargs)

    class Meta:
        model = ResumeInfo
        fields = ('resume', 'resume_html', 'pdf', 'tag')
        widgets = {
            'resume': Textarea(
                attrs={'autocomplete': 'off', 'autofocus': 'autofocus', 'onscroll': 'this.rows++;', 'placeholder': _('Resume Markdown Content')}
            ),
            'resume_html': Textarea(
                attrs={'autocomplete': 'off', 'autofocus': 'autofocus', 'onscroll': 'this.rows++;', 'placeholder': _('Resume Html Content')}
            ),
            'pdf': FileInput(
                attrs={'autocomplete': 'off', 'placeholder': _('pdf or docx')}
            ),
            'tag': TextInput(
                attrs={'autocomplete': 'off', 'placeholder': _('Tags')}
            ),
        }

    def clean_tag(self):
        """ Clean for tag """

        tag = self.cleaned_data['tag'].strip()
        return ' '.join([t.strip() for t in tag.split(' ')])
