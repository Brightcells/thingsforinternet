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

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.encoding import smart_str

from accounts.models import UserInfo
from accounts.forms import SignupUserInfoModelForm, LoginUserInfoModelForm, ForgotUserInfoModelForm, SettingsUserInfoModelForm
from utils.json_utils import JsonHttpResponse
from utils.send_email import SendEmail
from utils.utils import getUsr, getUI

import json
import shortuuid

from utils.geetest import geetest
from utils.utils import *


MAX_AGE = settings.COOKIE_MAX_AGE
SEND_EMAIL = settings.SEND_EMAIL
GEE_TEST = settings.GEE_TEST


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


def del_cookie(request, response, key):
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
    form = LoginUserInfoModelForm()

    if request.method == 'POST':
        form = LoginUserInfoModelForm(request.POST)
        if form.is_valid():
            response = redirect(next_url)
            response.set_cookie('usr', smart_str(form.cleaned_data['username']), MAX_AGE)
            return response

    usr, ui = getUsrUI(request)
    display_bg, slide_image_classify = (ui.display_bg, ui.classify) if ui else (True, '')

    return render(
        request,
        'accounts/login.html',
        dict(backlinks=BACKLINKS, form=form, next=next_url, display_bg=display_bg, slide_image_classify=slide_image_classify)
    )


def signup(request):
    next_url = request.GET.get('next', '') or get_referer_view(request)
    form = SignupUserInfoModelForm()

    if request.method == 'POST':
        form = SignupUserInfoModelForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.display_bg = True
            f.save()
            response = redirect(next_url)
            response.set_cookie('usr', smart_str(form.cleaned_data['username']), MAX_AGE)
            return response

    usr, ui = getUsrUI(request)
    display_bg, slide_image_classify = (ui.display_bg, ui.classify) if ui else (True, '')

    return render(
        request,
        'accounts/signup.html',
        dict(backlinks=BACKLINKS, form=form, next=next_url, display_bg=display_bg, slide_image_classify=slide_image_classify)
    )


def logout(request):
    next_url = request.GET.get('next', '') or get_referer_view(request)
    response = redirect(next_url)
    del_cookie(request, response, 'usr')
    return response


def forgot(request):
    next_url = request.GET.get('next', '') or get_referer_view(request)
    form = ForgotUserInfoModelForm()

    base_url = GEE_TEST.get('base_url', '')
    captcha_id = GEE_TEST.get('captcha_id', '')
    private_key = GEE_TEST.get('private_key', '')
    product = GEE_TEST.get('product', '')

    gt = geetest(captcha_id, private_key)

    usr, ui = getUsrUI(request)
    display_bg, slide_image_classify = (ui.display_bg, ui.classify) if ui else (True, '')

    if request.method == 'POST':
        form = ForgotUserInfoModelForm(request.POST)
        if form.is_valid():
            challenge = request.POST.get('geetest_challenge', '')
            validate = request.POST.get('geetest_validate', '')
            seccode = request.POST.get('geetest_seccode', '')
            result = gt.geetest_validate(challenge, validate, seccode)

            if result:
                email = form.data.get('email', '')
                try:
                    userinfo = UserInfo.objects.get(email=email)
                except UserInfo.DoesNotExist:
                    userinfo = None
                if userinfo:
                    new_password = shortuuid.uuid()
                    userinfo.password = hashlib.md5(new_password).hexdigest()
                    userinfo.save()
                    smail = SendEmail(SEND_EMAIL.get('username', ''), SEND_EMAIL.get('password', ''))
                    smail.send_email(email, u'tt4it.com密码重置', u'用户名：{0}\n密    码：{1}'.format(userinfo.username, new_password))
                    return redirect(next_url)
            else:
                form.errors['email'] = form.errors.get('email') or [u'Geetest validate error']

    try:
        challenge = gt.geetest_register()
    except:
        challenge = ''
    if len(challenge) == 32:
        url = 'http://%s%s&challenge=%s&product=%s' % (base_url, captcha_id, challenge, product)
    else:
        url = ''

    return render(
        request,
        'accounts/forgot.html',
        dict(backlinks=BACKLINKS, form=form, next=next_url, display_bg=display_bg, slide_image_classify=slide_image_classify, url=url)
    )


def api_user_check(request):
    _usr = request.POST.get('usr', '')
    try:
        UserInfo.objects.get(username=_usr)
        status, msg = True, 'user_already_exists'
    except:
        status, msg = False, 'user_not_exists'
    return HttpResponse(json.dumps(dict(status=status, msg=msg)))


def password_reset(request):
    next_url = request.GET.get('next', '') or get_referer_view(request)
    form = ForgotUserInfoModelForm()

    usr, ui = getUsrUI(request)
    display_bg, slide_image_classify = (ui.display_bg, ui.classify) if ui else (True, '')

    return render(
        request,
        'accounts/login.html',
        dict(backlinks=BACKLINKS, form=form, next=next_url, display_bg=display_bg, slide_image_classify=slide_image_classify)
    )


def member(request, uid=None):
    usr, ui = getUsrUI(request)

    if not ui and not uid:
        return redirect(reverse('accounts:login'))

    userinfo, display_bg, slide_image_classify = (ui.data, ui.display_bg, ui.classify) if ui else (None, True, '')

    if uid:
        try:
            userinfo = UserInfo.objects.get(pk=uid).data
        except:
            userinfo = None

    return render(
        request,
        'accounts/member.html',
        dict(backlinks=BACKLINKS, usr=usr, userinfo=userinfo, lists=getApp(request), display_bg=display_bg, slide_image_classify=slide_image_classify)
    )


def settings(request):
    next_url = request.GET.get('next', '') or get_referer_view(request)
    usr, ui = getUsrUI(request)

    if not ui:
        return redirect(reverse('accounts:login'))

    form = SettingsUserInfoModelForm(initial=ui.data)

    if request.method == 'POST':
        form = SettingsUserInfoModelForm(request.POST, instance=ui)
        if form.is_valid():
            form.save()
            return redirect(next_url)

    display_bg, slide_image_classify = (ui.display_bg, ui.classify) if ui else (True, '')

    return render(
        request,
        'accounts/settings.html',
        dict(backlinks=BACKLINKS, usr=usr, form=form, next=next_url, lists=getApp(request), display_bg=display_bg, slide_image_classify=slide_image_classify)
    )
