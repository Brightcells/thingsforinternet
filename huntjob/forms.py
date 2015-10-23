# -*- coding: utf-8 -*-

from django.forms import ModelForm
from django.forms.widgets import TextInput, Textarea
from django.utils.translation import ugettext_lazy as _

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

        tag = self.cleaned_data['tag'].strip()
        return ' '.join([t.strip() for t in tag.split(' ')])
