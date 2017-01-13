# -*- coding: utf-8 -*-

from django.shortcuts import redirect, render

from utils.tt4it_utils import *


def dh_home(request):
    backlinks = [{'name': 'TT4IT', 'url': 'dh:dh', 'para': ''}]
    usr, ui = getUsrUI(request)
    display_bg, slide_image_classify = (ui.display_bg, ui.classify) if ui else (True, '')

    if ui and ui.login_page != u'':
        return redirect(ui.login_page)
    else:
        return render(
            request,
            'dh/dh.html',
            dict(backlinks=backlinks, lists=getApp(request), usr=usr, display_bg=display_bg, slide_image_classify=slide_image_classify)
        )


def dh(request):
    backlinks = [{'name': 'TT4IT', 'url': 'dh:dh', 'para': ''}]
    usr, ui = getUsrUI(request)
    display_bg, slide_image_classify = (ui.display_bg, ui.classify) if ui else (True, '')

    return render(
        request,
        'dh/dh.html',
        dict(backlinks=backlinks, lists=getApp(request), usr=usr, display_bg=display_bg, slide_image_classify=slide_image_classify)
    )


def dh2(request):
    backlinks = [{'name': 'TT4IT', 'url': 'dh:dh', 'para': ''}]
    usr, ui = getUsrUI(request)
    display_bg, slide_image_classify, search_engine = (ui.display_bg, ui.classify, ui.search_engine) if ui else (True, '', '')

    return render(
        request,
        'dh/dh2.html',
        dict(usr=usr, display_bg=display_bg, slide_image_classify=slide_image_classify, search_engine=search_engine)
    )


def dh3(request):
    backlinks = [{'name': 'TT4IT', 'url': 'dh:dh', 'para': ''}]
    usr, ui = getUsrUI(request)
    display_bg, slide_image_classify, search_engine = (ui.display_bg, ui.classify, ui.search_engine) if ui else (True, '', '')

    return render(
        request,
        'dh/dh3.html',
        dict(usr=usr, display_bg=display_bg, slide_image_classify=slide_image_classify, search_engine=search_engine)
    )
