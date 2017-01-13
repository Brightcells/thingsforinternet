# -*- coding: utf-8 -*-

from django.conf import settings
from django.shortcuts import redirect

from utils.tt4it_utils import *


def search(request):
    _query = request.GET.get('query', '')
    try:
        usr, ui = getUsrUI(request)
        search_engine = ui.search_engine
    except:
        search_engine = 'google'
    return redirect(settings.SEARCH_ENGINE.get(search_engine, 'google') % (_query))
