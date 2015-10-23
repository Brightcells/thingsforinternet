# -*- coding: utf-8 -*-

"""
Copyright (c) 2014 Qimin Huang <kimi.huang@brightcells.com>

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

from django.shortcuts import render, redirect

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
