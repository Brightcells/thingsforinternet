# -*- coding: utf-8 -*-

from django.forms import ModelForm
from django.forms.widgets import FileInput, Textarea, TextInput
from django.utils.translation import ugettext_lazy as _
from pysnippets.strsnippets import strip

from resume.models import ResumeInfo


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

        tag = strip(self.cleaned_data['tag']) or ''
        return ' '.join([strip(t) for t in tag.split(' ')])
