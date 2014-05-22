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

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils.encoding import smart_str

from accounts.models import UserInfo
from accounts.forms import SignupUserInfoModelForm, LoginUserInfoModelForm

import re
import json


BACKLINKS = [
    {'name': 'TT4IT', 'url': 'dh:dh', 'para': ''},
]


# ref & modify: https://djangosnippets.org/snippets/1474/
def get_referer_view(request, default='/'):
    '''
        @function: get the referer view of the current request
        @paras:
        @returns: ref string
    '''
    # if the user typed the url directly in the browser's address bar
    referer = request.META.get('HTTP_REFERER')
    if not referer:
        return default

    # remove the protocol and split the url at the slashes
    referer = re.sub('^https?:\/\/', '', referer).split('/')
    '''
    if referer[0] != request.META.get('SERVER_NAME'):
        return default
    '''

    # add the slash at the relative path's view and finished
    referer = u'/' + u'/'.join(referer[1:])
    return referer


def delCookie(request, response, key):
    '''
        @function: del cookie by key
        @paras:
            √ request -
            √ request -
            √ key - the key by which to del
        @returns: None
    '''
    if key in request.COOKIES:
        response.delete_cookie(key)


def login(request):
    next_url = request.GET.get('next', '') or get_referer_view(request)

    if request.method == 'GET':
        form = LoginUserInfoModelForm()
    else:
        form = LoginUserInfoModelForm(request.POST)
        if form.is_valid():
            response = HttpResponseRedirect(next_url)
            response.set_cookie('usr', smart_str(form.cleaned_data['username']))
            return response

    return render(request, 'accounts/login.html', dict(backlinks=BACKLINKS, form=form, next=next_url))


def signup(request):
    next_url = request.GET.get('next', '') or get_referer_view(request)

    if request.method == 'GET':
        form = SignupUserInfoModelForm()
    else:
        form = SignupUserInfoModelForm(request.POST)
        if form.is_valid():
            form.save()

            response = HttpResponseRedirect(next_url)
            response.set_cookie('usr', smart_str(form.cleaned_data['username']))
            return response

    return render(request, 'accounts/signup.html', dict(backlinks=BACKLINKS, form=form, next=next_url))


def logout(request):
    next_url = request.GET.get('next', '') or get_referer_view(request)
    response = HttpResponseRedirect(next_url)
    delCookie(request, response, 'usr')
    return response


def api_user_check(request):
    _usr = request.POST.get('usr', '')
    try:
        UserInfo.objects.get(username=_usr)
        return HttpResponse(json.dumps(dict(status=True, msg='user_already_exists')))
    except:
        return HttpResponse(json.dumps(dict(status=False, msg='user_not_exists')))