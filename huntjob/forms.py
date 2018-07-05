# -*- coding: utf-8 -*-

from django.forms import ModelForm
from django.forms.widgets import Textarea, TextInput
from django.utils.translation import ugettext_lazy as _
from pysnippets.strsnippets import strip

from huntjob.models import QuestionInfo


class QuestionInfoModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(QuestionInfoModelForm, self).__init__(*args, **kwargs)

    class Meta:
        model = QuestionInfo
        fields = ('question', 'answer', 'tag')
        widgets = {
            'question': Textarea(
                attrs={'autocomplete': 'off', 'autofocus': 'autofocus', 'onscroll': 'this.rows++;', 'placeholder': _('Question')}
            ),
            'answer': Textarea(
                attrs={'autocomplete': 'off', 'placeholder': _('Answer')}
            ),
            'tag': TextInput(
                attrs={'autocomplete': 'off', 'placeholder': _('Tags')}
            ),
        }

    def clean_tag(self):
        """ Clean for tag """

        tag = strip(self.cleaned_data['tag']) or ''
        return ' '.join([strip(t) for t in tag.split(' ')])
