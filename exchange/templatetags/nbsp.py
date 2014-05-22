from django import template
from django.utils.safestring import mark_safe


register = template.Library()


@register.filter()
def nbsp(value):
    # this method isn't work when the value has html tag
    # which will cause html display error
    return mark_safe("&nbsp;".join(value.split(' ')))
