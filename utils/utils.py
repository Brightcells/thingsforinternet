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

from django.contrib.auth.models import User
from django.core import serializers
from django.core.urlresolvers import reverse
from django.db.models import Q, Count
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.utils.encoding import smart_str

from accounts.models import UserInfo
from dh.models import AppInfo, FunctionInfo
from resources.models import *

import re
import json
import time
import random
import string
import hashlib
import requests


def getUsr(request):
    '''
        @function: get usr from cookies, and if not exists, set usr None
        @paras:
        @returns: usr string
    '''
    return request.COOKIES['usr'] if 'usr' in request.COOKIES else None


def getUI(usr):
    '''
        @function: get usr object from UserInfo table
        @paras:
        @returns: usr string
    '''
    try:
        ui = UserInfo.objects.get(username=usr) if usr else None
    except:
        ui = None
    return ui


def getUsrUI(request):
    '''
        @function: get usr and object together
        @paras:
        @returns: (usr, ui) tuple
    '''
    usr = getUsr(request)
    return (usr, getUI(usr)) if usr else (usr, None)


def getIP(request):
    '''
        @function: get current ip for the desktop which visit from
        @paras:
        @returns: ip string
    '''
    return request.META['HTTP_X_FORWARDED_FOR'] if 'HTTP_X_FORWARDED_FOR' in request.META else request.META['REMOTE_ADDR']


def getUsrHost(request):
    '''
        @function: get usr and ip together
        @paras:
        @returns: (usr, ip) tuple
    '''
    return getUsr(request), getIP(request)


def getRef(request):
    '''
        @function: get ref from cookies, and if not exists, set ref 'dh:dh'
        @paras:
        @returns: ref string
    '''
    return request.COOKIES['ref'] if 'ref' in request.COOKIES else '/home'


def getApp(request):
    '''
        @function: get all app from table AppInfo
        @paras:
        @returns: app dict query set
    '''
    return AppInfo.objects.filter(display=True).order_by('position')


def getFunc(request, _app):
    '''
        @function: get all func for a app from table FunctionInfo
        @paras:
        @returns: func dict query set
    '''
    return FunctionInfo.objects.filter(app__name=string.upper(_app), display=True).order_by('position')


def getNav(request, _func):
    '''
        @function: get all nav for a function from table Nav
        @paras:
        @returns: nav dict query set
    '''
    return NavInfo.objects.filter(func__name=string.upper(_func), display=True).order_by('position')
