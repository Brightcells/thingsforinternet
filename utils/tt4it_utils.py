# -*- coding: utf-8 -*-

import string

from ipaddr import client_ip

from accounts.models import UserInfo
from dh.models import AppInfo, FunctionInfo
from resources.models import NavInfo


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
    except UserInfo.DoesNotExist:
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


def getUsrHost(request):
    '''
        @function: get usr and ip together
        @paras:
        @returns: (usr, ip) tuple
    '''
    return getUsr(request), client_ip(request)


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
    if _app:
        return FunctionInfo.objects.filter(app__name=string.upper(_app), display=True).order_by('position')
    else:
        return FunctionInfo.objects.filter(display=True).order_by('position')


def getNav(request, _func):
    '''
        @function: get all nav for a function from table Nav
        @paras:
        @returns: nav dict query set
    '''
    navs = NavInfo.objects.filter(func__name=string.upper(_func), display=True).order_by('position')
    return [nav.data for nav in navs]
