# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.shortcuts import redirect


def tt_login_required(func):
    def wrap(request, *args, **kwargs):
            if 'usr' not in request.COOKIES:
                return redirect('%s?next=%s' % (reverse('accounts:login'), request.path))
            return func(request, *args, **kwargs)
    return wrap
