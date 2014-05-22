# -*- coding: utf-8 -*-

###
# ErrorCode: 200***, for likeSite
#     {'errorCode': 200200, 'errorString': 'Like/Unlike the site success'}
#     {'errorCode': 200201, 'errorString': 'You have already like/unlike the site, don\'t hesitate'}
#     {'errorCode': 200202, 'errorString': 'Cancel like/unlike the site success'}
# ErrorCode: 300***, for Favorite
#     {'errorCode': 300200, 'errorString': 'Favorite the site success'}
#     {'errorCode': 300201, 'errorString': 'The parm of siteid not transmitted success'}
#     {'errorCode': 300202, 'errorString': 'Cancel favorite the site success'}
# ErrorCode: 400***, for Visit
#     {'errorCode': 400200, 'errorString': 'Record the visit success'}
#     {'errorCode': 400201, 'errorString': 'Record the visit failure'}
###

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


errorCodeDict = {
    'like_unlike_success': {'errorCode': 200200, 'errorString': 'Like/Unlike the site success'},
    'already_like_unlike': {'errorCode': 200201, 'errorString': 'You have already like/unlike the site, don\'t hesitate'},
    'cancel_like_unlike_success': {'errorCode': 200202, 'errorString': 'Cancel like/unlike the site success'},
    'favorite_site_success': {'errorCode': 300200, 'errorString': 'Favorite the site success'},
    'site_id_not_exists': {'errorCode': 300201, 'errorString': 'The parm of siteid not transmitted success'},
    'cancel_favorite_success': {'errorCode': 300202, 'errorString': 'Cancel favorite the site success'},
    'record_visit_success': {'errorCode': 400200, 'errorString': 'Record the visit success'},
    'record_visit_fail': {'errorCode': 400201, 'errorString': 'Record the visit failure'},
}


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
    return UserInfo.objects.get(username=usr) if usr else None


def getUsrUI(request):
    '''
        @function: get usr and object together
        @paras:
        @returns: (usr, ui) tuple
    '''
    return usr, getUI(getUsr(request)) if usr else usr, None


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


def getErrorCode(_key):
    '''
        @function: general control error code, return error code by key
        @paras: _key
        @returns: error code dict
    '''
    return errorCodeDict[_key]